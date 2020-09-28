def main():
    try:
        temp = float(input("Celsius: "))
    except:
        print('Please enter a number')

    temp = (temp * 1.8) + 32
    if temp % 1 == 0:
        temp = int(temp)
    print (f'Fahrenheit: {temp}')

if __name__ == '__main__':
    main()
