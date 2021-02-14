shouldItBeUpdated = True

def IsUpdate():
    return not shouldItBeUpdated

def EnableUpdates():
    global shouldItBeUpdated
    shouldItBeUpdated = True

def DisableUpdates():
    global shouldItBeUpdated
    shouldItBeUpdated = False