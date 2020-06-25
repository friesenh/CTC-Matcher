import gspread
from oauth2client.service_account import ServiceAccountCredentials
#from student import student

#basic stuff that needs to happen
scope = ['https://www.googleapis.com/auth/spreadsheets', \
'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name\
('coming2carleton.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('GoogleF').sheet1

data = wks.get_all_records()

#############################################################################

#Counts total number of students who filled out the form
studentcount = 0
for i in data:
    studentcount = studentcount + 1
totalstudents = studentcount

#Counts total number of variables
variablecount = 0
for i in data:
    for j in i:
        variablecount = variablecount + 1
totalvariables = int(variablecount / 2)

#Sorts data by columns
def sortbycolumn():
    #Prints timestamp
    for j in range(totalstudents):
        print(wks.cell(int(j)+1, 1).value)

    #Prints pronouns
    for j in range(totalstudents):
        print(wks.cell(int(j)+1, 2).value)

    #Prints interests
    for j in range(totalstudents):
        print(wks.cell(int(j)+1, 3).value)

    #Prints hometown
    for j in range(totalstudents):
        print(wks.cell(int(j)+1, 4).value)

    #Prints Email
    for j in range(totalstudents):
        print(wks.cell(int(j)+1, 5).value)
#sortbycolumn()

studentlist = []
individualstudents = []
#Sorts data by rows (by students, so more helpful)
"""def sortbyrow(students, variables, studentlist, individualstudents):
    print(type(studentlist))
    for j in range(students):
        for k in range(variables):
            #First value of the coordinate is the rows
            #Second value of the coordinate is the columns
            #Need to add 2 to the rows to make up for starting at 0 and
            #for having a "title row"
            #Need to add 1 to the columns to make up for starting at 0

            individualstudents.append(wks.cell(int(j)+2, k + 1).value)
            print(individualstudents)
    studentlist = list(studentlist.append(individualstudents))
    print(studentlist)
    individualstudents = []"""

#sortbyrow(totalstudents, totalvariables, studentlist, individualstudents)


def basicsortbyrow():
    for j in range(totalstudents):
        print("")
        print("Student #",j+1,":",sep='')
        for k in range(totalvariables):
            #First value of the coordinate is the rows
            #Second value of the coordinate is the columns
            #Need to add 2 to the rows to make up for starting at 0 and
            #for having a "title row"
            #Need to add 1 to the columns to make up for starting at 0

            print(wks.cell(int(j)+2, k + 1).value)
basicsortbyrow()












##
