# anagrams
test1= ["earth", "heart","tearh"]
test2=["earth", "hear", "ear"]

def checkAnagram(test):
    flag = True
    test_result = set(list(test[0]))
    for item in test:
        sett = set(list(item))
        if sett != test_result:
            return False
    return flag

for test in test1, test2:
    print(f"For {test}, {checkAnagram(test)}")
