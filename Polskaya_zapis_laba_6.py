list = input("Введите выражение: ")
a = list
def toPlska(s):
    lex=parse(s)
    s2=[]
    r=[]
    oper=["+","-","*","/","(",")"]
    for a in lex:
        if a=="(":
            s2=[a]+s2
        elif a in oper:
            if s2==[]:
                s2=[a]
            elif a==")":
                while(True):
                    q=s2[0]
                    s2=s2[1:]
                    if q=="(":
                        break
                    r+=[q]
            elif prty(s2[0]) < prty(a):
                s2=[a]+s2
            else:
                while(True):
                    if s2==[]:
                        break
                    q=s2[0]
                    r+=[q]
                    s2=s2[1:]
                    if prty(q)==prty(a):
                        break
                s2=[a]+s2
        else:
            r+=[a]
    while(s2 != []):
        q=s2[0]
        r+=[q]
        s2=s2[1:]
    return r
 
def prty(o):
    if o=="+" or o=="-":
        return 1
    elif o=="*" or o=="/":
        return 2
    elif o=="(":
        return 0
 
def parse(s):
    delims=["+","-","*","/","(",")"]
    lex=[]
    tmp=""
    for a in s:
        if a != " ":
            if a in delims:
                if tmp != "":
                    lex+=[tmp]
                lex+=[a]
                tmp=""
            else:
                tmp+=a
    if tmp != "":
        lex+=[tmp]
    return lex

print(*toPlska(a))
print(a,"=",eval(list))
