students = {
    '1001': {'name': 'Mathew', 'marks': [85, 90, 95]},
    '1002': {'name': 'Jade', 'marks': [90, 92, 94]},
    '1003': {'name': 'Charlie', 'marks': [75, 80, 85]},
    '1004': {'name': 'Kabir', 'marks': [80, 85, 90]}, 
    '1005': {'name': 'Elena', 'marks': [95, 90, 85]}
}
for key in students:
    total_marks = sum(students[key]['marks'])
    students[key]['total_marks'] = total_marks

for key in students:
    print('Roll No: ' + key)
    print('Name: ' + students[key]['name'])
    print('Marks: ' + str(students[key]['marks']))
    print('Total Marks: ' + str(students[key]['total_marks']))
    print('')

highest_total_marks = 0
for key in students:
    if students[key]['total_marks'] > highest_total_marks:
        highest_total_marks = students[key]['total_marks']
        highest_scoring_student = students[key]['name']

print('Student with highest total marks:')
print('Name: ' + highest_scoring_student)
print('Total Marks: ' + str(highest_total_marks))
