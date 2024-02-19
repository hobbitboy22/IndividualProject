import os

filepath = "/path/thing/hello/file.png"

directory, filename = os.path.splitext(filepath)

print(directory)
print(filename)

splitted = filename.split('.')[1]
print(splitted)