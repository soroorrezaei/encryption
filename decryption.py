
class Decryption:

    def __init__(self):
        self.init_total=[]
        self.mod26=[]

    
    def enter_cipherText(self):

        while True:
            self.input_cipherText = input("Enter your chipherText:\n ").upper()
            if self.input_cipherText.isalpha() :
                break
            else:
                print("Input contains space, numbers or symbols. Please enter letters only.")

        return self.input_cipherText
    
    def otp(self):

        while True:
            self.input_otp = input("Enter your decryption key (OTP):\n ").upper()
            if self.input_otp.isalpha() :
                break
            else:
                print("Input contains space, numbers or symbols. Please enter letters only.")

        return self.input_otp 
        
    def initial_total(self,cipherText_num,otp_num ):

        for i in range(len(otp_num)) :
            self.total=otp_num[i]- cipherText_num[i]
            self.init_total.append(self.total)
        return self.init_total

    def mod26_check(self):
        for i in self.init_total:
            if i<0:
                i += 26
                self.mod26.append(i)
            else:
                self.mod26.append(i)
        print(f'x.mod26={self.mod26}')
        return self.mod26


