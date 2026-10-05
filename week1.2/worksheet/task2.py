from util import read_numbers
import sys

fract = lambda a : a-int(a)
numbers = read_numbers()
if not numbers: sys.exit("Error: no numbers provided")

numbers.sort()
print(f"Minimum = {numbers[0]}")
print(f"Maximum = {numbers[len(numbers)-1]}")
print(f"Mean = {sum(numbers)/len(numbers)}")
median = numbers[(len(numbers)-1)//2]*(1.0-fract((len(numbers)-1)/2))
median += numbers[min(((len(numbers)-1)//2)+1, len(numbers)-1)]*(fract((len(numbers)-1)/2))  
print(f"Median = {median}")
    