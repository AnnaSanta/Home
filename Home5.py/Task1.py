# 1 Напишите программу, удаляющую из файла все слова, 
# содержащие "абв"

with open('Task.txt', 'a', encoding='utf-8') as f:
    print('привет абв пока абвг\n', file=f)

with open('Task.txt', 'w', encoding='utf-8') as f:  
     p = ' '.join(list(filter(lambda x: not 'абв' in x, f.split())))
     print(p)


# with open('Task.txt', 'r', encoding='utf-8') as f:
#    print(f.read())

# with open('Task.txt', 'r', encoding='utf-8') as f:
#     data = f.readlines() 