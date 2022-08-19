# anagrams
test1= ["earth", "heart","tearh"]
test2=["earth", "hear", "ear"]

lst= []

flag = True
for test in test1, test2:
    print(f"For {test}")
    test_result = set(list(test[0]))
    for item in test:
        sett = set(list(item))
        if sett != test_result:
            flag = False
            break

    print(flag,"\n")


