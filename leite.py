a = int(input())#minimo de leite
b = int(input())#máximo de leite
c = int(input())#capacidade da xicara em ml
d = int(input())#ml de café preparado pela máquina
volume = c - d
if volume > a and volume < b:
    print("S")
elif volume > a and volume < b:
    print("S") 
elif volume == a or volume == b:
    print("S")
else:
    print("N")