

class Encryption:

    def __init__(self):
        self.init_total=[]
        self.mod26=[]

    
        
    def enter_text(self):

        while True:
            self.input_text = input("Enter some text (letters only):\n ").upper()
            self.plain_text=self.input_text.replace(" ", "")
            if self.plain_text.isalpha() :
                break
            else:
                print("Input contains numbers or symbols. Please enter letters only.")

        return self.plain_text
    
        
    def initial_total(self, otp_num, plainText_numbers):

        for i in range(len(otp_num)) :
            self.total=otp_num[i]+ plainText_numbers[i]
            self.init_total.append(self.total)
    
    def mod26_check(self):
        for i in self.init_total:
            if i>25:
                i %= 26
                self.mod26.append(i)
            else:
                self.mod26.append(i)
        return self.mod26

