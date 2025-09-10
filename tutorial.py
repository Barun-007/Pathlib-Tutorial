import os
from pathlib import Path

"""
Pathlib module is introduce in Python version 3.4. It's a very convenient way to manipulate path over the Python OS module.
Pathlib uses OOP concept that's why it's becoming the developer 1st choice. So let's see how Pathlib works...
"""

## 1. To print current working directory
print(Path.cwd())  # using pathlib module
print(os.getcwd())  # using os module

## 2. To print all the files & folders within the current working directory
for p in Path().iterdir():
    print(p)

# Create a specific path object
my_dir = Path("Directory_1")
my_file = Path("file_1.txt")

print(type(my_dir))
print(my_file.name)

## 3. To get the extension of the file
print(my_dir.suffix)  # since it's a file that's why it has no extension
print(my_file.suffix)

## 4. To get the file name without the extension
print(my_dir.stem)
print(my_file.stem)

# Let's create a file path in the Directory_1 folder
new_file = "Sample.txt"
new_file_path = my_dir / my_file
print(new_file_path)

## 5. To check if any file or folder exist or not
print(my_dir.exists())
print(my_file.exists())
print(new_file_path.exists())

## 6. To see the parent directory of any path (files or folder)
print(my_dir.parent)
print(my_file.parent)  # . indicate that the current working directory
print(new_file_path.parent)

## 7. To see the absolute path
print(my_dir.parent.absolute())
print(my_file.parent.absolute())
print(new_file_path.parent.absolute())

## 8. Another way to see absolute path
"""
Most of the time to retreive the absolute path you use `resolve()` method
"""
print(my_dir.parent.resolve())
print(my_file.parent.resolve())

p = Path("..").resolve() # absolute() doesn't work here.
print(p)

## 9. To print current file's absolute path using pathlib
print(Path(__file__).resolve().parent) # __file__ is a special variable in Python that provides the path to the current file

## 10. Let's say we wanted to get access user's home directory
p = Path("~/dotfiles").expanduser() # resolve() doesn't work here
print(p)
# You can use Path.home() also
p = Path.home() / "dotfiles" # recommended for building path from scratch
print(p)

## 11. Advance searching methods using glob
dotfiles = Path.home() / "YOU CAN"
for p in dotfiles.rglob("*vscode*", case_sensitive=False): # glob only searches the path directory not the sub-directories. rglob search the sub-directories also
    print(p) # rgolob stands for recursive glob, additionally glob is also case sensetive

# Let's say you want to find .json file
dotfiles = Path.home() / "dotfiles"
for p in dotfiles.rglob("*.json"):
    print(p)

## 12. To open the file using pathlib
# Create a pathlib Path object
file_path = Path("file_1.txt")
# Open this file_path
with open(file_path) as f: # you can use file_path.open() (Path_object.open())
    print(f.read())

## 13. Create a new directory
p = Path("Temp_dir")
p.mkdir(exist_ok=True, parents=True) # exist_ok=True handles the if the file or folder already exist. parents=True handles if the parent directories don’t exist, create them too.

## 14. To remove a directory (should be an empty directory), for deleting non-empty directory use Python shutil module.
p.rmdir()

# 15. Create a file
p = Path("Temp_file.txt")
p.touch(exist_ok=True) # here by default exist_ok=True, but I mention it

## 16. Rename a file or folder
# Using rename() method
# p.rename(target="tempfile.txt") # rename() don't overwrite the file, also throw an error if the target file already exist
# Using replace() method()
temp_path = p.replace("tempfile.txt") # replace() overwrite the file if it's exist

## 17. To delete a file use unlink() method
temp_path.unlink()

print(Path("Helllo.py").exists())
print(Path("Helllo.py").is_file())