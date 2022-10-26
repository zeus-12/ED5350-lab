sports = ["cricket","basketball","tennis"]
students = ["vishnu","pranoy","thazeel"]
dct={}

string_of_sports=""
for item in sports:
    string_of_sports += item +", "

for item in students:
    fav_sport = input(f"{item}, enter fav sport among {string_of_sports}")
    dct[item] = fav_sport

print(dct)


