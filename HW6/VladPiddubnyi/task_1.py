task_1 = []
task_2 = []
task_3 = []

for i in range(1,11):
    if i % 2 == 0:
        task_1.append(i)
        
    
    elif i % 2 != 0 and i % 3 == 0:
        task_2.append(i)

    elif i % 2 != 0 and i % 3 != 0:
        task_3.append(i)



print(f'Парні числа: {task_1}')
print(f'Непарні числа, які діляться на 3: {task_2}')
print(f'Числа, які не діляться на 2 і 3: {task_3}')