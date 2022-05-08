def isValid(self, s): 
    stack = []
    for i in range(0,len(s),1):
        if s[i]=='(' or s[i]=='{' or s[i]=="[":
            stack.append(s[i])
        else:
            if len(stack)==0:
                return False
            else:
                currCharacter = stack.pop()
                if s[i]==')' and currCharacter!='(':
                    return False 
                elif s[i]=="]" and currCharacter!="[":
                    return False
                elif s[i]=='}' and currCharacter!="{":
                    return False
    if len(stack)==0:
        return True
    else:
        return False