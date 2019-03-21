def fizzbuzz(list1, list2):

    x = len(list1) + len(list2)
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    if x % 3 == 0:
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"

    return x
