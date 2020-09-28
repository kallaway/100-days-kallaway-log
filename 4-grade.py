import sys
def main():
    try:
        score = float(input("Enter Score: "))
        if not 0 < score < 1:
            raise
    except:
        print('Bad Score, enter a score between 0 and 1')
        sys.exit(0)

    print(computegrade(score))

def computegrade(score):
    if score >= 0.9:
        return('A')
    elif score >= 0.8:
        return('B')
    elif score >= 0.7:
        return('C')
    elif score >= 0.6:
        return('D')
    else:
        return('F')
if __name__ == '__main__':
    main()
