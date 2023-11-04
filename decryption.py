class Decryption:

    def __init__(self):
        self.init_total=[]
        self.mod26=[]

    
    
        
    def initial_total(self, random_key,number_list):
        print(random_key)
        print(number_list)

        for i in range(len(random_key)) :
            self.total=random_key[i]- number_list[i]
            self.init_total.append(self.total)
        return self.init_total
    

    def mod26_check(self,initial_total):
        for i in initial_total:
            if i<0:
                i += 26
                self.mod26.append(i)
            else:
                self.mod26.append(i)
        print(f'x.mod26={self.mod26}')
        return self.mod26


