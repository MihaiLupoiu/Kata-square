# Kata-square
Presentation
------------

Find the largest possible square in a matrix, avoiding obstacles.

Details
------------

The matrix is in a text file with the signs "." and "o"

Example:  

$ cat example_file  

...........................  
....o......................  
............o..............  
...........................  
....o......................  
...............o...........
...........................
......o..............o.....
..o.......o................

Write a Python program that:
- Finds the largest possible square not including any obstacle "o"
- Shows it by replacing the "." by "x"

Example:  

> program.py example_file  

.....xxxxxxx...............
....oxxxxxxx...............  
.....xxxxxxxo..............  
.....xxxxxxx...............  
....oxxxxxxx...............  
.....xxxxxxx...o...........  
.....xxxxxxx...............  
......o..............o.....  
..o.......o................

(It is an square, even if it does not look like visually.)

Additional information:
- All the lines in the input have the same length
- The input matrix may not be an square- If there are several solutions, choose the one closest to the beginning of  the file (up and left corner)