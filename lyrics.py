#!/usr/bin/python3

class Lyrics( object ):

    def __init__( self, song ):

        self.title  = song[1]
        self.year   = song[2] 
        self.artist = song[3]
        self.genre  = song[4]
        self.lyrics = song[5]

    def __str__( self ):
        return "[" + self.genre + "]\t"+\
              self.artist + " - " + self.title +\
              "\t(" + self.year + ") "
