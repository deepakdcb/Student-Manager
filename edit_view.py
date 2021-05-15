import pandas as pd
import seaborn as sns

#CLASSES
class student:
  def __init__(self, id, name, year, major):
    """
    name expects string
    year expects int, should be what year student is in (1, 2, 3, 4)
    grades expects list of strings, contating all grades
    """
    self.id = int(id)
    self.name = name
    self.year = int(year)
    self.major = major


class prof:
  def __init__(self, id, name , years):
    """
    name expects string
    classes expects list of objects, containg every object class they teach
    """
    self.id = id
    self.name = name
    self.years = years

class degree:
  def __init__(self, id, name, req_classes, undergrad):
    """
    d_name expects string, name of degree (Bachelor in Information Science)
    req_classes expects list of classes(c) objects
    undergrad expects a boolean true or false, used to indicate whether the degree is a undergrad degree or not
    """
    self.id = id
    self.name = name
    self.req_classes = req_classes
    if undergrad == "True":
        undergrad = True
    else:
        undergrad = False
    self.undergrad = undergrad

class c:
  def __init__(self, id, name, professorID, studentID, grade):
    """
    name expects String, following a specific format (INST326 instead of inst 326 or just programming)
    professor expects string, name of professor teaching the class
    students expects list of student objects 
    """
    self.id = id
    self.name = name
    self.professorID = professorID
    self.studentID = studentID
    self.grade = grade
    

def student_obj(students): 
    """
    students to objects, expects students dataframe
    converts dataframe of students to list of student objects
    """
    slist = [(student(row.studentID, row.Name, row.year, row.major)) for index, row in students.iterrows()]
    return slist




def prof_obj(professors):
    """
    professors to objects, expects professors dataframe
    converts dataframe of professors to list of professor objects
    """
    plist = [(prof(row.profID, row.Name, row.years_of_exp)) for index, row in professors.iterrows()]
    return plist




def degree_obj(degrees):
    """
    degrees to objects
    """
    dlist = [(degree(row.degreeID, row.degree_name, row.req_classID, row.undergrad)) for index, row in degrees.iterrows()]
    return dlist




def class_obj(classes):
    cList = [(c(row.classID,row.Name,row.professorID,row.studentID, row.grade)) for index, row in classes.iterrows()]
    return cList




def edit_students(sList, students):
    """
    edit_students, expects list of student objects and student dataframe, lets user choose a record in the table and edit it
    """
    user = input("Before you edit, would you like to view all records in student table? (yes to view, anything else for no): ")
    if user == 'yes':
        print(students.to_string())
    cont = True
    while cont == True:
        id = int(input("Which student do you want to edit? (Enter their ID): "))
        for s in sList:
            if id == s.id:
                print("ID        Name        Year        Major")
                print("\n\n" + str(s.id) + "       " + s.name + "        " + str(s.year) + "        " + s.major)
                #Check for valid input
                s.id = int(input("Enter ID: "))
                if type(s.id ) != int:
                    while type(s.id) != int:
                        s.id = input("Enter valid ID: ")
                s.name = input("Enter Name: ")
                s.year = int(input("Enter year: "))
                if type(s.year) != int:
                    while type(s.year) != int:
                        s.year = input("Enter valid year: ")
                s.major = input("Enter Major: ")
        user = input("Would you like to edit another record? (yes for another entry, anything else for no)")
        if user != 'yes':
            cont = False
    return sList

def edit_prof(pList, professors):
    """
    edit professors, expects list of professor objects and professors dataframe
    lets user choose a record in the table and edit it
    """
    user = input("Before you edit, would you like to view all records in the professor table? (yes to view, anything else for no): ")
    if user == 'yes':
        print(professors.to_string())
    cont = True
    while cont == True:
        id = int(input("Which professor do you want to edit? (Enter their ID): "))
        print("ID        Name       Years of Experience")
        for p in pList:
            if id == p.id:
                print(str(p.id) + "        " + str(p.name) + "        " + str(p.years))
                p.id = int(input("Enter ID: "))
                #check for valid input
                if type(p.id) != int:
                    while type(p.id) != int:
                        p.id = input("Enter Valid ID: ")
                p.name = input("Enter Name")
                p.years = int(input("Enter years of experience"))
                #check for valid input
                if type(p.years) != int:
                    s.year = input("Enter valid year: ")
        user = input("Would you like to edit another record? (yes for another entry, anything else for no)")
        if user != 'yes':
            cont = False
    return pList

def edit_degree(dList, degrees):
    """
    edit degrees, expects list of degree objects and degrees dataframe
    lets user choose a record in the table and edit it
    """
    user = input("Before you edit, would you like to view all records in the degrees table? (yes to view, anything else for no): ")
    if user == 'yes':
        print(degrees.to_string())
    cont = True
    while cont == True:
        id = int(input("Which degree do you want to edit? (Enter its ID): "))
        print("ID        Name        Required Classes        Undergrad")
        for d in dList:
            if id == d.id:
                print(str(d.id) + "        " + d.name + "        " + str(d.req_classes) + "        " + str(d.undergrad))
                d.id = int(input("Enter ID: "))
                d.name = input("Enter Name: ")
                d.req_classes = input("Enter Classes required, seperated by comma: ")
                d.req_classes = d.req_classes.split(",")
                d.undergrad = input("Enter true or false for undergrad")
                #convert undergrad to True or False bool
                if d.undergrad == "True":
                    d.undergrad = True
                elif d.undergrad == "False":
                    d.undergrad = False
                else:
                    while type(d.undergrad) != bool:
                        d.undergrad = input("Enter valid entry for undergrad: ")
                        if d.undergrad == "True":
                            d.undergrad = True
                        elif d.undergrad == "False":
                            d.undergrad = False
        user = input("Would you like to edit another record? (yes for another entry, anything else for no)")
        if user != 'yes':
            cont = False
    return dList


def edit_classes(cList, classes):
    """
    edit classes, expects list of class objects and classes dataframe
    lets user choose a record in the table and edit it
    """
    #print table before edit if user wants
    user = input("Before you edit, would you like to view all records in the degrees table? (yes to view, anything else for no): ")
    if user == 'yes':
        print(classes.to_string())

    #while loop for indefinite edits until user is done
    cont = True
    while cont == True:
        id = int(input("Which class do you want to edit? (Enter its ID): "))
        for cs in cList:
            if cs == cs.id:
                print(str(d.id) + "        " + d.name + "        " + str(d.req_classes) + "        " + str(d.undergrad))
                cs.id = int(input("Enter ID: "))
                cs.name = input("Enter name: ")
                cs.professorID = int(input("Enter professor ID: "))
                cs.studentID = int(input("Enter Student ID"))
                cs.grade = input("Enter grade")
                cs.grade.upper()
                #checks to see if user entered valid letter grade
                if cs.grade!= 'A' or cs.grade!= 'B' or cs.grade!= 'C' or cs.grade!= 'D' or cs.grade!= 'F':
                    while cs.grade != cs.grade!= 'A' or cs.grade!= 'B' or cs.grade!= 'C' or cs.grade!= 'D' or cs.grade!= 'F':
                        cs.grade = input("Enter valid grade")
                        cs.grade.upper()

        user = input("Would you like to edit another record? (yes for another entry, anything else for no)")
        if user != 'yes':
            cont = False
    return cList


def eoe(sList, pList, dList, cList, args):
    """
    End of edit, this function  gets run at the end of the edit function. 
    Converts students objects to list of dictonaries, then to a pandas dataframe, then gets saved into a csv file
    """

    #create list of dictionaries for each table
    slist_dict = []
    plist_dict = []
    dlist_dict = []
    clist_dict = []

    #creates dictionary for each row, then adds it to list
    for s in sList:
        dict = {"studentID": s.id,"Name": s.name, "year": s.year, "major": s.major}
        slist_dict.append(dict)

    for p in pList:
        dict = {"profID": p.id, "Name": p.name, "years_of_exp": p.years}
        plist_dict.append(dict)

    for d in dList:
        dict = {"degreeID": d.id, "degree_name": d.name, "req_classID": d.req_classes, "undergrad": d.undergrad}
        dlist_dict.append(dict)

    for cs in cList:
        dict = {"classID": cs.id, "Name": cs.name, "professorID": cs.professorID, "studentID": cs.studentID, "grade": cs.grade}
        clist_dict.append(dict)


    #converts list of dictionaries to pandas dataframe
    spd = pd.DataFrame(slist_dict)
    ppd = pd.DataFrame(plist_dict)
    dpd = pd.DataFrame(dlist_dict)
    cpd = pd.DataFrame(clist_dict)

    #save to csv files
    spd.to_csv(args[0], index = False)
    ppd.to_csv(args[1], index = False)
    dpd.to_csv(args[2], index = False)
    cpd.to_csv(args[3], index = False)



def student_graph(students, classes):
    cont = True
    while cont == True:
        user = input("Would you like to view all students (warning, large datasets can easily overload labels), or pick which students you want? (all for all students, pick to pick students): ")
        if user == 'all':
            #all prints all students
            new_df = students.merge(classes, on='studentID')
            graph = sns.countplot(x = 'Name_x', hue = 'grade', data = new_df)
            graph.set(xlabel='Student Name', ylabel = "Grades")
            graph.figure.savefig("graph.png")
            cont = False
        elif user == 'pick':
            user = input("Enter all IDs you want to see, seperated by comma: ")
            sList = user.split(",")
            
            sList = list(map(int, sList))

            #filtered dataframe of desiered rows
            f_df = students[students.studentID.isin(sList)]

            #merged dataframe with classes
            new_df = f_df.merge(classes, on='studentID')

            graph = sns.countplot(x = 'Name_x', hue = 'grade', data = new_df)
            graph.set(xlabel='Student Name', ylabel = "Grades")
            graph.figure.savefig("graph.png")
            cont = False

        else:
            print("Error, wrong input")
    print("\n\nThe graph has been saved to a PNG in the directory you ran the file in\nIf you do not see one of the IDs you asked for in the graph, it may be because the classes table does not have a row with that Student ID")

def prof_graph(professors, classes):
    """
    professor graph, user picks what type of graph they want to see
    """
    classes.rename(columns = {'professorID':'profID'}, inplace = True)
    cont = True
    while cont == True:
        user = input("Would you like to view all professors (warning, large datasets can easily overload labels), or pick which students you want? (all for all students, pick to pick students): ")
        if user == 'all':
            #all will graph all rows
            new_df = professors.merge(classes, on='profID')
            graph = sns.countplot(x = 'Name_x', hue = 'grade', data = new_df)
            graph.set(xlabel='Professor Name', ylabel = "Grades")
            graph.figure.savefig("graph.png")
            cont = False
        elif user == 'pick':
            user = input("Enter all IDs you want to see, seperated by comma: ")
            sList = user.split(",")
            
            #list of ids converted to int
            sList = list(map(int, sList))

            #filtered dataframe of desiered rows
            f_df = professors[professors.profID.isin(sList)]

            new_df = f_df.merge(classes, on='profID')

            graph = sns.countplot(x = 'Name_x', hue = 'grade', data = new_df)
            graph.set(xlabel='Professor Name', ylabel = "Grades")
            graph.figure.savefig("graph.png")
            cont = False

        else:
            print("Error, wrong input")
    print("\n\nThe graph has been saved to a PNG in the directory you ran the file in\nIf you do not see one of the IDs you asked for in the graph, it may be because the classes table does not have a row with that Student ID")

def class_graph(classes):
    """
    class graph, produces graph of performances per graph
    """
    graph = sns.countplot(x = 'Name', hue = 'grade', data = classes)
    graph.figure.savefig("graph.png")
    print("The graph has been saved to a PNG in the directory you ran the file in")










def menu(args):
    """
    Main menu for view/edit mode, user chooses which tool they wan to use
    """
    students = pd.read_csv(args[0])
    degrees = pd.read_csv(args[2])
    professors = pd.read_csv(args[1])
    classes = pd.read_csv(args[3])

    
    cont = True
    while cont == True:
        user = input("You are in Edit/View Mode.\nPlease enter the number for which option you want:\n1. Edit\n2. View\n3. Visualization\n\n Type 'exit' or 'e' to exit: ")
        if user == 'exit' or user == 'e':
            cont = False
        elif int(user) == 1:
            edit(students, degrees, professors, classes, args)
        elif int(user) == 2:
            view(students, degrees, professors, classes)
        elif int(user) == 3:
            visual(students, degrees, professors, classes)
            return
        else:
            if type(user) is not int():
                print("Your input is not a number")
            else:
                print("Invalid input, please try again")

def visual(students, degrees, professors, classes):
    """
    visualization menu, user chooses which table they want to visualize, degrees does not have visualization
    """

    sList = student_obj(students)
    pList = prof_obj(professors)
    dList = degree_obj(degrees)
    cList = class_obj(classes)


    cont = True
    while cont == True:
        user = input("\nYou are in visualization mode\n1. Graph of Student's performance\n2.Graph of Professor's grades of their students\n3. Graph of average grade per class\nType 'exit' or 'e' to exit\n\nWhich graph would you like to view\n\n")
        if user == 'exit' or user == 'e':
            cont = False
        elif int(user) == 1:
            student_graph(students, classes)
            cont = False
        elif int(user) == 2:
            prof_graph(professors, classes)
            cont = False
        elif int(user) == 3:
            cList = class_graph(classes)
            cont = False
        else:
            print("Error, wrong input")







def edit(students, degrees, professors, classes, args):
    """
    Edit menu, user chooses which table they want to edit through numbers
    """

    sList = student_obj(students)
    pList = prof_obj(professors)
    dList = degree_obj(degrees)
    cList = class_obj(classes)

    cont = True
    while cont == True:
        user = input("\n\n1. Students\n2. Professors\n3. Degrees\n4. Classes\nType 'e' or 'exit' to exit out of edit mode and return to menu\n\nWhich table would you like to edit?: ")
        if user == 'exit' or user == 'e':
            cont = False
        elif int(user) == 1:
            sList = edit_students(sList, students)
        elif int(user) == 2:
            pList = edit_prof(pList, professors)
        elif int(user) == 3:
            dList = edit_degree(dList, degrees)
        elif int(user) == 4:
            cList = edit_classes(cList, classes)
        else:
            print("Error, wrong input")
    
    #at the end of edit function, all changes get sent to eoe()
    eoe(sList, pList, dList, cList, args)
    return

def view(students, degrees, professors, classes):
    """
    View menu, user chooses which table they want to view through numbers
    """
    
    cont = True
    while cont == True:
        user = input("\n\n1. Students\n2. Professors\n3. Degrees\n4. Classes\nType 'e' or 'exit' to exit out of edit mode and return to menu\n\nWhich table would you like to view?: ")
        if user == 'exit' or user == 'e':
            cont == False
        elif int(user) == 1:
            num = students.size
            print(students.head(num))
        elif int(user) == 2:
            num = professors.size
            print(professors.head(num))
        elif int(user) == 3:
            num = degrees.size
            print(degrees.head(num))
        elif int(user) == 4:
            num = classes.size
            print(classes.head(num))
        else:
            print("Error, invalid input")
        user = input("Would you like to view another table? (yes for another table, anything else for no): ")
        if user != 'yes':
            cont = False
    




    


