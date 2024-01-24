#
# Fall 2024, CS 5001
# Lab 2 code file
# Practicing good code style and more complex functions

def main():
    #User Input date by day, month, year and convert to int
    day = int(input("Enter day:"))
    month = int(input("Enter month:"))
    year = int(input("Enter year:"))

    #Determine season by if/elif statements and store value as "season"
    if month == 12 or month == 1 or month == 2:
        season = "Winter"
    elif month > 2 and month < 6:
        season = "Spring"
    elif month > 5 and month < 9:
        season = "Summer"
    else:
        season = "Fall"
    
    #Print season to user
    print("Season:", season)

if __name__ == "__main__":
    main()