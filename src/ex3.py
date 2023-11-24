
# Define a function to count words and create two files larger-words and small-words
def create_files(fileName):
    # Creating a set to store the unique words
    uniqueWords = set()

    # Creating two list largeWords to store large words and smallWords to store small words
    largeWords = []
    smallWords = []

    #Opening the input file in read mode
    with open(fileName, "r") as file:
        # Loop through each line in the file
        for line in file:
            # Split the line by whitespace
            words = line.split()
            #Loop through each words in the line
            for word in words:
                # Adding the word to the set
                uniqueWords.add(word)
                # Checking if the length of the word is less than 3
                if len(word) < 3:
                    # If it is less than 3 then add it to the smallWords list
                    smallWords.append(word)
                else:
                    # If it is greater than 3 then add it to the largeWords list
                    largeWords.append(word)
    
    # Opening the large word file in write mode
    with open("C:\\Users\\f96s96x\\tedprojects\\Python\python-3\\files\\large-words.txt", "w") as file:
        # Writing the large words one per line to the file 
        for word in largeWords:
            file.write(word + "\n")

    # Opening the small words file in write mode
    with open("C:\\Users\\f96s96x\\tedprojects\\Python\python-3\\files\\small-words.txt", "w") as file:
        # Writing the small words oner per line to the file
        for word in smallWords:
            file.write(word + "\n")
    
    # return the size of the uniqueWords set
    return len(uniqueWords)



def ex3():
    total_words = create_files("C:\\Users\\f96s96x\\tedprojects\\Python\python-3\\files\\words.txt")
    print(f"Total words: {total_words}.")

ex3()