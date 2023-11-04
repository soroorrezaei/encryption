

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

        print("You entered:", self.input_text)
        return self.plain_text
    
        
    def initial_total(self, random_key,number_list):
        print(random_key)
        print(number_list)

        for i in range(len(random_key)) :
            self.total=random_key[i]+ number_list[i]
            self.init_total.append(self.total)
        return self.init_total
    
    def mod26_check(self,initial_total):
        for i in initial_total:
            if i>25:
                i %= 26
                self.mod26.append(i)
            else:
                self.mod26.append(i)
        print(f'x.mod26={self.mod26}')
        return self.mod26

