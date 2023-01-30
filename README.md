# Type And Count
This is a simple program that prompts the user to input a line of text and returns the number of words in that line.

## Description
"Type And Count" is a simple program that prompts the user to type in a line of text and then calculates the total number of words in the input. It does this by counting the number of spaces in the input and adding 1 for the last word, which is not followed by a space. The program outputs the total number of words to the user.

1.	## How to use
2.	Run the program by typing ‘python3 file-name.py’ in your terminal.
3.	When prompted, start typing your desired line of text.
4.	Press enter to submit your line of text.
5.	The program will return the number of words in your line of text.

## Example
Input: "Hello this is a test line"
Output: "6"

## Technical details
This program uses the built-in ‘input()’ function to gather user input, which is then stored in the variable line. The program then uses the ‘count()’ method to count the number of spaces in line and adds 1 to that count to account for the words in the line. Finally, it uses the ‘print()’ function to output the total number of words in the line.

## Contributions
This program is a simple script and does not require any contributions.

## License
This program is open-sourced and free to use for any purpose.

## Author
This program is created by xzebcex.

## Note
This program does not check for punctuation and will count it as a separate word.
