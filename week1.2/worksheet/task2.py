from util import read_numbers
import sys

numbers = read_numbers()
if numbers == []:
    sys.exit("Error: no numbers provided")

numbers.sort()
print(f"Minimum = {numbers[0]}")
print(f"Maximum = {numbers[len(numbers)-1]}")
print(f"Mean = {sum(numbers)/len(numbers)}")
print(f"Median = {numbers[(len(numbers)-1)//2]}")
    