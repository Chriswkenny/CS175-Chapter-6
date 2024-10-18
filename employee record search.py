#Christopher Kenny
#CS 175
#Employee Record Search


def main():
  found = False
  name_search = input("Enter the name of the employee you would like to look up: ").upper()
#Open the File
  employee_data = open('employees.txt', 'r')
#Read the first name
  name = employee_data.readline()

  while name != '':
    #Read ID
    emp_id = employee_data.readline()
    #Read Department
    emp_department = employee_data.readline()

    #Strip new lines
    emp_id = emp_id.rstrip('\n')
    emp_department = emp_department.rstrip('\n')
    name = name.rstrip('\n')

    if name == name_search:
      found = True
      print(f"{name}'s User ID is {emp_id}. {name} works in the {emp_department} department.")

    name = employee_data.readline()

  employee_data.close()

  if not found:
    print(f"{name_search} was not found in the file.")

#Call Function
main()
