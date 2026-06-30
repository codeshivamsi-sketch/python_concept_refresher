from fastapi import HTTPException

def divide(a, b):
    if b == 0:
        raise ValueError("b can't be 0")
    return a / b

print(divide(10, 1))
# divide(10,0)




try:
    divide(10, 0)
except ValueError as e:
    print(f"Caught: {e}")



try: 
    # API_KEY = None
    # if not API_KEY:
    #     raise ValueError("API_KEY is not set")

    amount = -1
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
except Exception as e:
    print(f"Err: ", e)


