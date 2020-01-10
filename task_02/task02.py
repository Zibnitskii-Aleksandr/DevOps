#____________________________________________________ Task 1
print("[ Task 1 ]", "-" * 50, "\n")
name = input("Your name: ")
age = input("Your age: ")
print(f"Hello, {name}, your age is {age}", "\n")
#____________________________________________________ Task 2
print("[ Task 2 ]", "-" * 50, "\n")
num = input("Input integer: ")
extent = 132
total = int(num)**extent
ost_3 = int(total % 3)
print("You entered the number: {0}, result exponentiation 132: {1}, the remainder of dividing by 3: {2}".format(num, total, ost_3),"\n")
#____________________________________________________ Task 3
print("[ Task 3 ]", "-" * 50, "\n")
from random import randint
len_list = input("Input length list: ")
int_arr = [randint(1, 50) for i in range(int(len_list))]
even = 0
for i in int_arr:
    if i%2 == 0:
        even += 1
print("Length your list: ", len_list)
print("Your list: ", int_arr)
print("The number of even digits: ", even, "\n")
#____________________________________________________ Task 4
print("[ Task 4 ]", "-" * 50, "\n")
len_list = input("Input length list: ")
int_arr = [randint(1, 100) for i in range(int(len_list))]
print("Length your list: ", len_list)
print("Your list: ", int_arr)
print("The MAX value is ", max(int_arr), ", the MIN values is ", min(int_arr) , "\n")
#____________________________________________________ Task 5
print("[ Task 5 ]", "-" * 50, "\n")
from random import choice
from string import ascii_letters
vol_string = int(input("The total number of rows in the list: "))
max_length = int(input("Maximum line length ( >5 ): "))
arr_source = []
for i in range(vol_string):
    arr_source.append(''.join(choice(ascii_letters) for j in range(randint(5, max_length))))
print("Source list","."*10)
print(arr_source)
max_ind = 0
min_ind = 0
for i in range(vol_string):
    if len(arr_source[max_ind]) < len(arr_source[i]):
        max_ind = i
    elif len(arr_source[i]) < len(arr_source[min_ind]):
        min_ind = i
arr_dest = arr_source.copy()
arr_dest[max_ind], arr_dest[min_ind] = arr_dest[min_ind], arr_dest[max_ind]
print("\n", f"MAX index {max_ind}, MIN index {min_ind}")
print("\n", "Destinations list:","."*10)
print(arr_dest, "\n")
print("[ End All Task ]", "-" * 44, "\n")
