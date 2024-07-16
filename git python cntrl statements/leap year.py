#Write a Python program that determines if a given year is a leap year or not.
year=int(input("Enter the year:"))
if year %4 ==0:
    print("leap year")
else:
    print("not a leap year")