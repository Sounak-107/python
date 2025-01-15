import time 
def c_to_f (a) :
    # let us concider a is in celcius and b is in farenhiet
    b = ((a * (9/5))+32)
    return b 

def f_to_c(b):
    # let us consider a is in celcius and b is in  farenhiet
    a = ((b - 32) * (5/9))
    return a

def km_to_m(a):
    #let us coincider a is in kilometer and b is in meter
    b = a * 1000
    return b

def m_to_km(b):
    # let us consider a is in meter and b is in kilometer
    a = b / 1000
    return a

def check(a):
    choice = a
    if choice == 1:
        c = float(input("Enter the temperature in Celcius: "))
        f = c_to_f(c)
        print(f"The temperature in Farenhiet is: {f}")
    elif choice == 2:
        f = float(input("Enter the temperature in Farenhiet: "))
        c = f_to_c(f)
        print(f"The temperature in Celcius is: {c}")
    elif choice == 3:
        km = float(input("Enter the length in kilometer: "))
        m = km_to_m(km)
        print(f"The length in meter is: {m}")
    elif choice == 4:
        m = float(input("Enter the length in meter: "))
        km = m_to_km(m)
        print(f"The temperature in Celcius is: {km}")
    elif choice not in range(1,5):
        print("Invalid choice. Please try again.")
        

print("choose what you want to do\n")
time.sleep(1)
a = int(input(" Enter 1 to convert a celcius temperature into farenhiet \n Enter 2 to convert the temperature into celcius \n Enter 3 to convert a length into meter \n Enter 4 to convert a length into km \n"))
check(a)