centipawnloss
=============

centipawnloss.py is a simple script that calculates
[lichess.org](http://lichess.org) style average centipawn loss
statistics from pgn files.  The pgn files must already be analyzed by
an engine and those engine evaluations should be formatted in a
particular way.  This script was designed with analyzing pgn files
generated with Scid vs PC in mind.  In order to ensure the best chance
of this script working you should export your pgn files without
variations and with an evaluation score after each move.  Multigame
pgn files are supported.

    python3 centipawnloss.py /path/to/game.pgn 