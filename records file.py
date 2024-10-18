#Christopher Kenny
#CS 175
#Records File

def main():
  found = False
  #Open the file
  employee_data = open('employees.txt', 'a')

  #Allow user to input data to be stored in generated file
  enter_data = int(input('How many employee records do you want to create: '))

  for x in range(enter_data):
    name = input('Enter employee name: ').upper()
    emp_id = input('Enter employee ID: ')
    emp_department = input('Enter employee department: ').upper()

    #Add user inputs to list
    employee_data.write(name + '\n')
    employee_data.write(emp_id + '\n')
    employee_data.write(emp_department + '\n')

  #Close file
  employee_data.close()

main()

