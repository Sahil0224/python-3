
# Defining a function to find the total number of gym visits
def find_total_visits():
    # Initialize a variable to store the total visits
    totalVisits = 0
    # Looping through the names of the CSV files
    for fileName in ["C:\\Users\\f96s96x\\tedprojects\\Python\python-3\\files\\week-1.csv", "C:\\Users\\f96s96x\\tedprojects\\Python\python-3\\files\\week-2.csv", "C:\\Users\\f96s96x\\tedprojects\\Python\python-3\\files\\week-3.csv"]:
        # Opening the file in read mode
        with open(fileName, "r") as file:
            # Skiping the header line
            next(file)
            # Looping through each line in the file
            for line in file:
                # Spliting the line by comma
                name, *visits = line.split(",")
                # Striping any whitespace
                name = name.strip()
                visits = [v.strip() for v in visits]
                # Converting the number of visits to integers
                visits = [int(v) for v in visits]
                # Sum up the visits for the current member
                membersVisits = sum(visits)
                # Add the member visits to the total visits
                totalVisits += membersVisits
    # Return the total visits
    return totalVisits


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()