author = "カミュ"
print(author[0])
print(author[1])
print(author[2])

para = "私は昨日{}を書いて、{}に送った"
print(para)
answer1 = input("一つ目の空欄を埋めてください：")
answer2 = input("二つ目の空欄を埋めてください：")
ans = para.format(answer1, answer2)
print(ans)


para2 = "aldous Huxley was born in 1894.".capitalize()
print(para2)

list = "どこで？　誰が？　いつ？".split("　")
print(list)

list2 = ["The", "fox", "jumped", "over", "the", "fence", "."]
para3 = " ".join(list2)
para3 = para3[0:-2] + "."
print(para3)

para4 = "A screaming comes across the sky".replace("s", "$")
print(para4)

index = "Hemingway".index("m")
print(index)

para5 = "\"友情\"、\"努力\"、\"勝利\""
print(para5)

para6 = "three " + "three " + "three"
print(para6)

para7 = "three " * 3
para8 = para7.strip()
print(para8)

para9 = "４月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(para9[:10])
