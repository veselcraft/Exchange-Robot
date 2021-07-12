import w2n

RUdict = {"один":1, "одного":1, "одному":1, "одним":1, "одном":1}

def SpecialSplit(MesTxt):
    MesTxt = MesTxt.replace("\n", ". ") #Replace hyphenation with dot

    while MesTxt.find("  ") != -1: #Removing double spaces
        MesTxt = MesTxt.replace("  ", " ")

    MesTxt = MesTxt.replace(",", ".") #comma to dot

    a = [] #The main array to which the result will be written
    start = 0
    end = 0
    for i in range(len(MesTxt)):
        if MesTxt[i] == " ":
            end = i
            a.append(MesTxt[start:end])
            start = end + 1
        elif i == len(MesTxt) - 1:
            end = len(MesTxt)
            a.append(MesTxt[start:end])
        elif not MesTxt[i].isdigit() and MesTxt[i + 1] == "." or not MesTxt[i].isdigit() and MesTxt[i + 1] == "/": #separating letters from symbols
            end = i + 2
            a.append(MesTxt[start:end])
            start = end + 1
        elif MesTxt[i].isdigit() and not MesTxt[i + 1].isdigit() and MesTxt[i + 1] != " " and MesTxt[i + 1] != ".": #separating a digit from a letter
            end = i + 1
            a.append(MesTxt[start:end])
            start = end
        elif not MesTxt[i].isdigit() and MesTxt[i + 1].isdigit() and MesTxt[i] != " " and MesTxt[i] != ".": #separating a letter from a digit
            end = i + 1
            a.append(MesTxt[start:end])
            start = end

    b = []

    for i in a:
        if i != "":
            b.append(i)

    return b

def TextToDigit(b):
    """ for i in range(len(b)):
        if b[i] in RUdict:
            b[i] = RUdict[b[i]] """
    

    
    i = len(b) - 1
    while i > 0:
        if (b[i] == "к" or b[i] == "k" or "тыс" in b[i] or "тис" in b[i] or "thousand" in b[i]) and b[i - 1][0].isdigit(): #2.5к = 2500
            b[i - 1] = str(float(b[i - 1]) * 1000)
            del b[i]
        elif (b[i] == "кк" or b[i] == "kk") and b[i - 1][0].isdigit(): #2.5кк = 2500000
            b[i - 1] = str(float(b[i - 1]) * 1000000)
            del b[i]
        elif (b[i] == "ккк" or b[i] == "kkk") and b[i - 1][0].isdigit(): #2.5ккк = 2500000000
            b[i - 1] = str(float(b[i - 1]) * 1000000000)
            del b[i]
        i -= 1
    return b
    