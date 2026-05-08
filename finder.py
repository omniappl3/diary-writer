import os
import re
import platform
import subprocess

def find_keyword():
    results = 0
    files = 0
    print('='*3, "Find Keyword", '='*3)
    keyword = input("Enter keyword: ").strip()
    print('- ' * 10, '-', sep='')
    if not keyword:
        return
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    for file in os.listdir():
        if file.endswith(".txt") and file[:-4].isdigit():
            try:
                with open(file, "r", encoding="utf-8") as f:
                    found = False
                    for line_num, line in enumerate(f, start=1):
                        for match in pattern.finditer(line):
                            print(f"{file} | line {line_num} | col {match.start() + 1}")
                            results += 1
                            found = True
                    if found:
                        files += 1
                    
            except (UnicodeDecodeError, PermissionError):
                continue
    print('- ' * 10, '-', sep='')
    print(f"[{results}] Results found across [{files}] files")
    print('=' * 20)

if __name__ == "__main__":
    find_keyword()
