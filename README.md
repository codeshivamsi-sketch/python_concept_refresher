# Python Syntax & Concepts — Refresher

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)

Everything required to understand any Python codebase.

---

## 1 — Python Basics

1. Variables & data types — `str`, `int`, `float`, `bool`, `None`
2. Lists & dicts — `[]`, `{}`, `.append()`, indexing
3. `if / elif / else`
4. `for` loops
5. Functions — `def`, `return`, parameters, default values
6. String methods — `.strip()`, `.split()`, `.join()`, `.lower()`, `.replace()`
7. List/string slicing — `text[0:500]`
8. f-strings — `f"Hello {name}"`
9. Ternary — `x if condition else y`

---

## 2 — Modules & Environment

10. `import` / `from x import y`
11. `if __name__ == "__main__":`
12. `os.getenv()` — reading env vars / API keys
13. `global` keyword
14. `dir()` — inspect all methods/attributes of any object

---

## 3 — Data Handling

14. `json.loads()` / `json.dumps()`
15. `yaml` module
16. `base64` module
17. `bytes` type
18. `re` module — regex, `re.split()`, `re.sub()`

---

## 4 — Error Handling & Flow

19. `try / except / finally`
20. `raise`
21. `enumerate()` — `for i, item in enumerate(list):`
22. `assert` — used in testing

---

## 5 — Files & System

23. `with` statement — context manager
24. File I/O — `open()`, `.read()`, `.write()`
25. `pathlib.Path`
26. `subprocess` — running shell commands from Python

---

## 6 — Classes & OOP

27. Classes — `__init__`, `self`, methods
28. Inheritance — `class Child(Parent):`
29. Method chaining — `text.strip().lower().split()`
30. `dict.get()` with default — `data.get("key", fallback)`
31. `Enum` — `EntryType.DEBIT`, `EntryType.CREDIT`

---

## 7 — Type System

32. Type hints — `def fn(x: str) -> list[str]:`
33. `Optional[str]` — nullable types
34. `TypedDict` — typed dicts (used in LangGraph `AgentState`)
35. `Annotated` — `Annotated[list, add_messages]`

---

## 8 — Advanced Python

36. Decorators — `@app.get()`, `@tool`, `@pytest.mark.asyncio`
37. List comprehensions — `[x for x in items if x]`
38. Dict comprehensions — `{k: v for k, v in d.items()}`
39. `yield` — generators & FastAPI dependency injection
40. `uuid` — `uuid.UUID`, `uuid.uuid4()`

---

## 9 — Async

41. `async def` / `await`
42. `async with` — async context manager
43. `async for` — async iteration (Kafka consumer)
44. `asyncio.run()` — entry point for async scripts
45. `asyncio.create_task()` — background tasks
46. `@asynccontextmanager` — custom async context managers

---

## 10 — Library Patterns

> Not core Python syntax, but patterns that repeat across projects.

47. Pydantic `BaseModel` — auto-validation of request/response shapes
48. `dataclasses` — lightweight structured data
49. SQLAlchemy async ORM — `select()`, `execute()`, `scalars().all()`
50. `sessionmaker` — DB session factory
51. FastAPI `Depends()` — dependency injection + overrides in tests
52. `pytest` async testing — `@pytest.mark.asyncio`
53. `structlog` processors — structured JSON logging
