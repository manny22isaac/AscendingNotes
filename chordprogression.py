
import random
#musicalModes

notes = ['C', 'C#', 'D', 'D#',
             'E', 'F', 'F#', 'G', 'G#',
             'A', 'A#','B']

rootkey = input("Enter the root Note: ").upper()
scale = input("Enter the Mode: ").lower()

class CircleFifths:
    """docstring for CircleFifths."""
    def __init__(self, scale, key):
        self.scale = scale
        self.rootkey = rootkey

    def shift(self, rootkey, index=0, s=0,):
        #shifts the leading item (rootkey) entered by the user down the list
        #removes the last term and puts it as the first term
        while index < 12 and s <12:
            s += 1
            index += 1
            new_notes = notes[-s:] + notes[:-s]
            if rootkey == new_notes[0]:
                print(new_notes)
                return new_notes

    #def modes(self, rootkey):
        #this function is currently being fixed
        #this takes the indexes of a string list of notes
        # and matches them to the integers of another list represented as a scale
        #keymode = []
        #major = [0, 2, 4, 5, 7, 9, 11]
        #keymode = [new_notes[i] for i in major]
        #print(keymode)

a = CircleFifths(scale, rootkey)
a.shift(rootkey)
