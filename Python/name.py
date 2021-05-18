name = input("Username: ")
pas = input("Password: ")
de = input("Designation: ")
org = input("Organisation: ")
if name == "shiba_tatsuya":
    if pas == "yotsuba":
        if de == "SL":
            if org == "FLT":
                print("Hello Shiba Tatsuya")

elif de == "CM":
    if org == "STARS":
        print("Hello Angie Sirius")

elif de == "SL":
    if org == "SIRIUS":
        print("Hello Shiba Miyuku")

elif de == "FG":
    if org == "SCFB":
        print("Hello Sudeeksha Yellanki")

else:
    print("Welcome "+name)
