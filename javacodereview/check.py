import  re
def checkV(v):
    x = re.search(r'switch\s\d{1,5}', v)
    if x:
        y = re.search(r'default', v)
        if y:
            return "you're good"
        else:
            return "code doesn't have default"
    z = re.search()



    return "There is no match"