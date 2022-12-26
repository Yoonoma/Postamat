import os

f_no = open("no_scren.txt", "r")
f_yes = open("yes_scren.txt", "r")

lst_no = [line.strip() for line in f_no]
lst_yes = [line.strip() for line in f_yes]

for i in lst_yes:
    if i not in lst_no:
        print(i)