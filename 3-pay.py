def main():
    hrs = float(input("Enter Hours: "))
    ratea = float(input ("Enter Rate: $"))
    rateb = ratea * 1.5
    if hrs > 40:
        ot = hrs - 40
        hrs = 40
    print (f'${round((hrs * ratea) + (ot * rateb), 2)}')

if __name__ == "__main__":
    main()
