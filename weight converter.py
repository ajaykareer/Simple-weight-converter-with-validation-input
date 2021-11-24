print("Simple Weight Converter from Lbs to Kgs or vice-versa")
print("By Ajay Kareer")

def main():
    while True:
        first_name = input("Enter your name: ")
        if not first_name.isalpha():
            print ("Enter your name in ALPHABETS unless you are Elon Musk.. :D")
            continue
        else:
            break
    while True:
        last_name = input("Enter your last name: ")
        if not last_name.isalpha():
            print("Enter your last name in Alphabets only")
            continue
        else:
            break
    print("Hi,", first_name.capitalize() + " "+ last_name.capitalize()+"!!")
    print("Press \"1\" to convert Lbs to Kg")
    print("Press \"2\" to convert Kgs to Lbs")
    value = (input())
    while value != "1" and value != "2":
        print("Enter valid input..")
        value = input("Choose option 1 or 2: ")
    if value == "1":
        while True:
            try:
                lbs_input = float(input("Enter your weight in Lbs: "))
            except ValueError:
                print("Enter correct weight.. :D")
                continue
            else:
                break
        kgs_result = round(lbs_input * 0.454,2)
        print("Your weight in Kgs is",str(kgs_result) + " Kg.")
        print("Wanna check again ??")
        app = input("Press \"y\" to run the script again or \"q\" to quit: ").lower()
        while app != "y" and app != "Y" and app != "q" and app!= "Q":
            print("Enter Valid Input (y or q)")
            app = input("Press \"y\" to run the script again or \"q\" to quit: ").lower()
        if app == "y":
            main()
        elif app == "q":
            print("Okay bye.. :)")
            exit()
    elif value == "2":
        while True:
            try:
                kgs_input = float(input("Enter your weight in Kgs: "))
            except ValueError:
                print("Enter correct weight.. :D")
                continue
            else:
                break
        lbs_result = round(kgs_input* 2.20462,2)
        print("Your weight in Lbs is", str(lbs_result) + " Lbs.")
        app = input("Press \"y\" to run the script again or \"q\" to quit: ").lower()
        while app != "y" and app != "Y" and app != "q" and app != "Q":
            print("Enter Valid Input (y or q)")
            app = input("Press \"y\" to run the script again or \"q\" to quit: ").lower()
        if app == "y":
            main()
        elif app == "q":
            print("Okay bye.. :)")
            exit()
main()