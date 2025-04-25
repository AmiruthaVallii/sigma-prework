# Given a list of integers, return the highest and lowest numbers in the array (without using max() or min())

def max_min(integer_list):
    # Sort the list
    sorted_list = sorted(integer_list)

    # Highest and lowest numbers in new array
    max_min_integers = [sorted_list[0], sorted_list[-1]]

    return max_min_integers


input_list = list(
    map(int, input("Enter a list of integers (separated by a space): ").split()))
print(max_min(input_list))
