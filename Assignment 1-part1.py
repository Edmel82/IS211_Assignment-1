#IS-211 Assignment1-Part1 (Edwards Meliton)

def list_divide(numbers, divide=2):
    #This should return the numbers in the list that aew divisible by divide.
    count = 0
    for num in numbers:
        if num % divide == 0:
            count += 1
    return count

def test_list_divide():
    #This is the first test case
    assert list_divide([1, 2, 3, 4, 5]) == 2

    #This is the second test case
    assert list_divide([2, 4, 6, 8, 10]) == 5

    #This is the third test case that should return 0
    assert list_divide(30, 54, 63, 98, 100], divide=10) == 2

    #This is fourth case with an empty list
    assert list_divide([]) == 0

    #This is the fifth case
    assert list_divide([1, 2, 3, 4, 5], divide=1) == 5

#This will call the test function
test_list_divide()
