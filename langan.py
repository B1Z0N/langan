import itertools                                                                 #analyzes an entropy of the language by its alphabet and a piece of text
from math import log                                                             #
                                                                                 #
clear_str_const = '#$%*+/<=>@^_~âœ˜‘’“”…€™\n!\'"(),-.0123456789:;?'             #
                                                                                 #
class Langan:                                                                    #
    def __init__(self, alpha, length = -1, clear = clear_str_const):             #
        self.entropy = 0                                                         #
        self.dict = {}                                                           #
        self.alphalist = list(set(clear_str(alpha, clear)))                      #
        print(self.alphalist)                                                    #
        self.len = length                                                        #
                                                                                 #
    def print(self):                                                             #
        print("Entropy:" + str(self.entropy))                                    #
                                                                                 #print("Dictionary:" + str(self.dict))
        print("Alphabet:" + str(self.alphalist))                                 #
        print("Length:" + str(self.len))                                         #
                                                                                 #
    def get_entropy(self, sample):                                               #
        self.dict = {}                                                           #
        for i in range(self.len - 1, len(sample)):                               #
            val = sample[i - self.len + 1 : i + 1]                               #
            if val in self.dict:                                                 #
                self.dict[val] += 1                                              #
            else:                                                                #
                self.dict.update({val : 1})                                      #
                                                                                 #
                                                                                 #
        amount = len(sample)                                                     #whole amount of variants
                                                                                 #
        self.entropy = 0                                                         #
        for i in self.dict:                                                      #
            p_i = self.dict[i] / amount                                          #
            self.entropy += p_i * log(1 / p_i, 2)                                #
        self.entropy /= self.len                                                 #
                                                                                 #
        return self.entropy                                                      #
                                                                                 #
    def eval_entropy(self, sample, start_len, accuracy = 0.1):                   #with given accuracy
        self.len = start_len                                                     #
        prev = self.get_entropy(sample)                                          #
        self.len += 1                                                            #
        cur = self.get_entropy(sample)                                           #
        while abs(prev - cur) > accuracy:                                        #
            prev = cur                                                           #
            self.len += 1                                                        #
            cur = self.get_entropy(sample)                                       #
                                                                                 #
        return self.entropy                                                      #
                                                                                 #
def clear_str(sample_str, symbol_str):                                           #
    for i in symbol_str:                                                         #
        sample_str = sample_str.replace(i,'')                                    #
                                                                                 #
    return sample_str.lower()                                                    #
                                                                                 #
def read_file(name, clear = clear_str_const):                                    #
    try:                                                                         #
        with open(name) as text:                                                 #
            text_str = ''                                                        #
            for line in text:                                                    #
                text_str += line                                                 #all in one str
    except IOError as ioerr2:                                                    #
        print("Error:" + str(ioerr2))                                            #
                                                                                 #
    return(text_str)                                                             #
                                                                                 #
lang = Langan(read_file('sheakspear'))                                           #may use alphabet or sheakspear
lang.eval_entropy(clear_str(read_file('sheakspear'), clear_str_const), 1, 0.1)   #it will take an alphabet for you
lang.print()                                                                     #
