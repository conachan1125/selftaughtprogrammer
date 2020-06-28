an = input("What do you like?")
with open("answer.txt", "w", encoding="UTF-8") as f:
    f.write(an)
    print(f)
