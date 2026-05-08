from datetime import datetime


def menu():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"========== Main Menu ==========\nEnter[h] or [help] to view commands. \n[{timestamp}]\n====================")
