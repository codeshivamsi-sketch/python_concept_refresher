from pathlib import Path

p = Path("notes.txt")

print("exists: ", p.exists())
print("filename: ", p.name)
print("file suffix: ", p.suffix)
print("filename without extension: ", p.stem)



# Bulding path
folder = Path("my_folder")
file = folder / "notes.txt"
print(file)



# Reading / Writing
p = Path("notes.txt")
content = p.read_text()
print("content: ", content)

p.write_text("hello")




# Create folders
Path("new_folders").mkdir(exist_ok=True) # exist_ok does nothing if already exists, without it, this would crash.
