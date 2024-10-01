import os
import filecmp

def compare_files(file1, file2):
    if filecmp.cmp(file1, file2, shallow=False):
        return "Files are similar"
    else:
        return "Files are not similar"

def main():
    file1 = "F:\\recovered_signal.txt"
    file2 = "F:\project\zhouyu\data\\result\solar_sys\smaller_scale\signal\signal.txt"

    if os.path.exists(file1) and os.path.exists(file2):
        result = compare_files(file1, file2)
        print(result)
    else:
        print("One or both files do not exist")

if __name__ == "__main__":
    main()