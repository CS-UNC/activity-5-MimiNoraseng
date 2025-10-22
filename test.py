# grades = []
# names = ['Max', 'Alex', 'Carey']
# grades.append([10,9,8,7])
# grades.append([9,9,8,7])
# grades.append([10,10,10,2])

# print(grades)
# print(grades[1])
# print(grades[2][2])

# names = ['Max', 'Alex', 'Carey']
# find index for 'Carey'
# x= grades.index('Carey')
#print(grades[x][3])

grades = {}
grades['Max']={'A1':10,'A2':9,'A3':8,'A4':7}
grades['Alex'] =[9,9,8,7]
grades['Carey'] =[10,10,10,2]

print(grades.keys())
for student in grades.keys():
    print(student.grades[student])

#print(grades['Max']['A1'])

#statement = "This is not cool!"
#data = [12.13,14,15,16]
#print(statement)
#print(data)
#print('----------------')
#data.append(35)
#print(data)
#statement = statement + 'modified'
#print(statement)

#statement2 = statement.upper()
#print(statement)
#print(statement2)
#statement3 = statement
#data3 = data 
#data3.append(32)
#print(data3)
# print(data)
# print(statement is statement3)

