# Read the numbers
import tkinter.filedialog

def openNumberFile():
    '''Opens a file that has a sequence of numbers separated by a space.
    Each line is a separate sequence of numbers. Makes a new list of int
    for each line and adds the new list to a master list of lists.
    Returns list of lists.
    '''
    numberFile = open(tkinter.filedialog.askopenfilename())
    numSetList = []
    for line in numberFile:
        seq = line.split()
        for i in range(len(seq)):
            seq[i] = int(seq[i])
        numSetList.append(seq)
    numberFile.close()
    return numSetList

# Find instances of consecutive numbers
def consecutiveDistanceRating(numSetList, step=1):
    '''(list of lists of int[, int]) -> int

    Prints the consecutive distance rating (CDR) of each list in numSetList.
    Step will define consecutive.

    >>> consecutiveDistanceRating([[1,2,3,4,5], [1,3,2,4,5]])
    4
    6
    >>> consecutiveDistanceRating([[1,2,3,4,5], [1,3,2,4,5]], step=2)
    6
    5
    '''
    for seq in range(len(numSetList)):
        total = 0
        for num in numSetList[seq]:
            if not (num + step) in numSetList[seq]:
                continue
            
            # compare the index value and add difference to total
            total += abs(numSetList[seq].index(num) -
                         numSetList[seq].index(num + step))
        print('Sequence %s\'s CDR is: %s' % (seq + 1, total))

consecutiveDistanceRating(openNumberFile())

input('Press any key to exit...')
