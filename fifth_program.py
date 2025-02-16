#fifth
list=[14,15,16,-17,-18,14]
for i in list:
    if i<0:
        print(f"first negative number:{i}")
        break
    elif i==0:
        continue
    else:
        print("there is no negativity")