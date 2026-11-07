def solution(X, Y, D):
    jumps = 0
    while X < Y:
        X = X + D #Adds the distance travelled
        jumps += 1 # increases jump by 1 everytime the frog jumps
    return jumps

def main():
    print(solution(10,85,30))

if __name__ == "__main__":
    main()