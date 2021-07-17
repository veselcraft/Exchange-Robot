from NewPrint import Print
from DBH import GetAllCrypto, GetAllCurrencies, GetExchangeRates, GetListOfCrypto, GetListOfCurrencies, GetListOfFlags
import GetExchangeRates

ListOfCur = []
ListOfCrypto = []

DictOfFlags = []

ListEntry = []
ListEqual = []
ListCryptoEntry = []
ListCryptoEqual = []

_eng_chars = u"`qwertyuiop[]asdfghjkl;'zxcvbnm,.QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM,."
_rus_chars = u"ёйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
_ukr_chars = u"'йцукенгшщзхїфівапролджєячсмитьбюЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ"

def SpecialSplit(MesTxt: str) -> list:
    MesTxt = MesTxt.replace("\n", " , ") # Replace hyphenation with dot

    while MesTxt.find("  ") != -1: # Removing double spaces
        MesTxt = MesTxt.replace("  ", " ")

    for i in range(len(MesTxt) - 2):
        if MesTxt[i].isdigit() and MesTxt[i + 2].isdigit() and MesTxt[i + 1] == ",":
            MesTxt = MesTxt[0:i + 1] + "." + MesTxt[i + 2:len(MesTxt)] # comma to dot

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
        elif MesTxt[i].isalpha() and not MesTxt[i + 1].isalpha() and not MesTxt[i + 1].isdigit(): #separating letters from symbols
            end = i + 1
            a.append(MesTxt[start:end])
            start = end
        elif MesTxt[i + 1].isalpha() and not MesTxt[i].isalpha() and not MesTxt[i].isdigit(): #separating symbols from letters
            end = i + 1
            a.append(MesTxt[start:end])
            start = end
        elif not MesTxt[i].isalpha() and not MesTxt[i].isdigit() and not MesTxt[i + 1].isalpha() and not MesTxt[i + 1].isdigit(): #separating symbols from letters
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

def LoadCrypto():
    global ListOfCrypto
    ListOfCrypto = GetListOfCrypto()

def LoadFlags():
    global DictOfFlags
    DictOfFlags = GetListOfFlags()

def LoadDictionaries():
    global ListEntry, ListEqual, ListCryptoEntry, ListCryptoEqual

    DicEntry = open("Dictionaries/CurEntry.txt", "r")
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

    DicEqual = open("Dictionaries/CurEqual.txt", "r")
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
    for i in range(len(ListEqual)):
        if ListEqual[i] == ['']:
            pass
        else:
            for j in range(len(ListEqual[i])):
                word = ListEqual[i][j]
                if word[0] in _eng_chars:
                    newRUword = ''
                    newUAword = ''
                    for k in range(len(word)):
                        index = _eng_chars.find(word[k])
                        newRUword += _rus_chars[index]
                        newUAword += _ukr_chars[index]
                    if newRUword not in ListEqual[i]:
                        ListEqual[i].append(newRUword)
                    if newUAword not in ListEqual[i]:
                        ListEqual[i].append(newUAword)
                elif word[0] in _rus_chars:
                    newENword = ''
                    newUAword = ''
                    for k in range(len(word)):
                        index = _rus_chars.find(word[k])
                        newENword += _eng_chars[index]
                        newUAword += _ukr_chars[index]
                    if newENword not in ListEqual[i]:
                        ListEqual[i].append(newENword)
                    if newUAword not in ListEqual[i]:
                        ListEqual[i].append(newUAword)
                elif word[0] in _ukr_chars:
                    newENword = ''
                    newRUword = ''
                    for k in range(len(word)):
                        index = _ukr_chars.find(word[k])
                        newENword += _eng_chars[index]
                        newRUword += _rus_chars[index]
                    if newENword not in ListEqual[i]:
                        ListEqual[i].append(newENword)
                    if newRUword not in ListEqual[i]:    
                        ListEqual[i].append(newRUword)

    DicCryptoEntry = open("Dictionaries/CryptoEntry.txt", "r")
    ListCryptoEntry = DicCryptoEntry.readlines()
    DicCryptoEntry.close()
    for i in range(len(ListCryptoEntry)):
        if ListCryptoEntry[i].find(","):
            ListCryptoEntry[i] = ListCryptoEntry[i].split(",")
        elif ListCryptoEntry == "":
            ListCryptoEntry[i] = []
        else:
            ListCryptoEntry[i] = [ListCryptoEntry[i]]
        ListCryptoEntry[i][len(ListCryptoEntry[i]) - 1] = ListCryptoEntry[i][len(ListCryptoEntry[i]) - 1].replace("\n", "")
    for i in range(len(ListCryptoEntry)):
        if ListCryptoEntry[i] == ['']:
            pass
        else:
            for j in range(len(ListCryptoEntry[i])):
                word = ListCryptoEntry[i][j]
                if word[0] in _eng_chars:
                    newRUword = ''
                    newUAword = ''
                    for k in range(len(word)):
                        index = _eng_chars.find(word[k])
                        newRUword += _rus_chars[index]
                        newUAword += _ukr_chars[index]
                    if newRUword not in ListCryptoEntry[i]:
                        ListCryptoEntry[i].append(newRUword)
                    if newUAword not in ListCryptoEntry[i]:
                        ListCryptoEntry[i].append(newUAword)
                elif word[0] in _rus_chars:
                    newENword = ''
                    newUAword = ''
                    for k in range(len(word)):
                        index = _rus_chars.find(word[k])
                        newENword += _eng_chars[index]
                        newUAword += _ukr_chars[index]
                    if newENword not in ListCryptoEntry[i]:
                        ListCryptoEntry[i].append(newENword)
                    if newUAword not in ListCryptoEntry[i]:
                        ListCryptoEntry[i].append(newUAword)
                elif word[0] in _ukr_chars:
                    newENword = ''
                    newRUword = ''
                    for k in range(len(word)):
                        index = _ukr_chars.find(word[k])
                        newENword += _eng_chars[index]
                        newRUword += _rus_chars[index]
                    if newENword not in ListCryptoEntry[i]:
                        ListCryptoEntry[i].append(newENword)
                    if newRUword not in ListCryptoEntry[i]:    
                        ListCryptoEntry[i].append(newRUword)

    DicCryptoEqual = open("Dictionaries/CryptoEqual.txt", "r")
    ListCryptoEqual = DicCryptoEqual.readlines()
    DicCryptoEqual.close()
    for i in range(len(ListCryptoEqual)):
        if ListCryptoEqual[i].find(","):
            ListCryptoEqual[i] = ListCryptoEqual[i].split(",")
        elif ListCryptoEqual == "":
            ListCryptoEqual[i] = []
        else:
            ListCryptoEqual[i] = [ListCryptoEqual[i]]
        ListCryptoEqual[i][len(ListCryptoEqual[i]) - 1] = ListCryptoEqual[i][len(ListCryptoEqual[i]) - 1].replace("\n", "")
    for i in range(len(ListCryptoEqual)):
        if ListCryptoEqual[i] == ['']:
            pass
        else:
            for j in range(len(ListCryptoEqual[i])):
                word = ListCryptoEqual[i][j]
                if word[0] in _eng_chars:
                    newRUword = ''
                    newUAword = ''
                    for k in range(len(word)):
                        index = _eng_chars.find(word[k])
                        newRUword += _rus_chars[index]
                        newUAword += _ukr_chars[index]
                    if newRUword not in ListCryptoEqual[i]:
                        ListCryptoEqual[i].append(newRUword)
                    if newUAword not in ListCryptoEqual[i]:
                        ListCryptoEqual[i].append(newUAword)
                elif word[0] in _rus_chars:
                    newENword = ''
                    newUAword = ''
                    for k in range(len(word)):
                        index = _rus_chars.find(word[k])
                        newENword += _eng_chars[index]
                        newUAword += _ukr_chars[index]
                    if newENword not in ListCryptoEqual[i]:
                        ListCryptoEqual[i].append(newENword)
                    if newUAword not in ListCryptoEqual[i]:
                        ListCryptoEqual[i].append(newUAword)
                elif word[0] in _ukr_chars:
                    newENword = ''
                    newRUword = ''
                    for k in range(len(word)):
                        index = _ukr_chars.find(word[k])
                        newENword += _eng_chars[index]
                        newRUword += _rus_chars[index]
                    if newENword not in ListCryptoEqual[i]:
                        ListCryptoEqual[i].append(newENword)
                    if newRUword not in ListCryptoEqual[i]:    
                        ListCryptoEqual[i].append(newRUword)

def SearchValuesAndCurrencies(arr: list) -> list:
    Values = [] #содержит суммы
    CurNumber = [] #содержит номера валют
    CryptoValues = [] #сожержит суммы
    CryptoNumber = [] #содержит номера криптовалют
    i = 0
    j = 0
    while i < len(ListEntry):
        while j < len(ListEntry[i]):
            for u in range(len(arr)):
                if u != len(arr) - 1 and (arr[u] + " " + arr[u + 1]).find(ListEntry[i][j]) == 0 and ListEntry[i] != ['']:
                    if u <= len(arr) - 3 and u != 0:
                        if arr[u + 2][0].isdigit():
                            Values.append(arr[u + 2])
                            CurNumber.append(i)
                        elif arr[u - 1][0].isdigit():
                            Values.append(arr[u - 1])
                            CurNumber.append(i)
                    elif u == len(arr) - 2 and arr[u - 1][0].isdigit():
                        Values.append(arr[u - 1])
                        CurNumber.append(i)
                    elif u == 0 and arr[u + 2][0].isdigit():
                        Values.append(arr[u + 2])
                        CurNumber.append(i)
                elif arr[u].find(ListEntry[i][j]) == 0 and ListEntry[i] != ['']:
                    if u != len(arr) - 1 and u != 0:
                        if arr[u + 1][0].isdigit():
                            Values.append(arr[u + 1])
                            CurNumber.append(i)
                        elif arr[u - 1][0].isdigit():
                            Values.append(arr[u - 1])
                            CurNumber.append(i)
                    elif u == len(arr) - 1 and arr[u - 1][0].isdigit():
                        Values.append(arr[u - 1])
                        CurNumber.append(i)
                    elif u == 0 and arr[u + 1][0].isdigit():
                        Values.append(arr[u + 1])
                        CurNumber.append(i)
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
                            #Indexes.append(u)
                            Values.append(arr[u + 1])
                            CurNumber.append(i)
                        elif arr[u - 1][0].isdigit():
                            #Indexes.append(u)
                            Values.append(arr[u - 1])
                            CurNumber.append(i)
                    elif u == len(arr) - 1 and arr[u - 1][0].isdigit():
                        #Indexes.append(u)
                        Values.append(arr[u - 1])
                        CurNumber.append(i)
                    elif u == 0 and arr[u + 1][0].isdigit():
                        #Indexes.append(u)
                        Values.append(arr[u + 1])
                        CurNumber.append(i)
            j += 1
        i += 1
        j = 0
    
    i = 0
    j = 0
    while i < len(ListCryptoEntry):
        while j < len(ListCryptoEntry[i]):
            for u in range(len(arr)):
                if u != len(arr) - 1 and (arr[u] + " " + arr[u + 1]).find(ListCryptoEntry[i][j]) == 0 and ListCryptoEntry[i] != ['']:
                    if u <= len(arr) - 3 and u != 0:
                        if arr[u + 2][0].isdigit():
                            CryptoValues.append(arr[u + 2])
                            CryptoNumber.append(i)
                        elif arr[u - 1][0].isdigit():
                            CryptoValues.append(arr[u - 1])
                            CryptoNumber.append(i)
                    elif u == len(arr) - 2 and arr[u - 1][0].isdigit():
                        CryptoValues.append(arr[u - 1])
                        CryptoNumber.append(i)
                    elif u == 0 and arr[u + 2][0].isdigit():
                        CryptoValues.append(arr[u + 2])
                        CryptoNumber.append(i)
                elif arr[u].find(ListCryptoEntry[i][j]) == 0 and ListCryptoEntry[i] != ['']:
                    if u != len(arr) - 1 and u != 0:
                        if arr[u + 1][0].isdigit():
                            CryptoValues.append(arr[u + 1])
                            CryptoNumber.append(i)
                        elif arr[u - 1][0].isdigit():
                            CryptoValues.append(arr[u - 1])
                            CryptoNumber.append(i)
                    elif u == len(arr) - 1 and arr[u - 1][0].isdigit():
                        CryptoValues.append(arr[u - 1])
                        CryptoNumber.append(i)
                    elif u == 0 and arr[u + 1][0].isdigit():
                        CryptoValues.append(arr[u + 1])
                        CryptoNumber.append(i)
            j += 1
        i += 1
        j = 0
    i = 0
    j = 0
    while i < len(ListCryptoEqual):
        while j < len(ListCryptoEqual[i]):
            for u in range(len(arr)):
                if arr[u] == ListCryptoEqual[i][j]:
                    if u != len(arr) - 1 and u != 0:
                        if arr[u + 1][0].isdigit():
                            #Indexes.append(u)
                            CryptoValues.append(arr[u + 1])
                            CryptoNumber.append(i)
                        elif arr[u - 1][0].isdigit():
                            #Indexes.append(u)
                            CryptoValues.append(arr[u - 1])
                            CryptoNumber.append(i)
                    elif u == len(arr) - 1 and arr[u - 1][0].isdigit():
                        #Indexes.append(u)
                        CryptoValues.append(arr[u - 1])
                        CryptoNumber.append(i)
                    elif u == 0 and arr[u + 1][0].isdigit():
                        #Indexes.append(u)
                        CryptoValues.append(arr[u + 1])
                        CryptoNumber.append(i)
            j += 1
        i += 1
        j = 0
    answ_ar = [Values, CurNumber, CryptoValues, CryptoNumber]

    n = len(answ_ar[0])
    i = 0
    while i < n:
        for j in range(len(answ_ar[0])):
            if answ_ar[1][i] == answ_ar[1][j] and answ_ar[0][i] == answ_ar[0][j] and j != i:
                answ_ar[0].pop(j)
                answ_ar[1].pop(j)
                j -= 1
                n -= 1
                break
        i += 1
    n = len(answ_ar[2])
    i = 0
    while i < n:
        for j in range(len(answ_ar[2])):
            if answ_ar[3][i] == answ_ar[3][j] and answ_ar[2][i] == answ_ar[2][j] and j != i:
                answ_ar[2].pop(j)
                answ_ar[3].pop(j)
                j -= 1
                n -= 1
                break
        i += 1
    return answ_ar

def TextToDigit(b: list) -> list:
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
    
def AnswerText(Arr: list, chatID: str) -> str:
    global DictOfFlags
    global ListOfCur
    global ListOfCrypto

    answer = ''
    for i in range(len(Arr[1])): #Проходимся по всем распознаным классическим валютам
        answer += "\n" + "======" + "\n"
        CurVault = float(Arr[0][i])
        CurCurrency = ListOfCur[Arr[1][i]]
        PartOfAnswer = DictOfFlags[CurCurrency] + str(f'{CurVault:,}'.replace(","," ")) + " " + CurCurrency + "\n"

        ListOfChatCurrencies = GetAllCurrencies(chatID)
        ListOfChatCrypto = GetAllCrypto(chatID)
        for j in ListOfChatCurrencies: #Проходимся по всем классическим валютам
            if CurCurrency == j:
                pass
            elif j == 'EUR':
                Vault = round(CurVault / GetExchangeRates.exchangeRates[CurCurrency], 2)
                Vault = f'{Vault:,}'.replace(","," ")
                PartOfAnswer += "\n" + DictOfFlags[j] + str(Vault) + j
            elif j != 'EUR':
                Vault = round(CurVault * (GetExchangeRates.exchangeRates[j] / GetExchangeRates.exchangeRates[CurCurrency]), 2)
                Vault = f'{Vault:,}'.replace(","," ")
                PartOfAnswer += "\n" + DictOfFlags[j] + str(Vault) + " " + j
        if CurCurrency == 'UAH' and CurVault == 40.0:
            PartOfAnswer += "\n👖1 штаны"
        elif CurCurrency == 'USD' and CurVault == 300.0:
            PartOfAnswer += "\n🤛1"

        if len(ListOfChatCurrencies) != 0:
            PartOfAnswer += "\n"
        
        for j in ListOfChatCrypto: #Проходимся по всем криптовалютам
            if CurCurrency == 'EUR':
                Vault = round(CurVault / GetExchangeRates.exchangeRates[CurCurrency] / GetExchangeRates.cryptoRates[j], 9)
                Vault = f'{Vault:,}'.replace(","," ")
                PartOfAnswer += "\n" + str(Vault) + " " + j
            elif CurCurrency != 'EUR':
                Vault = round(CurVault * (GetExchangeRates.exchangeRates['USD'] / GetExchangeRates.exchangeRates[CurCurrency] / GetExchangeRates.cryptoRates[j]), 9)
                Vault = f'{Vault:,}'.replace(","," ")
                PartOfAnswer += "\n" + str(Vault) + " " + j
        answer += PartOfAnswer + "\n"

    for i in range(len(Arr[3])): #Проходимся по всем распознаным криптовалютам
        answer += "\n" + "======" + "\n"
        CurVault = float(Arr[2][i])
        CurCurrency = ListOfCrypto[Arr[3][i]]
        PartOfAnswer = str(f'{CurVault:,}'.replace(","," ")) + " " + CurCurrency + "\n"

        ListOfChatCurrencies = GetAllCurrencies(chatID)
        ListOfChatCrypto = GetAllCrypto(chatID)
        for j in ListOfChatCurrencies: #Проходимся по всем классическим валютам
            if j == 'EUR':
                Vault = round(CurVault * 1 / GetExchangeRates.exchangeRates['USD'] * GetExchangeRates.cryptoRates[CurCurrency], 2)
                Vault = f'{Vault:,}'.replace(","," ")
                PartOfAnswer += "\n" + DictOfFlags[j] + str(Vault) + " " + j
            elif j != 'EUR':
                Vault = round(CurVault * GetExchangeRates.exchangeRates[j] / GetExchangeRates.exchangeRates['USD'] * GetExchangeRates.cryptoRates[CurCurrency], 2)
                Vault = f'{Vault:,}'.replace(","," ")
                PartOfAnswer += "\n" + DictOfFlags[j] + str(Vault) + " " + j

        if len(ListOfChatCurrencies) != 0:
            PartOfAnswer += "\n"
        
        for j in ListOfChatCrypto: #Проходимся по всем криптовалютам
            if CurCurrency == j:
                pass
            else:
                Vault = round(CurVault * GetExchangeRates.cryptoRates[CurCurrency] / GetExchangeRates.cryptoRates[j], 9)
                Vault = f'{Vault:,}'.replace(","," ")
                PartOfAnswer += "\n" + str(Vault) + " " + j
        answer += PartOfAnswer + "\n"

    return answer

def UpdateUsingStats():
    return None