
"""
Decryption Process

This part of the program performs the decryption process using a one-time pad (OTP). It includes the following steps:

1. Create an instance of the Decryption class for decryption.
2. Prompt the user to input the ciphertext that needs to be decrypted.
3. Prompt the user to input the decryption key (OTP).
4. Convert the ciphertext letters to numbers based on a letter-to-number mapping.
5. Convert the decryption key (OTP) letters to numbers using the same mapping.
6. Calculate the initial total for decryption by subtracting OTP numbers from ciphertext numbers.
7. Apply modulo 26 for the initial total to handle negative values and ensure it stays within the range [0, 25].
8. Convert the decrypted numbers back to letters and display the plaintext.

Usage:
- Follow the prompts to input the ciphertext you wish to decrypt.
- Enter the decryption key (OTP) when prompted.

Note:
- The letter-to-number mapping is based on the English alphabet (A-Z).
- This part of the code is responsible for the decryption process.
"""

# Decryption class responsible for the decryption process.
class Decryption:

# Get user input for cipher text.
    def enter_cipherText(self):
        """
        Get user input for ciphertext.

        This method prompts the user to input ciphertext, ensuring that only letters are accepted.

        Returns:
        - The ciphertext (letters only) entered by the user.
        """
        while True:
            input_cipherText = input("Enter your chipherText:\n ").upper()
            if input_cipherText.isalpha() :
                break
            else:
                print("Input contains space, numbers or symbols. Please enter letters only.")

        return input_cipherText
    
# Get user input for the decryption key (OTP).
    def otp(self):
        """
        Get user input for the decryption key (OTP).

        This method prompts the user to input the decryption key (OTP), ensuring that only letters are accepted.

        Returns:
        - The decryption key (OTP) entered by the user.
        """
        while True:
            input_otp = input("Enter your decryption key (OTP):\n ").upper()
            if input_otp.isalpha() :
                break
            else:
                print("Input contains space, numbers or symbols. Please enter letters only.")

        return input_otp 

# Calculate the total by subtracting OTP numbers from cipher text numbers in mod26.
    def total_calc(self,cipherText_num,otp_num ):
        """
        Calculate the total by subtracting OTP numbers from ciphertext numbers with modulo 26 handling.

        This method takes a list of ciphertext numbers and a list of OTP numbers and calculates
        the total by subtracting OTP numbers from corresponding ciphertext numbers, handling modulo 26 for negative values.

        Args:
        - cipherText_num: List of ciphertext numbers.
        - otp_num: List of OTP numbers.

        Returns:
        - A list containing the total calculated by subtracting OTP numbers from ciphertext numbers.
        """
        total=[]

        for i in range(len(otp_num)) :
            calc= cipherText_num[i]-otp_num[i]
            if calc<0:
                calc+=26
            total.append(calc)
        return total
