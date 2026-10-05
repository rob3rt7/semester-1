from util import read_numbers
import sys

numbers = read_numbers()
if numbers == []:
    sys.exit("Error: no numbers provided")

def fract(a):
    return a-int(a)

numbers.sort()
print(f"Minimum = {numbers[0]}")
print(f"Maximum = {numbers[len(numbers)-1]}")
print(f"Mean = {sum(numbers)/len(numbers)}")
median = numbers[len(numbers)//2]*(1.0-fract((len(numbers)-1)/2))
median += numbers[(len(numbers)//2)+1]*(fract((len(numbers)-1)/2))
print(f"Median = {median}")
    