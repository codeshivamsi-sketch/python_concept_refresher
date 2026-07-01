from enum import Enum

class EntryType(Enum):
    DEBIT = "debit"
    CREDIT = "credit"

print(EntryType.DEBIT)
print(EntryType.DEBIT.value)


class EntryType2(str, Enum):
    DEBIT = "debit"


print(EntryType.DEBIT == "debit") # This returns false since type is not str.
print(EntryType2.DEBIT == "debit")
