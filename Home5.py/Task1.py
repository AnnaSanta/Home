# 1 Напишите программу, удаляющую из файла все слова, 
# содержащие "абв"

with open('Task1.txt', 'a', encoding='utf-8') as f:
    print('привет абв пока абвг\n', file=f)    

with open('Task1.txt', 'r', encoding='utf-8') as f:
    print(f.read())  

with open('Task1.txt', 'w+', encoding='utf-8') as f:  
    temp = f.read()  
    z = [i for i in temp.split()]
    p = ' '.join(list(filter(lambda x: not 'абв' in x, z)))
    print(p)
