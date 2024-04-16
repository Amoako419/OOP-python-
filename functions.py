def commentary(color):
    if color == 'red':
        return "it's a tomato"
    elif color == 'green':
        return "it is a green pepper"
    elif color == 'bee purple':
        return "I dont know what it is only bees can see it"
    else:
        return "I've never heard of this " + color + "."
    
comment = commentary('blue')
print (comment)


def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")
        
whatis(0.00000001)