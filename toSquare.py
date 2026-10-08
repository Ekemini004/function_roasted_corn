
numbers = [2, 3, 4, 5, 7]

def square(list_input):

    result = []

    for index in range(0, len(numbers)):

        result.append(numbers[index]**2)

    return result





print(square(numbers))
