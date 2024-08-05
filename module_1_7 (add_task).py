grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list (students)
students = students_list
print(students, type(students))
print(students_list)
students_sort = sorted(students_list) # - сортировка
print(students_sort)
grades_0 = grades[0]
grades_1 = grades[1]
grades_2 = grades[2]
grades_3 = grades[3]
grades_4 = grades[4]
grades_0_av = sum(grades_0) / len(grades_0)
grades_1_av = sum(grades_1) / len(grades_1)
grades_2_av = sum(grades_2) / len(grades_2)
grades_3_av = sum(grades_3) / len(grades_3)
grades_4_av = sum(grades_4) / len(grades_4)
grades_av = {round(grades_0_av,1), round(grades_1_av,1), round(grades_2_av,1), round(grades_3_av,1), round(grades_4_av,1)}
print(grades_av)
students = students_sort
print(students, type(students))
students_grade = dict (zip(students,grades_av)) # zip от слова zipper (застёжка-молния) -- сшивает половинки
print(students_grade)