"""
Created on Fri Jun 24 12:58:19 2022

@author: Yassin Hassan
"""
import tkinter as tk
from functools import partial


window = tk.Tk()
window.title("Match the Manager with the Campus")
window.geometry("350x400")
window.resizable(False, False)


firstlbl = tk.Label(window,text = "Academic Manager")
firstlbl.place(x=50,y=20)  
secondlbl = tk.Label(window,text = "Campus")
secondlbl.place(x=230,y=20)  

manager = tk.StringVar()
mListbox = tk.Listbox(window,exportselection=0)
mListbox.place(x=30,y=40)

campus = tk.StringVar()
cListbox = tk.Listbox(window,exportselection=0)
cListbox.place(x=210,y=40)  

dict_pc = { "Rafiq Manan":"Nelson Mandela",
            "Tess Biscombe":"Cape Town Claremont",
            "Annemie Parkin":"Cape Town Tygervalley",
            "Claris Mhike":"Midrand",
            "Tendai Muzanenham":"Pretoria",
            "Anri Pienaar":"Potchefstroom",
            "Lance Krasner":"Bedfordview",
            "Kyle Knickelbein":"East London",
            "Olika Saikoolal":"Durban",
            "Karin Soderlund":"Mbombela" " and " "Bloemfontein"}

person_ls = []
campus_ls = []

for key in dict_pc:
    person_ls.append(key)
    campus_ls.append(dict_pc[key])


person_ls.sort()
campus_ls.sort()

for itemp in person_ls:
    mListbox.insert(tk.END, '{}'.format(itemp))

for itemc in campus_ls:
    cListbox.insert(tk.END, '{}'.format(itemc))



def validatedata():
    person = ""
    campus = ""
    for i in mListbox.curselection():
        person = mListbox.get(i)
        for i in cListbox.curselection():
            campus = cListbox.get(i)
        if str(dict_pc[person]) == str(campus):
            res_lbl.config(text = "CORRECT")
        else:
            res_lbl.config(text = "INCORRECT")


validatedata = partial(validatedata)

ans_lbl = tk.Label(window,text = "Answer: ")
ans_lbl.place(x=130,y=290)
res_lbl = tk.Label(window,text = "")
res_lbl.place(x=210,y=290)
btn = tk.Button(window, text = "Determine if Match is Correct",command=validatedata)
btn.place(x=110,y=240)
 
window.mainloop()