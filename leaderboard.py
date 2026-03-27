import csv #Library for handling CSV files

def saveScore(name, balance): #Function to save the name and balance of the final score
    with open("leaderboard.csv", "a") as file: #Here we append new data to the CSV file using the a
        writer = csv.DictWriter(file, fieldnames=["name", "balance"]) #Appending new data to the CSV file
        writer.writerow({"name": name, "balance": balance}) #Writing the name and balance to the CSV file 

def showTopScores(): #Function that shows the scores
    print("===LEADERBOARD===")
    try:
        with open("leaderboard.csv", "r") as file: #Reading the CSV file
            reader = csv.DictReader(file)
            for row in reader:
                print(f"{row['name']}: {row['balance']}") #Prints the name and balance for the scores
    except FileNotFoundError: #If there are no scores that have been saved yet
        print("No scores.")

showTopScores()