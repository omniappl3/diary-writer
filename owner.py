import os

OWNER_FILE = "owner.txt"

def get_owner():

    if not os.path.exists(OWNER_FILE):
        owner = input("Enter owner name: ").strip()
        with open(OWNER_FILE, "w", encoding="utf-8") as file:
            file.write(owner)
        return owner
    with open(OWNER_FILE, "r", encoding="utf-8") as file:
        return file.read().strip()
