import os
from indexer import get_next_index

def read_entry():
    index_count = get_next_index() - 1
    print('=' * 20)
    print(f"{index_count} entries found")
    print('- '*10 + '-')
    index = input("Enter diary index: ")
    print('-- -- -- -- -- -- --')
    if not index.isdigit():
        print("Invalid index")
        print('=' * 20)
        return
    filename = f"{index}.txt"
    if not os.path.exists(filename):
        print("Diary not found")
        print('=' * 20)
        return
    print()
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
        print('=' * 20)

if __name__ == "__main__":
    read_entry()
