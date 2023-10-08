# Crypto_exercise
Exercising codes of Cryptography Engineering
# Ex_1. Simple traversal of a string.

Input an English text string and output the same string in uppercase without any punctuation or non-letter characters. Create a list of numbers corresponding to the converted letters (A=0, B=1, ..., Z=25). Then, calculate the frequency count of each letter and find the percentage of E, T, and A in the text to assess its typicality in English.

# Ex_2. Error checking. Simple calculation. A function.

Create a Python program that takes a string of capital letters, along with two integers 'a' and 'b' (where 'a' is an odd number not equal to 13, and 'b' is within the range (-26, 26)). The program validates the input and performs an affine transformation on the letters, outputting the transformed string. It ensures the correctness of 'a' by utilizing the provided modinvert() function for finding the modular inverse. This program is designed to work with valid input, providing an error message for invalid input conditions.


# Ex_3. Matrices, a little of bits

Input an 8-character hexadecimal string and a 16-character uppercase letter string. Validate the input hex string and convert each hex digit into a 4-bit binary representation, forming an 8x4 matrix. Convert the uppercase letters into a numerical 4x4 matrix. Multiply the two matrices modulo 26 and output the result as a matrix of capital letters.


# Ex_4. Feistel network, with trivial transformation, without a key

Input a text string, convert it to a list of numbers (0-25), and pad it to a multiple of 16. Implement a Feistel network with a specified number of rounds (initially 4) on 16-letter blocks, applying a specific transformation to each block. Understand and discuss the reversibility of this transformation. Test your code incrementally, and it should return the original input with swapped halves after an even number of rounds.
