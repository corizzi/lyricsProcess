#!/usr/bin/python3

class Occurence ( object ):

    """
    """

    def __init__( self, text, stopWords ):

        self.dict = {}

        # Remove metacharacters, spaces and ponctuations 
        for sep in ["\n", "'", ".", ",", "?", "!"]:
            text = ' '.join( text.split( sep ) )

        wordList = text.split(' ') 

        # Remove 1-letter words 
        wordList = [w for w in wordList if len(w) > 1]

        for word in wordList:
            # lowercase the word
            word = word.lower()
            if word not in stopWords:
                self.wordProcess( word )

        # TODO : ajouter le tri du dico ici


    def wordProcess( self, word ):

        """
        Word Process Method :
        > if the word isn't in the dict : add it
        > else +1 on the count 
        """

        # The word isn't in the dict
        if not word in self.dict:
            self.dict[ word ] =  1
        # The word is in the dict
        else:
            self.dict[ word ] += 1


    def mostCommon( self, n=-1 ):

        """
        Display the n most common words
        10 is the default value
        """

        # Sort the dict and browse in 
        if n == -2:
            print(sorted( self.dict, key=self.dict.get, reverse=True ))
            return

        i=0

        for word in sorted( self.dict, key=self.dict.get, reverse=True ):
            print( word )
