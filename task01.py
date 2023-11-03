#!python3
# Create a user interface to have the user enter in data for a teacher
# Use the menu options below to help navigate your program:
# User input has been encloded by _ _
"""
1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 1_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 0

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _0_
Enter in the scores for 10 students for Assignment 1:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_
Complete.

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 2_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 1

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _1_

Enter in the scores for 10 students for Assignment 2:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_

"""

import json
#Things to do:
"""
1. make way to input assignment
    It will create its own ID
    
"""
class roomy():
    biglis = {}

    def adding(self):
        name = input("Enter assignment name: ").strip()
        val = str(input("Enter assignment value: ").strip())
        print(f"Assignment created with ID{self.tally+1}")   
        file = {"assignmentID" : self.tally+1,"assignmentName" : name,"assignmentValue" : val,}
        for i in range(1,11):file[str(i)] = 0
        return(file)
    def appending(self):
        ask = input("Enter assignment ID: ").strip()
        data = (open("data.csv","r").read()).split("\n")
        for i in range(len(data)):
                if data[i] == "":
                    data.pop(i)
        num = 1
        for i in (data):
            self.biglis[num] = json.loads(i)
            num+=1
        open("data.csv","w").write("")
        ndata = open("data.csv","a")
        forbiden = ["assignmentID","assignmentName","assignmentValue"]
        for i in self.biglis:
            
            if i == int(ask):
                
                for j in self.biglis[i]:
                     
                    if j in forbiden:
                        continue
                    else:

                        updat = input(f"Student {j}: ")
                        self.biglis[i][j] = int(updat)
        for i in self.biglis: ndata.write(json.dumps(self.biglis[i])+"\n")
        



                
        
    def viewing(self):
        data = (open("data.csv","r").read()).split("\n")
        for i in range(len(data)):
            if data[i] == "":
                data.pop(i)
        for i in (data):
            print(i)
        print("\n\n")
        return None

    def __init__(self):
        
        while True:
            data = (open("data.csv","r").read()).split("\n")
            for i in range(len(data)):
                if data[i] == "":
                    data.pop(i)
            tally = len(data)
            self.tally = tally
            
            
            action = input("What would you like to do?\n1. Create an Assignment\n2. Enter in Assignment Scores\n3. View Scores\n4. Delete All\n--> ").strip()
            if action == "1":
                file = self.adding()
                data = open("data.csv","a")
                data.write(json.dumps(file)+"\n")
                data = open("data.csv","r")
                data.close()
                print("\n")
            elif action == "2":
                self.appending()
            elif action == '3':
                self.viewing()
            elif action == '4':
                data = open("data.csv","w").write("")
                self.tally = 0
        

roomy()
