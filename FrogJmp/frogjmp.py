def solution(X, Y, D):
    jumps = 0
    while X < Y:
        X = X + D
        jumps += 1
    return jumps

def main():
    print(solution(10,85,30))

if __name__ == "__main__":
    main()