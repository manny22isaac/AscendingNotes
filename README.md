### AscendingNotes 

This simple program takes the root key of a 12 note scale and shifts the elements according to the root note. 

### Motivation 

The purpose of this program is to make a circle of fifths with different scales/modes in ascending order. 
Eventually, the project will be meant to generate complex melodies from python scripts to puredata.
This program is geared towards both hobbyist musicans and programmers. 

### Build Status 
Currently in process of implementing the function modes() to CircleFifths.
Modes() will display which notes are in the scale/mode.

### Example
1. select a root key:
'E'
2. the mode option isn't available yet so just hit enter and skip
3. The program will return all the notes in ascending order towards the higher octave which will look like this:

    'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D# 
    
I modeled the program after the pitch constillation. 

                              E(0)
                    D#(11)             F(1)  
                    
                D(10)                        F#(2)
                 
                 
             C#(9)                             G(3) 
             
                                        
                C(8)                         G#(4)
                    
                    B(7)               A(5)
                              A#(6)
 
 
 
 
 
 
 
