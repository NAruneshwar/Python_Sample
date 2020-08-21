def toGoatLatin(S):
    result = str()
    i = 0
    for s in S.split():
        i+=1
        if(s[0] in ['a','e','i','o','u','A','E','I','O','U']):
            s+='ma'
        elif(s[0]==' '):
            pass
        else:
            s+=s[0]
            s= s[1:]
            s+='ma'
        
        s+='a'*i
        result+=s+' '

    return result[:-1]



print(toGoatLatin('I speak Goat Latin'))