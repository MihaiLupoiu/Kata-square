#!/usr/bin/python
from __future__ import print_function
import sys
__author__ = 'mihai'

def readFile(fname):
    """

    :rtype : (BinaryMatrix,OriginalMatrix)
    """
    binaryMatrix = []
    originalMatrix = []
    with open(fname) as f:
        binaryLine = []
        originalLine = []
        while True:
            c = f.read(1)
            if not c:
                break
            elif c == ".":
                binaryLine.append(1)
                originalLine.append(".")
            elif c == "o":
                binaryLine.append(0)
                originalLine.append("o")
            elif c == "\n":
                binaryMatrix.append(binaryLine)
                originalMatrix.append(originalLine)
                binaryLine = []
                originalLine = []
    return (binaryMatrix, originalMatrix)


def printMaxSubSquare(mat, orMat):
    nrows = len(mat)
    ncols = 0
    if mat:
        ncols = len(mat[0])
    if not (nrows and ncols):
        return 0
    subMat = [[0] * ncols for _ in xrange(nrows)]

    ## Find the maximum entry, and indexes of maximum entry in subMat[][] ##
    for i in range(nrows):
        for j in range(ncols):
            if mat[i][j] == 1:
                subMat[i][j] = min(subMat[i][j - 1], subMat[i - 1][j], subMat[i - 1][j - 1]) + 1
            else:
                subMat[i][j] = 0;

    max_of_SubMax, max_i, max_j = subMat[0][0], 0, 0
    for i in range(nrows):
        for j in range(ncols):
            if max_of_SubMax < subMat[i][j]:
                max_of_SubMax = subMat[i][j]
                max_i = i
                max_j = j

    #print(max_of_SubMax, max_i, max_j)

    for i in range(max_i, max_i - max_of_SubMax, -1):
        for j in range(max_j, max_j - max_of_SubMax, -1):
            orMat[i][j] = "x"

    for i in orMat:
        for j in i:
            print(j,end ="")
        print()

if __name__ == "__main__":
    argument = len(sys.argv)
    if argument != 2:
        print("Help: console#> main.py fileToRead")
    else:
        binaryMatrix, orignalMatrix = readFile(sys.argv[1])
        printMaxSubSquare(binaryMatrix, orignalMatrix)
