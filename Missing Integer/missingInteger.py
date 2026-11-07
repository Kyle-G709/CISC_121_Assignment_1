def solution(A):
    new_arr =[]
    for i in A:
        if i not in new_arr:#if the integer is not added to the new array add it
            new_arr.append(i)
    for i in range(1, len(new_arr) + 2): #checks from 1 to the end of the array + 1 to see if that number is in there
        if i not in new_arr: #the first number that isn't in there is the smallest number and return it
            return i
def main():
    test = [1, 3, 6, 4, 1, 2]
    print(solution(test))

if __name__ == "__main__":
    main()