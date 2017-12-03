import unittest


def get_answer(number):
    if number ==3:
        return "Fizz"
    return  number


assert (get_answer(1)==1)
assert (get_answer(2)==2)
assert (get_answer(3)=="Fizz")
