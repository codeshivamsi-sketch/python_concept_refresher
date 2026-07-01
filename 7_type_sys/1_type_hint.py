def greet(name: str) -> str:
    return f"Hello {name}"


def add(a: int, b: int) -> int:
    return a + b


def get_users() -> list[str]:
    return ["tom", "harry"]


# python doesnt enforce it at runtime
# they are for readiblity/tooling, editor will warn if wrong type is passed






# variable type hints
name: str = "shivam"
age: int = 32
scores: list[int] = [90,22,67]
user: dict[str, str] = {"name": "shivam"}
