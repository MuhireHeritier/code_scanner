import  re
def checkV(v):
    x = re.search(r'switch', v)
    if x:
        y = re.search(r'default', v)
        if y:
            return "you're good"
        else:
            return "code doesn't have default"

    z = re.search(r'throws', v)
    if z:
        result = re.search(r'catch', v)
        if result:
            return "You're good!"
        else:
            return "An exception is thrown from a function, but it is not caught."

    tr = re.search(r'Thread',v)
    if tr:
        rs = re.search(r'start', v)
        if rs:
            return "You're good. Good to use start instead of run. "
        else:
            return "Check well, you migth have used run instead of start"

    cl = re.search(r'public', v)
    if cl:
        fl = re.search(r'final', v)
        if fl:
            return "Your code has critical public variable that is final "
        else:
            return "Your code has public variable which is not final, prompts to allow your code to be modified to contain unexpected values"
    return "There is no matching errors"