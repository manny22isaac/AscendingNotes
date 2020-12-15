#!/bin/python3
#this program is still in progress. I've yet to add the rest of the program.
notes = ('C', 'C#', 'D', 'D#',
             'E', 'F', 'F#', 'G', 'G#',
             'A', 'A#','B')

#changed the [] to () since the values won't change
#considering on adding harmonic and melodic scales
scale = {'major':(0, 2, 4, 5, 7, 9, 11),
    'minor':(0, 2, 3, 5, 7, 8, 10),
    'phrygian':(0, 1, 3, 5, 7, 8, 10),
    'lydian':(0, 2, 4, 6, 7, 9, 11),
    'mixolydian':(0, 2, 4, 5, 7, 9, 10),
    'aeolian':(0, 2, 3, 5, 7, 8, 10),
    'locrian':(0, 1, 3, 5, 6, 8, 10),
    'chromatic':(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
    'wholetone':(0, 2, 4, 6, 8, 10),
    'diminished7thchord': (0, 3, 6, 9),
    'augmentedchord':(0, 4, 8),
    'tritone':(0, 6)}

rootkey = input("Enter the root Note: ").upper()

class CircleFifths:
    """docstring for CircleFifths."""
    def __init__(self, key):
        self.rootkey = rootkey

    def shift(self, rootkey, first_index=0, first_s=0,):
        #shifts the leading item (rootkey) entered by the user down the list
        #removes the last term and puts it as the first term
        for index, s in zip(range(first_index, 12), range(first_s, 12)):
            first_index += 1
            first_s += 1
            new_notes = notes[-first_s:] + notes[:-first_s]
            if rootkey == new_notes[0]:
                return new_notes


def main():
    a = CircleFifths(rootkey)
    key = a.shift(rootkey)
    
    keymode = []
    print('Select a scale and enter it below')
    for k in scale:
        print(k)

    mode_name = input("Enter the mode: ").lower()
    mode = scale.get(mode_name)
    if mode is None:
        print( f"Scale {mode_name} not in list. Please start the program again.")
    else:
        key_mode = [key[i] for i in mode]
        print(key_mode)
main()

