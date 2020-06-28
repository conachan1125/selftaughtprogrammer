import csv

list = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on File", "Flight"]
    ]

with open("movie.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for item in list:
        w.writerow(item)
