def printTop():
    for i in range(0,13):
        if i > 0:
            print i, "   ",
        else:
            print "     ",

def timesTable():
    printTop()
    table = [[0 for x in range(12)] for x in range(12)]
    for i in range(0,12):
        print ""
        print i+1, "   ",
        for j in range(0,12):
            table[i][j] = (i+1) * (j+1)
            print (i+1) * (j+1), "   ",

if __name__ == "__main__":
    timesTable()