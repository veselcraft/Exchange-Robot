import DBH

BlackList = []

def IsUserInBlackList(userID):
    if userID in BlackList:
        return True
    else:
        return False

def LoadBlackList():
    BlackList = DBH.GetBlacklist

def AddToBlackList(userID, chatID, chatName):
    if userID not in BlackList:
        BlackList.append(userID)
    DBH.AddBlacklist(userID, chatID, chatName)

def RemoveFromBlackList(userID):
    BlackList.remove(userID)
    DBH.ClearBlacklist(userID)