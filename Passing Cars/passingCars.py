def solution(A):
    passed = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] == 0 and A[j] == 1:
                passed += 1
    if passed > 1000000000:
        return -1
    return passed

def main():
    test = [0,1,0,1,1]
    print(solution(test))

if __name__ == "__main__":
    main()