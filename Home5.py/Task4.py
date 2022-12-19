# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия
# и восстановления данных.
# Входные и выходные данные хранятся
#  в отдельных текстовых файлах.
# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff 

def encode(s):

	encoding = "" # выходная строка

	i = 0
	while i < len(s):
		count = 1
		while i + 1 < len(s) and s[i] == s[i + 1]:
			count = count + 1
			i = i + 1

		encoding += str(count) + s[i]
		i = i + 1

	return encoding


if __name__ == '__main__':

	s = 'aaaasssdddwwwwwwwwwwwweeeffffff'
	print(encode(s))

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
           count += char 
        else: 
            decode += char * int(count)
            count = ''
    return decode   
decoded_val = rle_decode('4a3s3d9w3w3e6f') 
print(decoded_val)