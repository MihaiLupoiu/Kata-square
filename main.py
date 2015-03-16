__author__ = 'myhay'

def readFile(fname):
    binariMatrix = []
    with open(fname) as f:
        line = []
        while True:
            c = f.read(1)
            if not c:
                break
            elif c == ".":
                line.append(1)
            elif c == "o":
                line.append(0)
            elif c == "\n":
                binariMatrix.append(line)
                line = []
    return binariMatrix

def max_size(mat, ZERO=0):
    nrows = len(mat)
    ncols = 0
    if mat:
        ncols = len(mat[0])
    if not (nrows and ncols):
        return 0
    counts = [[0]*ncols for _ in xrange(nrows)]
    for i in reversed(xrange(nrows)):     # for each row
        assert len(mat[i]) == ncols # matrix must be rectangular
        for j in reversed(xrange(ncols)): # for each element in the row
            if mat[i][j] != ZERO:
                counts[i][j] = (1 + min(
                    counts[i][j+1],  # east
                    counts[i+1][j],  # south
                    counts[i+1][j+1] # south-east
                    )) if i < (nrows - 1) and j < (ncols - 1) else 1 # edges
    print(counts)
    return max(c for rows in counts for c in rows)

matrix = readFile("example_file.txt")

print max_size(matrix)