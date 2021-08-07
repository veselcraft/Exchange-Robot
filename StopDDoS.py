import time
import BlackList

listOfUsersCurTimes = [] #1000 записей
TimeOfBlockedUsers = []

def updateData(userID: str, chatID: str, countOfCur: int, chatName: str) -> bool:
    if countOfCur > 50:
        BlackList.AddToBlackList(userID, chatID, chatName)
        return True
    else:
        global listOfUsersCurTimes
        while len(listOfUsersCurTimes) >= 1000:
            listOfUsersCurTimes.pop(0)
        listOfUsersCurTimes.append([userID, countOfCur, int(time.time())])

        countOfCurInList = 0
        countTimesInList = 0
        for i in range(len(listOfUsersCurTimes)):
            if listOfUsersCurTimes[i][0] == userID:
                countOfCurInList += listOfUsersCurTimes[i][1]
                countTimesInList += 1

        if countOfCurInList / countTimesInList > 15 and countTimesInList > 10:
            BlackList.AddToBlackList(userID, chatID, chatName)
            return True
        
        return False