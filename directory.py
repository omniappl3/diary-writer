import os

def view_directory():

    files = []
    for file in os.listdir():
        if file.endswith(".txt") and file[:-4].isdigit():
            files.append(file)
    if len(files) == 0:
        print("No diary files found")
        return
    files.sort(key=lambda x: int(x[:-4]))
    print("\n==== Diary Directory ====\n")
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
        print(f"{file} -> {first_line}")
    print("=========================")
