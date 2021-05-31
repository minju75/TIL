import sys

def solution2(n):
    num_list = list()
    for _ in range(n):
        num_list.append(int(sys.stdin.readline().strip()))

    max_num = max(num_list)

    print(max_num)
    print(num_list.index(max_num)+1)

if __name__ == "__main__":
    solution2(9)