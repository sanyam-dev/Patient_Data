from os import WEXITED
global std_list
std_list = []

def addStudent():
    print("Adding Student...\n")
    STUDENT = []
    name = input("Enter Name: ")
    STUDENT.append(name)
    roll = input("Enter Roll Number: ")
    STUDENT.append(roll)
    adm_no = input("Enter Admission Number: ")
    STUDENT.append(adm_no)
    clas  = input("Enter Class: ")
    STUDENT.append(clas)
    sci = int(input("Marks in Science: "))
    STUDENT.append(sci)
    maths = int(input("Marks in Maths :"))
    STUDENT.append(maths)
    ss  =int(input("Marks in SS: "))
    STUDENT.append(ss)
    en =int(input("Marks in English: "))
    STUDENT.append(en)
    std_list.append(STUDENT)
    print("{} is added to the database".format(std_list[len(std_list)-1][0]))
    mainMenu()

def Updatedetail():
    print("Updating Score...\n")
    mainMenu()
    pass
def displayMarks(roll_no):
    for i in range(len(std_list)):
        if roll_no == std_list[i][1]:
            print(": SCIENCE : MATHS : SOCIAL SCIENCE : ENGLISH :")
            print(":" + " " + "{}" + (" ")*(8-len(str(std_list[i][4])))+":" + " " + "{}" + (" ")*(6-len(str(std_list[i][5])))+":" + " " + "{}" + (
                " ")*(15-len(str(std_list[i][6])))+":" + " " + "{}" + (" ")*(8-len(str(std_list[i][7])))+":".format(std_list[i][4], std_list[i][5], std_list[i][6], std_list[i][7]))
        else:
            print("Enter Valid Roll Number")       
    mainMenu()
    pass
def ComputeRank():

    print("Computing Ranks...\n")
    mainMenu()

def MeritList():
    print("Fetching Merit list...\n")
    mainMenu()
    pass

def mainMenu():
    print("\n")
    print("1. Add Student Data")
    print("2. Update Score Sheet")
    print("3. Display Mark Sheet")
    print("4. Compute Rank")
    print("5. Merit list")
    print("6. Quit")

    try :
        option = int(input("Enter Choice: "))
        if option == 1:
            addStudent()
        elif option == 2:
            UpdateScore()
        elif option == 3:
            roll = input("Enter Roll Number: ")
            displayMarks(roll)
        elif option == 4:
            ComputeRank()
        elif option == 5:
            MeritList()
        elif option == 6:
            quit()
        else:
            print("!!!!!------- Enter Value in 1-6 -------!!!!!")
            mainMenu()
    except ValueError:
        print("Enter Values between 1-6")
    

    
mainMenu()
