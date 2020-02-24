last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ['physics', 'calculus', 'poetry','history']

grades = [98, 97, 85, 88]

gradebook = zip(subjects, grades)

gradebook = list(gradebook)

print(gradebook)

gradebook.extend([('computer science', 100), ('visual arts', 98)])

print(gradebook)

'''
Otherwise we can extend in the initial 
lists and then zip the total list:

subjects.extend(['computer science', 'visual arts'])

grades.extend([100,98])

gradebook = list(zip(subjects, grades))

print(gradebook)
'''

full_gradebook = gradebook +last_semester_gradebook

print(full_gradebook)




