def euler20():
    
    counter = 1
    for i in range(2, 101):
        counter *= i
    counter = sum(map(int,str(counter)))
    print("Result: " + str(counter))

euler20()
