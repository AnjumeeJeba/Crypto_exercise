# Ex 1

# Input a string of English text
text = input("Enter a string of English text: ")

# Initialize an empty string to store the processed text
processed_text = ""

# Define a string containing all uppercase letters
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Loop through each character in the input text
for char in text:
    # Check if the character is an uppercase letter
    if char in uppercase_letters:
        # Append the uppercase letter to the processed text
        processed_text += char

# Create a list of numbers representing the letters in the processed text
letter_numbers = [ord(char) - 65 for char in processed_text]

# Initialize a list of 26 zeros to count letter frequencies
letter_frequencies = [0] * 26

# Define a set of punctuation characters
punctuation = set(".,!?;:'\"()[]{}")

# Iterate through the input text
for char in text:
    if char.isalpha():  # Check if the character is alphabetic
        processed_text += char.upper()  # Convert to uppercase and append to cleaned_text
        letter_frequencies[ord(char.upper()) - ord('A')] += 1

# Print the cleaned text (uppercase without punctuation)
print("Processed Text:", processed_text)

# Print the frequency count of each letter
for letter, count in zip(range(26), letter_frequencies):
    print(f"{chr(letter + ord('A'))}: {count} occurrences")

# Calculate the percentage of E, T, and A
percentage_E = (letter_frequencies[ord("E") - 65] / len(letter_numbers)) * 100
percentage_T = (letter_frequencies[ord("T") - 65] / len(letter_numbers)) * 100
percentage_A = (letter_frequencies[ord("A") - 65] / len(letter_numbers)) * 100

# Print the processed text, letter frequencies, and percentages
print("Processed Text (Uppercase without Punctuation):", processed_text)
print("Letter Frequencies:", letter_frequencies)
print("Percentage of E:", percentage_E)
print("Percentage of T:", percentage_T)
print("Percentage of A:", percentage_A)

# Ex 2

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def modinvert(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


# Input a string of English capital letters
T = input("Enter a string of English capital letters: ")

# Input two integers a and b
a = int(input("Enter an odd integer a (0 < a < 26, not 13): "))
b = int(input("Enter an integer b (0 < |b| < 26): "))

# Sanity check for input values
if not (0 < a < 26 and a % 2 != 0 and a != 13 and 0 < abs(b) < 26):
    print("Input values are not valid.")
    exit()

# Perform the affine transformation and print the result
for c in T:
    transformed_letter = chr(65 + (a * (ord(c) - 65) + b) % 26)
    print(transformed_letter, end='')

print()  # Print a newline for a clean output

# Ex 3

# Input a string of 8 hexadecimals
H = input("Enter a string of 8 hexadecimals: ")

# Input a string of 16 capital letters
Letters = input("Enter a string of 16 capital letters: ")

# Check the validity of the hexadecimal string
if not (len(H) == 8 and all(h in "0123456789abcdef" for h in H)):
    print("Invalid hexadecimal input.")
    exit()

# Define the hexchar to bit conversion array
hxarray = [
    [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1],
    [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1],
    [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
    [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1],
    [0, 0, 0, 1], [0, 0, 1, 0]
]

# Convert the hexadecimal string to a list of lists of bits
matrix_hex = [[hxarray[int(hexchar, 16)] for hexchar in H]]

# Put the 16 capital letters into a numerical 4x4 matrix
numlist = [ord(x) - 65 for x in Letters]
matrix_letters = [numlist[i:i + 4] for i in range(0, 16, 4)]

# Initialize an empty matrix for the result
result_matrix = [[0 for _ in range(4)] for _ in range(8)]

# Flatten matrix_hex into a single list of numbers
flat_matrix_hex = [num for sublist in matrix_hex for num in sublist]

# Flatten matrix_letters into a single list of numbers
flat_matrix_letters = [num for row in matrix_letters for num in row]


for i in range(8):
    for j in range(4):
        temp_sum = 0  # Reset temp_sum for each calculation
        for k in range(4):
            temp_sum = matrix_hex[0][k] * matrix_letters[k][j]
            temp_sum = 0  # Initialize temp_sum as an integer
        result_matrix[i][j] = temp_sum % 26  # Assign the accumulated value to the result matrix

# Convert the result matrix to capital letters
result_letters = ''.join([chr(x + 65) for row in result_matrix for x in row])

# Print the result
for i in range(0, len(result_letters), 4):
    print(result_letters[i:i + 4])


# Ex 4

ROUNDS = 4  # Number of rounds in the Feistel network

# Input a text string
text = input("Enter a text string: ")

# Transform the text to a list of numbers (0-25)
letters = [ord(char) - ord('A') for char in text]

# Pad the list to have a length multiple of 16 with zeros
remainder = len(letters) % 16
if remainder != 0:
    padding = [0] * (16 - remainder)
    letters.extend(padding)


# Define the Feistel-like transformation function
def feistel(left_half, right_half, round_num):
    new_left = right_half
    new_right = [(x + (round_num * y)) % 26 for x, y in zip(left_half, right_half)]
    return new_left, new_right


# Split the letters into blocks of 16
blocks = [letters[i:i + 16] for i in range(0, len(letters), 16)]

# Apply Feistel-like transformation to each block
for block in blocks:
    left_half, right_half = block[:8], block[8:]
    for round_num in range(ROUNDS):
        left_half, right_half = feistel(left_half, right_half, round_num)
    block[:8], block[8:] = right_half, left_half

# Flatten the transformed blocks into a single list
transformed_letters = [char for block in blocks for char in block]

# Convert the numbers back to characters
transformed_text = ''.join([chr(num + ord('A')) for num in transformed_letters])

# Print the transformed text
print("Transformed Text:", transformed_text)
