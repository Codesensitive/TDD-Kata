
def Add(a,b):
    #Negative number list
    arrpos = []
    adder=0
    #Returns Sum and list of negative numbers
    def search(lst):
        retSum=0
        for item in lst:
            retSum+= int(item)
            if int(item) < 0:
                    arrpos.append(item)
        return retSum

    if a.startswith("//"):
        sign = a[2]
        li = a[5:].split(sign)
        adder+=search(li)
    elif a.__contains__('\n'):
        li=a.split('\n')
        adder+=search(li)
    elif a.__contains__(';'):
        li=a.split(';')
        adder+=search(li)

    else:
        if int(a)<0:
            arrpos.append(a)

        adder+=int(a)
    if b.startswith("//"):
        sign1 = a[2]
        li2 = a[5:].split(sign1)
        adder+=search(li2)
    elif b.__contains__('\n'):
        li2 = b.split('\n')
        adder+=search(li2)
    elif b.__contains__(';'):
        li2=b.split(';')
        adder+=search(li2)
    else:
        if int(b)<0:
            arrpos.append(b)
        adder+=int(b)

    if len(arrpos) == 1:
        raise Exception("negatives not allowed")
    elif len(arrpos) > 1:
        raise Exception(",".join(arrpos))

    return adder



