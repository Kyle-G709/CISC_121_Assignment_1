def solutions(A):
    pairs = {} # create an empty dictionary
    for i in A: # for each element, add it to the dictionary or increase occurrence by 1
        if i in pairs: 
            pairs[i] += 1
        else:
            pairs[i] = 1
    for key,value in pairs.items(): 
        if value % 2 != 0: #Checks if key has a pair, and if it doesn't return the key
            return key

def main():
    test = [9, 3, 9, 3, 9, 7, 9]
    print(solutions(test))

if __name__ == "__main__":
    main()