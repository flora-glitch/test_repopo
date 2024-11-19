def a():
    displacment=float(input("input displacment:"))
    time=float(input("input time:"))
    velocity=str(displacment*time)
    print(velocity + "m/s")

def b():
        force = float(input("input force:"))
        area = float(input("input area:"))
        pressure = str(force/area)
        print(pressure + "pa")


def c():
    force = float(input("input force:"))
    distance = float(input("input distance:"))
    work = str(force * distance)
    print(work)


def d():
    voltage = float(input("input voltage:"))
    resistance = float(input("input resistance:"))
    current = str(voltage/resistance)
    print(current)


def e():
    force = float(input("input force:"))
    length = float(input("input length"))
    surfacetension= str(force * length)
    print(surfacetension)


def main():
    user_choice=input("choose from a-e:")
    if user_choice == 'a':
        a()
    elif user_choice == 'b':
        b()
    elif user_choice == 'c':
        c()
    elif user_choice == 'd':
        d()
    elif user_choice == 'e':
        e()
if __name__ == '__main__':
    main()