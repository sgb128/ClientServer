"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

s1 = 'разработка'
s2 = 'администрирование'
s3 = 'protocol'
s4 = 'standard'

en_1 = s1.encode(encoding='utf-8')
en_2 = s2.encode(encoding='utf-8')
en_3 = s3.encode(encoding='utf-8')
en_4 = s4.encode(encoding='utf-8')

dec_1 = en_1.decode(encoding='utf-8')
dec_2 = en_2.decode(encoding='utf-8')
dec_3 = en_3.decode(encoding='utf-8')
dec_4 = en_4.decode(encoding='utf-8')

print(f'{"="*50}\n\t{s1=}\n{"-" * 35}\n{en_1=}\n{dec_1=}\n{"*" * 50}')
print(f'{"="*50}\n\t{s2=}\n{"-" * 35}\n{en_2=}\n{dec_2=}\n{"*" * 50}')
print(f'{"="*50}\n\t{s3=}\n{"-" * 35}\n{en_3=}\n{dec_3=}\n{"*" * 50}')
print(f'{"="*50}\n\t{s4=}\n{"-" * 35}\n{en_4=}\n{dec_4=}\n{"*" * 50}')