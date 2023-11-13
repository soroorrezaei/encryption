

# Encryption class responsible for the encryption process.
class Encryption:
    
    """
        Encryption class responsible for the encryption process.

        This class provides methods to encrypt plain text using a one-time pad (OTP) encryption technique.
        It includes the following methods:

        - enter_text: Get user input for plain text.
        - initial_total: Calculate the initial total by adding OTP numbers and plain text numbers.
        - mod26_check: Apply modulo 26 for numbers greater than 25 to ensure they stay within the range [0, 25].

        Usage:
        - Call the methods of this class to perform text encryption.

        Note:
        - The letter-to-number mapping is based on the English alphabet (A-Z).
        - The code is designed for one-time pad (OTP) encryption.
        """
    
        
# Get user input for plain text.
    def enter_text(self):
        """
        Get user input for plain text.

        This method prompts the user to input plain text, ensuring that only letters are accepted.

        Returns:
        - The plain text (letters only) entered by the user.
        """

        while True:
            input_text = input("Enter some text (letters only):\n ").upper()
            plain_text=input_text.replace(" ", "")
            if plain_text.isalpha() :
                break
            else:
                print("Input contains numbers or symbols. Please enter letters only.")

        return plain_text
    
 # Calculate the initial total by adding OTP numbers and plain text numbers.
    def initial_total(self, otp_num, plainText_numbers):
        """
        Calculate the initial total by adding OTP numbers and plain text numbers.

        This method takes a list of OTP numbers and a list of plain text numbers and calculates
        the initial total by adding corresponding elements together.

        Args:
        - otp_num: List of OTP numbers.
        - plainText_numbers: List of plain text numbers.

        Returns:
        - A list containing the initial total calculated by adding OTP numbers and plain text numbers.
        """
        self.init_total=[]

        for i in range(len(otp_num)) :
            total=otp_num[i]+ plainText_numbers[i]
            self.init_total.append(total)
        print(f'initial_total={self.init_total}')
    
# Apply modulo 26 for numbers greater than 25.
    def mod26_check(self):
        """
        Apply modulo 26 for numbers greater than 25.

        This method takes the initial total and applies modulo 26 to each element to ensure that
        the numbers stay within the range [0, 25].

        Returns:
        - A list containing the initial total after applying modulo 26.
        """
        self.mod26=[]

        for i in self.init_total:
            if i>25:
                i %= 26
            self.mod26.append(i)
            
        return self.mod26

