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
        print(self.random_key)
        return self.random_key
    
    def convert_number_letter(self,numbers):
        self.letter_list=[]
        for i in numbers:
            self.letter=self.letter_dict[i]
            print(self.letter)
            self.letter_list.append(self.letter)
        return self.letter_list
    
    def convert_letter_number(self, letters):
        self.number_list=[]
        for letter in letters:
            for key, value in self.letter_dict.items():
                if value == letter:
                    self.number_list.append(key)
        print(f'self.number_list = {self.number_list}')
        return self.number_list


  
    



x=en.Encryption()
y=Main()
plain_text=x.enter_text()
print(f'pl={plain_text}')

random_key=y.generate_random_key(len(plain_text))

otp=' '.join(y.convert_number_letter(random_key))
print(otp)

number_list=y.convert_letter_number(plain_text)

initial_total=x.initial_total(random_key,number_list)
print(initial_total)

mod26=x.mod26_check(initial_total)
print(f'x.mod26222={mod26}')

ciphertext=y.convert_number_letter(mod26)
print(f'Encrypted text is:{ciphertext}')

###############
# Decryption
###############
z=de.Decryption()




















