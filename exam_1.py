grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list_sort = sorted(students_list)
#print(students_list_sort)
def function(a):
    return sum(a)/len(a)
x = map(function, grades)
average_score = list(x)
#print(average_score)
grade_book = dict(zip(students_list_sort, average_score))
print(grade_book)
