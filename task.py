from random import randrange

def task_1(): # Lottery ticket generator

    ticket = []

    # Code here
    for i in range(6):
        ticket.append(randrange(1, 49))
    
    return ticket

def task_2(): # Countdown

    output = []

    # Code here
    number = int(input("Enter a number below 100: "))
    for i in (reversed(range(1, 101))):
        output.append(i)
        if (i == number):
            break;

    return output

def task_3():
    people_cars = {
        "Adam": "Volvo",
        "Kate": "BMW",
        "Mark": "BMW",
        "Hannah": "Ford",
        "Max": "Volvo",
        "Celine": "Fiat"
    }

    car_make_lengths = set()

    for car_make in people_cars.values():
        car_make_lengths.add(len(car_make))
    
    #return f"There will be {len(car_make_lengths)} different sizes of key rings."
    return car_make_lengths

print(len(task_3()))