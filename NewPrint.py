consoleLog = False

def Print(printingText):
    if consoleLog:
        print(printingText)

def EnableLogging():
    global consoleLog
    consoleLog = True

def DisableLogging():
    global consoleLog
    consoleLog = False