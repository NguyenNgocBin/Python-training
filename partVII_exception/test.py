



try:
    line = open("ad.txt", "r") 
    for x in line:
            a = x.strip()
            try:
                number = int(a)
                print(number)
            except ValueError:
                print("Error")
    line.close()
except FileNotFoundError as e:
    print(e)
    