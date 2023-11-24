from pprint import pprint

# A function to build a list of cars from two list
def build_car_list():
    # a list to store the cars
    carList = []

    # a dictionary to store the car ids and models
    carIds = {}

    # open the car-ids file in read mode
    with open("C:\\Users\\f96s96x\\tedprojects\\Python\python-3\\files\\car-ids.txt", "r") as file:
        # Loop through each line in the file
        for line in file:
            # split the line in comma
            carId, carModel = line.split(",")
            # strip any white spaces
            carId = carId.strip()
            carModel = carModel.strip()
            # Add the car id and car model to the dictionary
            carIds[carId] = carModel
    # Open the input file in read mode
    with open("C:\\Users\\f96s96x\\tedprojects\\Python\python-3\\files\\input.txt", "r") as file:
        # loop through each line in the file
        for line in file:
            # split line in comma
            carId, carMiles = line.split(",")
            # strip any white spaces
            carId = carId.strip()
            carMiles = carMiles.strip()
        # Try to convert the car miles to an integer
            try:
                carMiles = int(carMiles)
            # If it fails, skip the line
            except ValueError:
                continue
            # Check if the car id is in the dictionary
            if carId in carIds:
                # Get the car model from the dictionary
                carModel = carIds[carId]
                # Check if the car miles are reasonable
                if carMiles < 1000000:
                    # Create a dictionary to store the car details
                    car = {"id": carId, "miles": carMiles, "model": carModel}
                    # Append the car to the list
                    carList.append(car)
    # Return the car list
    return carList

def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
