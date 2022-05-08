def reverseWords(self, s):
    newStr = ''
    arr = []
    for i in range(0,len(s),1):
        if s[i]==' ':  
            if len(newStr)!=0:
                arr.append(newStr)
                newStr = ''
            continue
        else:
            newStr+=s[i]
    if len(newStr)!=0:
        arr.append(newStr)
    arr.reverse()
    out = ' '.join(arr)
    return out