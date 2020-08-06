
import random
notes = ['C', 'C#', 'D', 'D#',
             'E', 'F', 'F#', 'G', 'G#',
             'A', 'A#','B']

scale = {'major':[0, 2, 4, 5, 7, 9, 11],
    'minor':[0, 2, 3, 5, 7, 8, 10],
    'phrygian':[0, 1, 3, 5, 7, 8, 10],
    'lydian':[0, 2, 4, 6, 7, 9, 11],
    'mixolydian':[0, 2, 4, 5, 7, 9, 10],
    'aeolian':[0, 2, 3, 5, 7, 8, 10],
    'locrian':[0, 1, 3, 5, 6, 8, 10],
    'chromatic':[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'wholetone':[0, 2, 4, 6, 8, 10],
    'diminished7thchord': [0, 3, 6, 9],
    'augmentedchord':[0, 4, 8],
    'tritone':[0, 6]}


rootkey = input("Enter the root Note: ").upper()

class CircleFifths:
    """docstring for CircleFifths."""
    def __init__(self, key):
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

    #def modes(self, new_notes):
        #this function is currently being fixed
        #this takes the indexes of a string list of notes
        # and matches them to the integers of another list represented as a scale
        #keymode = []

        #major = [0, 2, 4, 5, 7, 9, 11]
        #keymode = [new_notes[i] for i in major]
        #print(keymode)


def main():
    a = CircleFifths(rootkey)
    key = a.shift(rootkey)

    keymode = []

    print('Select a scale and enter it below')
    for k in scale:
        print(k)

    mode = input("Enter the mode: ").lower()
    x = scale.get(mode)


    keymode = [key[i] for i in x]
    print(keymode)


main()
