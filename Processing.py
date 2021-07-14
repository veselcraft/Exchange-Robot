from DBH import GetListOfCurrencies

ListOfCur = []
ListEntry = []
ListEqual = []

_eng_chars = u"`qwertyuiop[]asdfghjkl;'zxcvbnm,.QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM,."
_rus_chars = u"ёйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
_ukr_chars = u"'йцукенгшщзхїфівапролджєячсмитьбюЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ"

_spec_symbols = u"~!@#$%^&*()_+-=|/.,?>\<№"

def GetCur(num):
    global ListOfCur
    return ListOfCur[num]

def SpecialSplit(MesTxt):
    MesTxt = MesTxt.replace("\n", ". ") # Replace hyphenation with dot

    while MesTxt.find("  ") != -1: # Removing double spaces
        MesTxt = MesTxt.replace("  ", " ")

    for i in range(len(MesTxt) - 2):
        if MesTxt[i].isdigit() and MesTxt[i + 2].isdigit() and MesTxt[i + 1] == ",":
            MesTxt = MesTxt[0:i + 1] + "." + MesTxt[i + 2:len(MesTxt)] # comma to dot
    print(MesTxt)

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
        #elif not MesTxt[i].isdigit() and MesTxt[i + 1] == "." or not MesTxt[i].isdigit() and MesTxt[i + 1] == "/": #separating letters from symbols
        elif not MesTxt[i].isdigit() and MesTxt[i + 1] in _spec_symbols: #separating letters from symbols
            end = i + 1
            a.append(MesTxt[start:end])
            start = end
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

def LoadCurrencies():
    global ListOfCur
    ListOfCur = GetListOfCurrencies()

def LoadDictionaries():
    global ListEntry
    global ListEqual
    DicEntry = open("Dictionaries/Dictionary1.txt", "r")
    ListEntry = DicEntry.readlines()
    DicEntry.close()
    for i in range(len(ListEntry)):
        if ListEntry[i].find(","):
            ListEntry[i] = ListEntry[i].split(",")
        elif ListEntry == "":
            ListEntry[i] = []
        else:
            ListEntry[i] = [ListEntry[i]]
        ListEntry[i][len(ListEntry[i]) - 1] = ListEntry[i][len(ListEntry[i]) - 1].replace("\n", "")
    for i in range(len(ListEntry)):
        if ListEntry[i] == ['']:
            pass
        else:
            for j in range(len(ListEntry[i])):
                word = ListEntry[i][j]
                if word[0] in _eng_chars:
                    newRUword = ''
                    newUAword = ''
                    for k in range(len(word)):
                        index = _eng_chars.find(word[k])
                        newRUword += _rus_chars[index]
                        newUAword += _ukr_chars[index]
                    if newRUword not in ListEntry[i]:
                        ListEntry[i].append(newRUword)
                    if newUAword not in ListEntry[i]:
                        ListEntry[i].append(newUAword)
                elif word[0] in _rus_chars:
                    newENword = ''
                    newUAword = ''
                    for k in range(len(word)):
                        index = _rus_chars.find(word[k])
                        newENword += _eng_chars[index]
                        newUAword += _ukr_chars[index]
                    if newENword not in ListEntry[i]:
                        ListEntry[i].append(newENword)
                    if newUAword not in ListEntry[i]:
                        ListEntry[i].append(newUAword)
                elif word[0] in _ukr_chars:
                    newENword = ''
                    newRUword = ''
                    for k in range(len(word)):
                        index = _ukr_chars.find(word[k])
                        newENword += _eng_chars[index]
                        newRUword += _rus_chars[index]
                    if newENword not in ListEntry[i]:
                        ListEntry[i].append(newENword)
                    if newRUword not in ListEntry[i]:    
                        ListEntry[i].append(newRUword)

    DicEqual = open("Dictionaries/Dictionary2.txt", "r")
    ListEqual = DicEqual.readlines()
    DicEqual.close()
    for i in range(len(ListEqual)):
        if ListEqual[i].find(","):
            ListEqual[i] = ListEqual[i].split(",")
        elif ListEqual == "":
            ListEqual[i] = []
        else:
            ListEqual[i] = [ListEqual[i]]
        ListEqual[i][len(ListEqual[i]) - 1] = ListEqual[i][len(ListEqual[i]) - 1].replace("\n", "")

def SearchValuesAndCurrencies(arr):
    Indexes = [] #содержит индексы местонахождения
    CurNumber = [] #содержит номера валют
    i = 0
    j = 0
    while i < len(ListEntry):
        while j < len(ListEntry[i]):
            for u in range(len(arr)):
                if arr[u].find(ListEntry[i][j]) == 0 and ListEntry[i] != ['']:
                    if u != len(arr) - 1 and u != 0:
                        if arr[u + 1][0].isdigit():
                            Indexes.append(u)
                            CurNumber.append(i)
                        elif arr[u - 1][0].isdigit():
                            Indexes.append(u)
                            CurNumber.append(i)
                    elif u == len(arr) - 1 and arr[u - 1][0].isdigit():
                        Indexes.append(u)
                        CurNumber.append(i)
                    elif u == 0 and arr[u + 1][0].isdigit():
                        Indexes.append(u)
                        CurNumber.append(i)

                """ if len(Indexes) >= 50:
                    return [[],[]] """
            j += 1
        i += 1
        j = 0
    i = 0
    j = 0
    while i < len(ListEqual):
        while j < len(ListEqual[i]):
            for u in range(len(arr)):
                if arr[u] == ListEqual[i][j]:
                    if u != len(arr) - 1 and u != 0:
                        if arr[u + 1][0].isdigit():
                            Indexes.append(u)
                            CurNumber.append(i)
                        elif arr[u - 1][0].isdigit():
                            Indexes.append(u)
                            CurNumber.append(i)
                    elif u == len(arr) - 1 and arr[u - 1][0].isdigit():
                        Indexes.append(u)
                        CurNumber.append(i)
                    elif u == 0 and arr[u + 1][0].isdigit():
                        Indexes.append(u)
                        CurNumber.append(i)
                if len(Indexes)>=50:
                    return [[],[]]
            j += 1
        i += 1
        j = 0
    
    suma = []
    i = 0
    while i <= len(Indexes) - 1:
        e = Indexes[i]
        if e == 0 and arr[len(arr) + 1][0].isdigit():
            suma.append(arr[e - 1])
        elif arr[e - 1][0].isdigit():
            suma.append(arr[e - 1])
        elif arr[e + 1][0].isdigit():
            suma.append(arr[e + 1])
        i += 1
    answ_ar = [suma, CurNumber]
    return answ_ar

def TextToDigit(b):
    """ for i in range(len(b)):
        if b[i] in RUdict:
            b[i] = RUdict[b[i]] """

    i = len(b) - 1
    while i > 0:
        if (b[i] == "к" or b[i] == "k" or "тыс" in b[i] or "тис" in b[i] or "thousand" in b[i]) and b[i - 1][0].isdigit(): #2.5к = 2500
            b[i - 1] = str(float(b[i - 1]) * 1000)
            del b[i]
        elif (b[i] == "кк" or b[i] == "kk" or "млн" in b[i]) and b[i - 1][0].isdigit(): #2.5кк = 2500000
            b[i - 1] = str(float(b[i - 1]) * 1000000)
            del b[i]
        elif (b[i] == "ккк" or b[i] == "kkk") and b[i - 1][0].isdigit(): #2.5ккк = 2500000000
            b[i - 1] = str(float(b[i - 1]) * 1000000000)
            del b[i]
        i -= 1
    return b
    