# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
print("hello world!")
name = input("What is your name? ")
print("Nice to meet you,", name)

# function that takes parameters


# function that returns a value


# function with default value for an parameter


# function with variable number of parameters
def count_numbers(which, nums):
    if which != "even" and which != "odd":
        return -1
    
    result = 0
    for num in nums:
        if which == "even" and num % 2 == 0:
            result += 1
        if which == "odd" and num % 2 != 0:
            result += 1
    return result


print(count_numbers("even", [1,4,7,10,19,21,24,13,14]))
print(count_numbers("odd", [1,4,7,10,19,21,24,13,14]))
print(count_numbers("blarg", [1,4,7,10,19,21,24,13,14]))

