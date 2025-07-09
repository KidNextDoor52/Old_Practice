from car_ex import Car

def main():

    print("--- My Car Ownership History ---")

    car1 = Car(
        make="Nissan",
        model="Maxima",
        year="2005",
        color="Gold",
        vin=None
    )

    car2 = Car(
        make="Ford",
        model="Escape",
        year="2010",
        color="Silver",
        vin=None
    )

    car3 = Car(
        make="Ford",
        model="Mustang",
        year="2018",
        color="Black",
        vin=None
    )

    my_cars = [car1, car2, car3]

    for i, car in enumerate(my_cars):
        print(f"\nCar #{i+1}")
        print(f" Description: {car.display_info()}")
        print(f" Car age: {car.get_age()}")
        print(f" Repaint: {car.repaint()}")

if __name__ == "__main__":
    main()