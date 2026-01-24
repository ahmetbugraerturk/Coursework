"""This line is written to change the working directory from parts folder to root folder"""
import os
os.chdir(r'../')

def decrypt_the_message(input_path, s, output_path):
    """Function to decrypt the message in the input file and write the decrypted message to the output file."""
    letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    nums = "12345678901234567890"
    with open(input_path, "r") as inp:
        with open(output_path, "w") as out:
            for line in inp:
                decrypted = ""
                for char in line:
                    if char.isalpha():
                        if char.islower():
                            decrypted += letters[letters.find(char)-s]
                        elif char.isupper():
                            decrypted += letters.upper()[letters.upper().find(char)-s]
                    elif char.isnumeric():
                        decrypted += nums[nums.find(char)-s]
                    else:
                        decrypted += char
                out.write(decrypted)
