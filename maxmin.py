
def min_max():
    number_list = input(
        'Enter a list of numbers separated by spaces: ').strip().split(' ')
    for i in range(len(number_list)):
        number_list[i] = int(number_list[i])
    sorted_numbers = sorted(number_list)
    min_max_numbers = [sorted_numbers[0], sorted_numbers[-1]]
    return min_max_numbers


print(min_max())
