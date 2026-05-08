import os
from datetime import datetime
from indexer import get_next_index

def write_entry():
    print('='*20,"\nDiary Writer")
    
    index = get_next_index()
    filename = f"{index}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Created: {created}\tIndex: {index}\n")
        file.write("=" * 40)
        print("- " * 10 + "-")
        print("Type [/exit] to save and quit.")
        while True:
            text = input("> ")
            if text == "/exit":
                break
            file.write(f"\n{text}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n[{timestamp}]")

    print("- " * 10 + "-")
    print(f"\nSaved in {filename} at index #{index}")
    print('='*40)
