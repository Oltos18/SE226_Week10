from abstract import *

main_list=ListCount("weirdWords.txt")
main_dict=DictCount("weirdWords.txt")

print("In list")
main_list.calculateFreqs()
print()

print("In dict")
main_dict.calculateFreqs()


