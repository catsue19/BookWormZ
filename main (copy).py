# Submission by Atta Yazdy and Catherine Sue
# for the MLH Hack the Classroom Hackathon!
# Python script created from Sept 1 to Sept 3

import re

# open the file and read the student names
file = open("studentInfo.txt", "r")
fileInfo = []
text = file.readlines()
#print(text)
#delay(1000)

for line in text:
  line = line.strip()
  line = line.split(",")
  fileInfo.append(line)

numItems = len(fileInfo)

print(fileInfo)
#delay(1000)

validLevels = list(range(0, 6+1))
#print(validLevels)

name = input("Please enter your name: ").upper()

keepGoing = True
addStudent = 0
# concatenating through the file to determine whether the student is new or not
for i in range(0, numItems):
  while keepGoing:
    if name in fileInfo[i]:
      print ("You are a student in this class!")
      keepGoing = False
      namePlace = i
    elif name not in fileInfo[i] and i < numItems - 1:
      i +=1
    else:
      print ("You are not a current student in this class.")
      response = input("Type 'Y' to add a new student or any other key to cancel ").upper()
      # adding a student to the file
      if response == "Y":
        newStudent=[]
        newStudent.append(name)
        newStudentLevel = int(input("Please enter the student's current reading level: "))
        
        if newStudentLevel in validLevels:
          newStudent.append(newStudentLevel)
          fileInfo.append(newStudent)
          addStudent = 1
          namePlace = i+1
          keepGoing = False
        else:
          print("Invalid reading level.")
          exit()
          
      else:
        exit()

bookType = input(
      "What kind of book did you read? Please choose from the following options: Type 'P' for Picture Book, 'C' for Chapter Book, or 'A' for Audio Book ").upper()
# collecting information from students
numPagesRead = 0.0
playbackSpeed = 0.0
if bookType == "P" or bookType == "C":
  numPagesRead = float(input("How many pages did you read? "))
elif bookType == "A":
  playbackSpeed = float(input("What speed are you listening to your audiobook at? "))
else:
    print("Book type is invalid.")
    exit()

time = float(input("How many minutes did you read for? "))

grade = int(input("What grade are you in? (Enter 0 if in kindergarten!) "))
# calculating reading level based on words per minute
def calculateLevel(bookType, grade, numPagesRead, playbackSpeed, time):
  
  if bookType == "P" or bookType == "C":
    if bookType == "P":
      wordsPerPage = 20.0
    elif bookType == "C":
      wordsPerPage = 200.0
    
    wordsPerMin = (wordsPerPage * numPagesRead) / time
    
    if wordsPerMin < 53:
      bookLevel = 0  
    elif wordsPerMin >= 53 and wordsPerMin < 89:
      bookLevel = 1
    elif wordsPerMin >= 89 and wordsPerMin < 107:
      bookLevel = 2
    elif wordsPerMin >= 107 and wordsPerMin < 123:
      bookLevel = 3
    elif wordsPerMin >= 123 and wordsPerMin < 139:
      bookLevel = 4
    elif wordsPerMin >= 139 and wordsPerMin < 150:
      bookLevel = 5
    elif wordsPerMin >= 150:
      bookLevel = 6
  # determining reading levels for audiobooks via playback speed  
  elif bookType == "A":
    if playbackSpeed >= 0 and playbackSpeed < 1:
      bookLevel = grade - 1
    elif playbackSpeed == 1:
      bookLevel = grade
    elif playbackSpeed > 1:
      bookLevel = grade + 1
    
  return bookLevel
  
# calling the function 
bookLevel = calculateLevel(bookType, grade, numPagesRead, playbackSpeed, time)

fileInfo[namePlace].append(bookLevel)

# comments for the teacher
if bookLevel < grade:
  print("This student is eligible for testing! It appears that their reading level, Grade", bookLevel, ",is less than their expected reading level, Grade", grade)
elif bookLevel > grade:
  print("This student is eligible for testing! It appears that their reading level, Grade", bookLevel, "is greater than their expected reading level, Grade", grade)
elif bookLevel == grade:
  print("The student's reading level, Grade", bookLevel, "is equal to their expected reading level, Grade", grade)

# write new recommended book level to the file
file = open("studentInfo.txt", "w")
for i in range(0, numItems + addStudent):
  line = str(fileInfo[i])
  line = re.sub(r"[\[\]]", "", line)
  line = re.sub(r"[\']", "", line)
  file.writelines(line +'\n')
  file = open("studentInfo.txt", "a")

file = open("studentInfo.txt", "r")
print(file.read())

file.close()
