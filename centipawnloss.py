# First we need to get the pgn file
pgnname = input("Analyze which file? ")
pgnfile = open(pgnname, 'r')
pgn = pgnfile.read()

# checking to see if I am remembering how to open file in python
# correctly.  pgn should be a string with the pgn data in it.
print(pgn)
