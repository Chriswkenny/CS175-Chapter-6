#Christopher Kenny
#CS 175
#Read a file to add numbers

def add_numbers():
  numbers = open('numbers.txt', 'r')
  number1 = int(numbers.readline())
  number2 = int(numbers.readline())
  number3 = int(numbers.readline())


  average = (number1 + number2 + number3) / 3

  print(f"The numbers are: {number1}, {number2}, {number3}.")
  print(f"The total is: {average}")

add_numbers()
