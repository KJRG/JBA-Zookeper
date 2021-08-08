# put your python code here
students_in_class_1 = int(input())
students_in_class_2 = int(input())
students_in_class_3 = int(input())

desks_in_class_1 =\
    (students_in_class_1 // 2)\
    + (students_in_class_1 % 2)

desks_in_class_2 =\
    (students_in_class_2 // 2)\
    + (students_in_class_2 % 2)

desks_in_class_3 =\
    (students_in_class_3 // 2)\
    + (students_in_class_3 % 2)

min_number_of_desks =\
    desks_in_class_1\
    + desks_in_class_2\
    + desks_in_class_3

print(min_number_of_desks)
