import re


def checkV(codes):
    x = re.search(r'switch', codes)
    if x:
        y = re.search(r'default', codes)
        if y:
            return "You're good. Your switch statement has a default. "
        else:
            return "You used switch statement, but you don't have default. The code does not have a default case in a " \
                   "switch statement, which might lead to complex logical errors and resultant weaknesses. So the failure to " \
                   "put default may result into security issues. "

    z = re.search(r'throws', codes)
    if z:
        result = re.search(r'catch', codes)
        if result:
            return "You're alright. You are handling exceptions properly. Just refactor and Happy Coding!"
        else:
            return "An exception is thrown from a function, but it is not caught. "

    tr = re.search(r'Thread', codes)
    if tr:
        rs = re.search(r'start', codes)
        if rs:
            return "You're good. Good to use start instead of run. "
        else:
            return "Check well, you might have used run instead of start. A Thread object's run() method is a bug. " \
                   "Double check, you might have accidentally called run() instead of start(), so the run() method " \
                   "will execute in the caller's thread of control."

    cl = re.search(r'public', codes)
    if cl:
        fl = re.search(r'final', codes)
        if fl:
            return "Your code has critical public variable that is final which allow it to be modified in unexpected " \
                   "ways. "
        else:
            return "Your code has public variable which is not final, prompts to allow your code to be modified to " \
                   "contain unexpected values "
    return "There is no matching errors. Check your codes well, and re-upload!"
