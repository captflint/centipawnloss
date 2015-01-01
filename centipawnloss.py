# First we need to get the pgn file.
import sys
pgnfile = open(sys.argv[1], 'r')
pgn = pgnfile.read()

# Next we need to parse the pgn file for the evaluation scores.  The
# pgn files that this script is programed to parse are generated by
# the program Scid vs PC which encloses evaluation scores in curly
# brackets.  The variation should be stripped to ensure proper
# parsing.
scores = []
evalstring = ""
recording = False

for char in pgn:
    if recording:
        if char in "1234567890.-+":
            evalstring += char
        else:
            recording = False
            scores.append(float(evalstring))
            evalstring = ""
    else:
        if char == "{":
            recording = True

# Now we do the actual math.
whiteloss = []
blackloss = []
white = True
lastscore = 0
for score in scores:
    if white:
        loss = lastscore - score
        if loss > 0:
            whiteloss.append(loss)
        else:
            whiteloss.append(0)
    else:
        loss = (lastscore - score) * -1
        if loss > 0:
            blackloss.append(loss)
        else:
            blackloss.append(0)
    white = not white
    lastscore = score

avgwl = sum(whiteloss) / len(whiteloss)
avgbl = sum(blackloss) / len(blackloss)

# Finally we print the results
print("White Average Centipawn Loss: ", int(avgwl * 100))
print("Black Average Centipawn Loss: ", int(avgbl * 100))
