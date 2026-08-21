try:
    name_file = input("Enter name file: ")
    with open(name_file) as file:
        noi_dung = file.read()
    print("noi dung file")
    print(noi_dung)
except FileNotFoundError:
    print("Error: File not ton tai")
finally:
    print("End program")