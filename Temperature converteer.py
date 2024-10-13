print("Temperature converter")
while True:
    print("1.Fahrenheit to Celcius\n2.Celcius to Fahrenheit\n3.Exit")
    ask=input("Enter the choice(1-3): ")
    if ask=='1':
        temp=int(input("Enter the temperature in Fahrenheit"))
         #convert using eqn and print
        c=(temp-32)*5/9
        print(c," F")

    elif ask=="2":
        temp=int(input("Enter the temperature in Celcius"))
        #convert using eqn and print
        f=temp*5/9+32
        print(f," C")

    
    elif ask=="3":
        print("Exiting")
        break

    else:
        print("invalid choice")
        continue
    

