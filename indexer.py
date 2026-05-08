import os

def get_next_index():

    nums = []
    for file in os.listdir():
        if file.endswith(".txt") and file[:-4].isdigit():
            nums.append(int(file[:-4]))
    if len(nums) == 0:
        return 1
    return max(nums) + 1
