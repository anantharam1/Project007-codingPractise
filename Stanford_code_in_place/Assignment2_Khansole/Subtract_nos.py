#This program subtracts one number from another.
def main():
    print ('This program subtracts one number from another.')
#accept first no.
    x = input('Enter first number: '  )
#accept second no.
    y = input('Enter second number: ')
#convert the input received as string into a float
    x = float(x)
    y = float(y)
#subtract
    z = x-y
#print the final result
    print ('The result is ' + str(z))

if __name__ == '__main__':
    main()