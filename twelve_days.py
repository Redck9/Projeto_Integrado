lyrics = ["a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ","four Calling Birds, ","five Gold Rings, ","six Geese-a-Laying, ","seven Swans-a-Swimming, ","eight Maids-a-Milking, ","nine Ladies Dancing, ","ten Lords-a-Leaping, ", "eleven Pipers Piping, ","twelve Drummers Drumming, "]
time = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

stringfrst = "On the"
stringscnd = "day of Christmas my true love gave to me: "
stringFinal= ""

stringFinal = stringfrst + " " + time[0] + " " + stringscnd

for i in range(1,13):
    valor = 50 + len(time[i-1])
    stringFinal = stringFinal[:valor] + lyrics [i-1] + stringFinal[valor:]
    print(stringFinal)
    if(i < 12):
        stringFinal = stringFinal.replace(time[i-1], time[i])
    else:
        break





























'''lyrics = ["a Partridge in a Pear Tree.", "two Turtle Doves", "three French Hens","four Calling Birds","five Gold Rings","six Geese-a-Laying","seven Swans-a-Swimming","eight Maids-a-Milking","nine Ladies Dancing","ten Lords-a-Leaping", "eleven Pipers Piping","twelve Drummers Drumming"]


time = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

i=0

lista = []
def fatoriar(num1):
    lista.append(num1)
    if num1 == 13:
        return
    s1 = "On the "
    s2 = " day of Christmas my true love gave to me:"
    for i in lista:
        if(i==1):
            s1 = s1 + time[i-1] + s2 + ' ' + lyrics[i-1]
        else:
            valor = 50 + len(time[num1-2])
            print(time[i-1])
            #s1 = s1 + ', ' + lyrics[i-1]
            s1 = s1[:valor] + lyrics[i-1] + ', ' + s1[valor:]
            s1 = s1.replace(time[i-2], time[i-1])

    print(s1)
    fatoriar(num1+1)
    i = i +1

fatoriar(i)

for x in lyrics:
    print(x)

elif(i==12):
            valor = 49 + len(time[i-1])
            #s1 = s1 + ', ' + lyrics[i-1]+ '.'
            s1 = s1[:valor] + lyrics [i-1] + s1[valor:]
            s1 = s1.replace(time[i-2], time[i-1])'''