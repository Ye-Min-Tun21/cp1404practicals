# 1.

out_file = open("name.txt", "w")
name = input("Please enter your name: ")
print(name, file=out_file)
out_file.close()

# 2.

with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)

# 3.

with open("numbers.txt", "r") as in_file:

    num1 = int(in_file.readline().strip())
    num2 = int(in_file.readline().strip())
    in_file.close()

result = num1 + num2
print("The sum of the first two numbers is:", result)

# 4.


with open("numbers.txt", "r") as in_file:
    numbers = [int(line.strip()) for line in in_file]

result = sum(numbers)
print("The sum of all the numbers is:", result)
