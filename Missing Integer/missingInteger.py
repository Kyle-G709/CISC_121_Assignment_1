def solution(A):
    new_arr =[]
    for i in A:
        if i not in new_arr:
            new_arr.append(i)
    for i in range(1, len(new_arr) + 2):
        if i not in new_arr:
            return i
def main():
    test = [1, 3, 6, 4, 1, 2]
    print(solution(test))

if __name__ == "__main__":
    main()