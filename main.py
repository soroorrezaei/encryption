import random
import encryption as en
import decryption as de


class Main:

    def __init__(self):
        self.random_key=[]
        self.letter_dict={0:'A',1:'B',2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                          8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 
                          15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V',
                          22:'W', 23:'X', 24:'Y', 25:'Z' }
        

    def generate_random_key(self,length):
        for i in range (length):
            self.random_num=random.randrange(26)
            self.random_key.append(self.random_num)
        # self.random_key = ''.join(random.randrange(26) for _ in range(length))
        return self.random_key
    
    def convert_number_letter(self,numbers_list):
        self.letter_list=[]
        for i in numbers_list:
            self.letter=self.letter_dict[i]
            self.letter_list.append(self.letter)
        return self.letter_list
    
    def convert_letter_number(self, letters_list):
        self.number_list=[]
        for letter in letters_list:
            for key, value in self.letter_dict.items():
                if value == letter:
                    self.number_list.append(key)
        return self.number_list


  
    


main=Main()
encrypt=en.Encryption()

plain_text=encrypt.enter_text()

otp_num=main.generate_random_key(len(plain_text))

otp=' '.join(main.convert_number_letter(otp_num))
print(f'Your decryption Key is: {otp}')

plainText_numbers=main.convert_letter_number(plain_text)

initial_total=encrypt.initial_total(otp_num,plainText_numbers)

mod26=encrypt.mod26_check()

ciphertext=main.convert_number_letter(mod26)
print(f'Encrypted text is:{ciphertext}')

###############
# Decryption
###############


decrypt=de.Decryption()

input_cipherText=decrypt.enter_cipherText()

input_otp=decrypt.otp()

cipherTextNum=main.convert_letter_number(input_cipherText)

otpNum=main.convert_letter_number(input_otp)

initial_total=decrypt.initial_total(cipherTextNum, otpNum)

mod26_dec=decrypt.mod26_check()

plainText=main.convert_number_letter(mod26_dec)
print(f'your Plain Text is:{plainText}')
























