def my_split(text):
    lst = []
    for i in range(0, len(text)):
        if text[i] == " ":
            lst.append(text[0:i])


    return


print(my_split("as  da dada dad ad"))
