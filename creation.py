import pandas as pd


def create_students():
  """
  Takes the user through the student creation process
  """
  print("\nYou are creating a students table\n\nID: integer, id of student\nName: string, name of student\nYear: int, how many years the student has been at the college\nMajor: string, name of their major\n")
  sList = []
  a = True
  while a == True:
   id = input("Enter student ID: ")
   name = input("Enter name of student: ")
   year = input("Enter year of student: ")
   major = input("Enter major of student: ")

   dict = {"studentID": id,"Name": name, "year": year, "major": major}
   sList.append(dict)

   user = input("Would you like to enter another entry? (yes to continue/anything else to stop): ")
   if user != 'yes':
     a = False
   return pd.DataFrame(sList)
  


def create_prof():
  """
  Takes the user through the prof creation process
  """

  print("\nYou are now creating the professors table\n\nID: integer, ID of professor\nName: string, name of professor\nYears of Experience: int, number of years the professor has in education\n")
  pList = []
  cont = True
  while cont == True:
    id = input("Enter professor ID: ")
    name = input("Enter name: ")
    years = input("Enter years of experience: ")

    dict = {"profID": id, "Name": name, "years_of_exp": years}
    pList.append(dict)
    
    user = input("Would you like to enter another entry? (yes to continue/anything else to stop): ")
    if user != 'yes':
        cont = False
  
  return pd.DataFrame(pList) 


def create_degrees():
  """
  Takes the user through the degree creation process

  """
  print("\nYou are now creating the Degrees table\n\nID: integer, ID of degree\nName: string, name of degree\nRequired Classes: list of ints, list of the required IDs for classes")

  dList = []
  a = True
  while a == True:
    degreeID = int(input("Enter degreeID: "))
    d_name = input("Enter name of degree: ")
    req_classes = input("Enter the required class IDs for this degree, seperated by commas: ")
    req_list = req_classes.split(",")

    x = input("Enter Y if this degree is undergrad, anything else if not: ")
    if x == 'Y' or x == 'y':
      undergrad = True
    else:
      undergrad = False

    dict = {"degreeID": degreeID, "degree_name": d_name, "req_classID": req_list, "undergrad": undergrad}
    dList.append(dict)

    user = input("Would you like to enter another entry? (yes to continue/anything else to stop): ")
    if user != 'yes':
        a = False
  return pd.DataFrame(dList)

def create_classes():
  """
  Takes user through the classes creation process
  """
  a = True
  print("\nYou are now creating the classes table\n\nClass ID: integer, enter ID of class\nClass Name: string, Name of class\nProfessor ID: integer, ID of professor\nStudent ID: integer, ID of student\nGrade: char, Letter grade of student")
  cList = []
  while a == True:
    classID = input("Enter class ID: ")
    c_name = input("Enter name of class: ")
    professorID = input("Enter ID of professor")
    studentID = input("Enter the ID of the student: ")
    grade = input("Enter grade: ")

    dict = {"classID": classID, "Name": c_name, "professorID": professorID, "studentID": studentID, "grade": grade}
    cList.append(dict)

    user = input("Would you like to enter another entry? (yes to continue/anything else to stop): ")
    if user != 'yes':
        a = False
  return pd.DataFrame(cList)


def create():
    print("\nHello, welcome to creation mode.\nYou will be taken through each table and asked to enter records.\n\n")

    student_df = create_students()
    professor_df = create_prof()
    degrees_df = create_degrees()
    classes_df = create_classes()

    student_df.to_csv("Students.csv", index = False)
    professor_df.to_csv("Professors.csv", index = False)
    degrees_df.to_csv("Degrees.csv", index = False)
    classes_df.to_csv("Classes.csv", index = False)

