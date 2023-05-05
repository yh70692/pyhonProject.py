"""
Created on Fri Jun 24 07:48:40 2022

@author: Yassin
"""

lst=[]

def main():
    lst = open("Colors.txt", "r")

    def Input():
        search = input("Enter a letter to search : ")
        return search[0]
    def SearchColors(letter):
        selectedColor =[]
        for color in lst:
            if color[0] == letter:
                print(color)
                selectedColor.append(color)
    letter = Input()
    SearchColors(letter)




main()