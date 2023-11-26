def anagramma(x:str, y:str):
    a = [0]*26
    b = [0]*26
    for elem in x:
        a[ord(elem)-ord('a')]+=1
    for elem in y:
        b[ord(elem)-ord('a')]+=1
    
    for i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True