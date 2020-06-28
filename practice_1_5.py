favorite_musician = ["宮野真守", "水瀬いのり", "平井堅"]
print(favorite_musician)

travel_destination = [(34.987528, 135.759323), (43.06417,141.34694)]
print(travel_destination)

my_dict = {"height" : "167.0", "weight" : "57.5", "favorite_color" : "blue"}
print(my_dict)

key = input("好きなキーを入力してください")
if key in my_dict:
    print(my_dict[key])
else:
    print("残念")

set_list = {"宮野真守": ["Break it", "exciting"], "水瀬いのり" : ["starry wish", "ココロソマリ"], "平井堅" : ["Popstar", "瞳を閉じれば"]}
print(set_list)
