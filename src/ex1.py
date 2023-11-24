from ValidationException import ValidationException


# Define a function to validate a file
def validate_file(fileName):
    # Open the file in read mode
    with open(fileName, "r") as file:
        # Skip the header line
        next(file)
        # Loop through each line in the file
        for line in file:
            # Split the line by comma
            car, mileage = line.split(",")
            # Strip any whitespace
            car = car.strip()
            mileage = mileage.strip()
            # Try to convert the mileage to an integer
            try:
                mileage = int(mileage)
            # If it fails, raise a validation exception with the car name and the invalid mileage
            except ValueError:
                raise ValidationException(f"Invalid mileage for {car}: {mileage}")
            # If it succeeds, check if the mileage is positive
            if mileage < 0:
                # If not, raise a validation exception with the car name and the negative mileage
                raise ValidationException(f"Negative mileage for {car}: {mileage}")
    # If no exception is raised, return True
    return True

def ex1():
    try:
        validate_file("C:\\Users\\f96s96x\\tedprojects\\Python\python-3\\files\\input.txt")
    except ValidationException as ve:
        print(ve)

ex1()