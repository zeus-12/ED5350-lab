# loop
def reverse_loop(query,type):
    if type == "sentence":
        return query[::-1]
    elif type == "words":
        words = query.split(" ")
        reverse_words = ""
        for item in words:
            reverse_words += (item[::-1]) + " "
        return reverse_words
    else:
        return

print(reverse_loop("sun is hot","sentence"))
print(reverse_loop("sun is hot","words"))

# recursion
def reverse_recursion(query,type):
    if type == "sentence":
        # length = len(query)
        if len(query) == 1:
            return query[0]
        return  reverse_recursion(query[1:], type)+query[0]
    elif type == "words":
        if " " not in query:
            if query:
                return query[::-1]
            else:
                return

        elif " " in query :
            space_index = query.index(" ")
            # res = query[:space_index:-1]
            return query[:space_index][::-1]+" " +  reverse_recursion(query[space_index+1:],type) 

print(reverse_recursion("sun is hot","sentence"))
print(reverse_recursion("sun is hot","words"))
