import unittest


def get_answer(number):
    if number % 15==0:
        return "FizzBuzz"
    if number % 3==0:
        return "Fizz"
    elif number % 5== 0:
        return "Buzz"

    return  number

print(get_answer(15))
assert (get_answer(1)==1)
assert (get_answer(2)==2)
assert (get_answer(3)=="Fizz")
assert (get_answer(6)=="Fizz")
assert (get_answer(5)=="Buzz")
assert (get_answer(10)=="Buzz")
assert (get_answer(15)=="FizzBuzz")
assert (get_answer(30)=="FizzBuzz")

for number in range(1,100):
    print("number=", number)
    print("get_answer=", get_answer(number))

