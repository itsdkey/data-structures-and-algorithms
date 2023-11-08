from collections import defaultdict
from typing import Iterator

FieldWithTTL = dict[str, int]
Record = dict[str, int | FieldWithTTL]


class Database:
    database: dict[str, Record] = defaultdict(Record)

    def set(
        self, timestamp: str, key: str, field: str, value: str | FieldWithTTL
    ) -> str:
        if isinstance(value, str):
            value = int(value)
        self.database[key][field] = value
        return ""

    def compare_and_set(
        self,
        timestamp: str,
        key: str,
        field: str,
        expected_value: str,
        new_value: str | FieldWithTTL,
    ) -> str:
        value = self.get(timestamp, key, field)
        if value == int(expected_value):
            self.set(timestamp, key, field, new_value)
            return "true"
        return "false"

    def set_with_ttl(
        self, timestamp: str, key: str, field: str, value: str, ttl: str
    ) -> str:
        value = {
            "value": int(value),
            "ttl": int(timestamp) + int(ttl),
        }
        return self.set(timestamp, key, field, value)

    def compare_and_set_with_ttl(
        self,
        timestamp: str,
        key: str,
        field: str,
        expected_value: str,
        new_value: str,
        ttl: str,
    ) -> str:
        new_value = {
            "value": int(new_value),
            "ttl": int(timestamp) + int(ttl),
        }
        return self.compare_and_set(timestamp, key, field, expected_value, new_value)

    def compare_and_delete(
        self, timestamp: str, key: str, field: str, expected_value: str
    ) -> str:
        value = self.get(timestamp, key, field)
        if value == int(expected_value):
            self.database[key].pop(field)
            return "true"
        return "false"

    def get(self, timestamp: str, key: str, field: str) -> str:
        value = self.database.get(key, {}).get(field, "")
        if isinstance(value, dict):
            value, ttl = value["value"], value["ttl"]
            if ttl <= int(timestamp):
                self.database[key].pop(field)
                value = ""
        return value

    def scan(self, timestamp: str, key: str) -> str:
        result = ""
        if record := self.database.get(key):
            keys = iter(sorted(record.keys()))
            return self._prepare_record_info(int(timestamp), record, keys)
        return result

    def scan_with_prefix(self, timestamp: str, key: str, prefix: str) -> str:
        result = ""
        if record := self.database.get(key):
            keys = filter(lambda f: f.startswith(prefix), sorted(record.keys()))
            return self._prepare_record_info(int(timestamp), record, keys)
        return result

    @staticmethod
    def _prepare_record_info(timestamp: int, record: Record, keys: Iterator) -> str:
        values = []
        for field in keys:
            field_value = record[field]
            if isinstance(field_value, dict):
                field_value, ttl = field_value["value"], field_value["ttl"]
                if ttl > timestamp:
                    values.append(f"{field}({field_value})")
            else:
                values.append(f"{field}({field_value})")
        return ", ".join(values)


def solution(queries: list[list[str]]) -> list:
    output = []
    database = Database()
    for query in queries:
        operation, *args = query
        if method := getattr(database, operation.lower(), None):
            output.append(method(*args))
        else:
            raise ValueError(f"Operation {operation} does not exist")
    return output
