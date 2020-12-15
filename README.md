### CircleFifths 

This simple program takes the root key of a 12 note scale and shifts the elements according to the root note. 

### Motivation 

The purpose of this program is to make a circle of fifths with different scales/modes in ascending order. 
Eventually, the project will be meant to generate complex melodies from python scripts to puredata or any device that can recieve midi. 
This program is geared towards both musicans and programmers. 

### Build Status 
Experimenting with MIDI and python. 

### Example
1. Select a root key:
'E'
The program will output the notes in the key of 'E'

['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D# ]

2. Select a mode:
major
minor
phrygian
lydian
mixolydian
aeolian
locrian
chromatic
wholetone
diminished7thchord
augmentedchord
tritone

3. The program will return all the notes in ascending order towards the higher octave which will look like this:

 ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
    
The program is heavily modeled after the pitch constillation.
The notes in a key sequence operate as a clock. 
Counterclockwise the notes go down a scale and the flats are sharps.
Clockwise the notes go up a scale and the sharps are flats. (Essentially they're the same notes.)


                              E(0)
                    D#(11)             F(1)  
                    
                D(10)                        F#(2)
                 
                 
             C#(9)                             G(3) 
             
                                        
                C(8)                         G#(4)
                    
                    B(7)               A(5)
                              A#(6)



 
 
 
 
 
 
