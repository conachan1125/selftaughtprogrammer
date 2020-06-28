list1 = ["ウォーキングデッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイアダイアリーズ"]
for name in list1:
    print(name)

for i in range(25, 51):
    print(i)

for i, name in enumerate(list1):
    print(i,name)

numbers = [11, 32, 33, 15, 1]
while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")

list2 = [8, 19, 148, 4]
list3 = [9, 1, 33, 83]
n_list = []
for i in list2:
    for j in list3:
        n_list.append(i * j)

print(n_list)
