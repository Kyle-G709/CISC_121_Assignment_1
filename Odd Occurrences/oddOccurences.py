def solutions(A):
    pairs = {}
    for i in A:
        if i in pairs:
            pairs[i] += 1
        else:
            pairs[i] = 1
    for key,value in pairs.items():
        if value % 2 != 0:
            return key

def main():
    test = [9, 3, 9, 3, 9, 7, 9]
    print(solutions(test))

if __name__ == "__main__":
    main()