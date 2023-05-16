from abc import ABC


class Abs(ABC):
    adrs=''
    def calculateFreqs(self):
        pass


class ListCount(Abs):
    def __init__(self, x):
        Abs.adrs=x
    def calculateFreqs(self):
        with open(Abs.adrs, "r") as f:
            list_1=f.read().split()
            f.close()
        letter_list = []
        for str in list_1:
            for letter in str:
                letter_list.append(letter)
        resulting_list=[]
        for letter in letter_list:
            if (letter in resulting_list):
                index = resulting_list.index(letter)
                resulting_list[index+1]+=1
            else:
                resulting_list.append(letter)
                resulting_list.append(1)
        for i in range(0,len(resulting_list),2):
            print(f"{resulting_list[i]} = {resulting_list[i+1]}")
            """print(resulting_list[i] + " = " + resulting_list[i + 1].__str__())"""



class DictCount(Abs):
    def __init__(self, x):
        Abs.adrs=x
    def calculateFreqs(self):
        with open(Abs.adrs, "r") as f:
            d={}
            file_read=f.read().split()
        for word in file_read:
            for letter in word:
                if letter in d.keys():
                    d[letter]+=1
                else:
                    d[letter]=1
        for keys,values in d.items():
            print(f"{keys} = {values}")
        f.close()
