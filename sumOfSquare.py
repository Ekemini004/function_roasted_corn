
numbers = [2, 3, 4, 5, 7]

def square(list_input):

    sumOfElements = 0

    for index in range(0, len(numbers)):

        sumOfElements += (numbers[index]**2)

    return sumOfElements





print(square(numbers))
