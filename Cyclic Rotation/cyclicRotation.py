def solution(A, K):
    for i in range(K):
        last = A[len(A) - 1] #Save the last element in the array
        for j in range(len(A)): #Swap the array element by 1
            temp = A[j]
            A[j] = last
            last = temp
    return A

def main():
    test_arr = [3, 8, 9, 7, 6]
    n = 3
    new_arr = solution(test_arr, n)
    print(new_arr)

if __name__ == "__main__":
    main()