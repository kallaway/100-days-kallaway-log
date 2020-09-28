import sys
def main():
    try:
        score = float(input("Enter Score: "))
        if not 0 < score < 1:
            raise
    except:
        print('Bad Score, enter a score between 0 and 1')
        sys.exit(0)

    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')
if __name__ == '__main__':
    main()
