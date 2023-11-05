"""
Main Program for Text Encryption and Decryption

This program allows the user to perform text encryption and decryption using a one-time pad (OTP).
It includes the following steps:
Part 1: Encryption
1. Generate a random key (OTP) for encryption.
2. Convert the user-provided plain text to numbers based on a letter-to-number mapping.
3. Calculate the initial total by adding the OTP numbers and plain text numbers.
4. Apply modulo 26 to the initial total to ensure it stays within the range [0, 25].
5. Convert the encrypted numbers back to letters and display the ciphertext.

Part 2: Decryption
1. Allow the user to input the ciphertext for decryption.
2. Input the decryption key (OTP).
3. Convert the ciphertext to numbers based on the letter-to-number mapping.
4. Subtract the OTP numbers from the ciphertext numbers to obtain the initial total for decryption.
5. Apply modulo 26 for the initial total to handle negative values.
6. Convert the decrypted numbers back to letters and display the plaintext.

Usage:
- Follow the prompts to input plain text, which will be encrypted, and later, input the ciphertext for decryption.
- Enter the decryption key (OTP) when prompted.

Note:
- The letter-to-number mapping is based on the English alphabet (A-Z).
- The code may be used as a starting point for implementing a simple text encryption and decryption application.
"""


import random
import encryption as en
import decryption as de

# Main class responsible for running the encryption and decryption processes.
class Main:

    def __init__(self):
        self.random_key=[]
        self.letter_dict={0:'A',1:'B',2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                          8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 
                          15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V',
                          22:'W', 23:'X', 24:'Y', 25:'Z' }
        
# Generate a random key for encryption.

    def generate_random_key(self,length):
        for i in range (length):
            self.random_num=random.randrange(26)
            self.random_key.append(self.random_num)
        # self.random_key = ''.join(random.randrange(26) for _ in range(length))
        return self.random_key
    
# Convert a list of numbers to letters using the letter dictionary.
    
    def convert_number_letter(self,numbers_list):
        self.letter_list=[]
        for i in numbers_list:
            self.letter=self.letter_dict[i]
            self.letter_list.append(self.letter)
        return self.letter_list

# Convert a list of letters to numbers using the letter dictionary.

    def convert_letter_number(self, letters_list):
        self.number_list=[]
        for letter in letters_list:
            for key, value in self.letter_dict.items():
                if value == letter:
                    self.number_list.append(key)
        return self.number_list


  
    

while True:
# Create an instance of the Main class for encryption and  decryption process.
    main=Main()

# Create an instance of the Encryption class for the encryption process.
    encrypt=en.Encryption()

# Get user input for plain text and generate a random key.
    plain_text=encrypt.enter_text()
    print(f'plainntext={plain_text}')

    otp_num=main.generate_random_key(len(plain_text))
    print(f'otp_num={otp_num}')

# Convert the OTP numbers to letters for display.
    otp=' '.join(main.convert_number_letter(otp_num))
    print(f'Your decryption Key is: {otp}')

# Convert plain text to numbers and calculate the initial total.
    plainText_numbers=main.convert_letter_number(plain_text)
    print(f'plainText_numbers={plainText_numbers}')

    initial_total=encrypt.initial_total(otp_num,plainText_numbers)

# Apply modulo 26 for the initial total.
    mod26=encrypt.mod26_check()
    print(f'mod26={mod26}')

# Convert the encrypted text to letters for display.
    ciphertext=main.convert_number_letter(mod26)
    print(f'Encrypted text is:{ciphertext}')

###############
# Decryption
###############

# Create an instance of the Decryption class for the decryption process.
    decrypt=de.Decryption()

# Prompt the user to input the ciphertext for decryption.
    input_cipherText=decrypt.enter_cipherText()
    print(f'you have entered {input_cipherText}')

# Prompt the user to input the decryption key (OTP).
    input_otp=decrypt.otp()
    print(f'your decription key is:{input_otp}')

# Convert the ciphertext letters to numbers using the letter-to-number mapping.
    cipherTextNum=main.convert_letter_number(input_cipherText)
    print(f'ciphernumbers:{cipherTextNum}')

# Convert the decryption key (OTP) letters to numbers using the letter-to-number mapping.
    otpNum=main.convert_letter_number(input_otp)
    print(f'otpNum={otpNum}')

# Calculate the total in mod26 for decryption by subtracting OTP numbers from ciphertext numbers.
    Total=decrypt.total_calc(cipherTextNum, otpNum)
    print(f'Total={Total}')

# Convert the decrypted numbers back to letters and display the plaintext.
    plainText=main.convert_number_letter(Total)
    print(f'your Plain Text is:{plainText}')

    print('***************************************************')
























