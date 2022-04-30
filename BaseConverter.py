print("Welcome to number bases converter ! ")

def main():

    def EncoderNum(num,base):
        conversion = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if base == 1 or base > len(conversion):
            return num
        result = ''
        while num > 0:
            result += conversion[num % base]
            num = num // base
        return result[::-1]

    def DecoderNum(num,base) :
        conversion = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if base == 1 or base > len(conversion):
            return num
        result = 0
        n = len(num)-1
        for i in num:
            result += conversion.index(i)*(base**n)
            n -= 1
        return result

    while True:
        try:
            print('Type 1 to convert decimal to base or 2 to convert base to decimal : ')
            choice = int(input(">>> "))
            if choice == 1 or choice == 2:
                break
        except:
            print("Please enter a number ! ")

    if choice == 1:
        number = int(input("Enter the number to convert : "))
        bs = int(input("Enter the base : "))
        print('The converted number is : ')
        print(EncoderNum(number,bs))


    if choice == 2:
        number = str(input("Enter the number to convert : "))
        bs = int(input("Enter the base : "))
        print('The converted number is : ')
        print(DecoderNum(number, bs))

    chs = str(input("Do u want to retry ? (y/n) : "))

    if chs == 'y' or chs == 'Y' or chs == 'Yes' or chs == 'yes':
        main()

if __name__ == '__main__':
    main()