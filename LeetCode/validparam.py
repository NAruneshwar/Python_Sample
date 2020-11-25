def isValid(s):
    result = []
    matchs = {'(':')','[':']','{':'}'}
    for k in s:
        if k in ('(','[','{'):
            result.append(k)
        elif k in (')',']','}'):
            if len(result)==0:
                return False
            if k == matchs[result[-1]]:
                result.pop()
            else:
                return False
    if len(result) == 0:
        return True
    else:
        return False
                
isValid('()')
                