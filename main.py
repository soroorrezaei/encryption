import random

class Encryption:

    def __init__(self):
        self.letter_dict={0:'A',1:'B',2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                          8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 
                          15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V',
                          22:'W', 23:'X', 24:'Y', 25:'Z' }
        self.random_key=[]
        self.letter_list=[]
        self.number_list=[]
        



    
    def enter_text(self):

        while True:
            self.input_text = input("Enter some text (letters only):\n ").upper()
            self.plain_text=self.input_text.replace(" ", "")
            if self.plain_text.isalpha() :
                break
            else:
                print("Input contains numbers or symbols. Please enter letters only.")

        print("You entered:", self.input_text)
        return self.plain_text


    def generate_random_key(self,length):
        for i in range (length):
            self.random_num=random.randrange(26)
            self.random_key.append(self.random_num)
        # self.random_key = ''.join(random.randrange(26) for _ in range(length))
        print(self.random_key)
        return self.random_key
    
    def convert_number_letter(self,numbers):
        for i in numbers:
            letter=self.letter_dict[i]
            print(letter)
            self.letter_list.append(letter)
        return self.letter_list
    

    def convert_letter_number(self,letter):
        for i in letter:        
            for value in self.letter_dict.items():
                if value == i:
                    self.number_list.append(value)
                return self.number_list



    def initial_total(self):
        print(self.random_key)
        print(self.number_list)

        for i in self.random_key:
            for j in self.number_list:
                ini_total=i+j
        return ini_total
            



x=Encryption()
plain_text=x.enter_text()

random_key=x.generate_random_key(len(plain_text))

otp=' '.join(x.convert_number_letter(random_key))
print(otp)

number_list=x.convert_letter_number(plain_text)
initial_total=x.initial_total()
print(initial_total)
















