import os
import filecmp

def compare_files(file1, file2):
    if filecmp.cmp(file1, file2, shallow=False):
        return "信号文件相同，咒语成立"
    else:
        return "信号文件不相同，咒语可能成立"

def main():
    file1 = "D:\\temp\\spell-from-ThreeBodyTrilogy-main\\data\\result\\solar-sys\\signal\\signal.txt"
    file2 = input("输入恢复信号文件路径（来自recover_signal.py）: ")

    if os.path.exists(file1) and os.path.exists(file2):
        result = compare_files(file1, file2)
        print(result)
    else:
        print("One or both files do not exist")

if __name__ == "__main__":
    main()
