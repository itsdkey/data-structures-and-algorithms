from dropbox.database import Database


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
