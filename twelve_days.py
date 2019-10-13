lyrics = ["a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ","four Calling Birds, ","five Gold Rings, ","six Geese-a-Laying, ","seven Swans-a-Swimming, ","eight Maids-a-Milking, ","nine Ladies Dancing, ","ten Lords-a-Leaping, ", "eleven Pipers Piping, ","twelve Drummers Drumming, "]
time = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

stringfrst = "On the"
stringscnd = "day of Christmas my true love gave to me: "
stringFinal= ""

stringFinal = stringfrst + " " + time[0] + " " + stringscnd

for i in range(0,12):
    valor = 50 + len(time[i])
    stringFinal = stringFinal[:valor] + lyrics [i] + stringFinal[valor:]
    print(stringFinal)
    if(i < 11):
        stringFinal = stringFinal.replace(time[i], time[i+1])
    else:
        break

