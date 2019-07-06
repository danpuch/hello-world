def fizzbuzz(number):

    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz" "{} is divisible by 3 and 5".format(number)
    elif number % 3 == 0:
        return "Fizz" "{} is divisible by 3".format(number)
    elif number % 5 == 0:
        return "Buzz" "{} is divisible by 5".format(number)
    else:
        return str(number) , " {} is not divisible by 3 and 5".format(number)

calce=fizzbuzz(15)
print(calce)