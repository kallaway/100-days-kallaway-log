import sys
def main():
    try:
        h = float(input("Enter Hours: "))
        r = float(input ("Enter Rate: $"))
    except:
        print('Error, please enter numeric input')
        sys.exit(0)

    print(f'${computepay(h, r)}')

def computepay(h, ra):
    if h > 40:
        ot = h - 40
        h = 40
    rb = ra * 1.5
    return round((h * ra) + (ot * rb), 2)

if __name__ == '__main__':
    main()
