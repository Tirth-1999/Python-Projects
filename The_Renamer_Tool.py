import os
st = input("Please provide the file directory to search for ?? ")
ext = input("Which extension you want to change file for ?? ")
new_name = input("starting_name (ending with number) : ")
starting_index = int(input("please enter the starting index : "))
os.chdir(st)

for i in os.listdir():
    if ext in i:
        new = new_name + str(starting_index) + "." + ext
        os.rename(i, new)
        starting_index += 1

print("\nTotal file Changed: ", str(starting_index-1))
print("\nDone!! Do you want to check files ??? Y for Yes || N for No")
if (input() == 'Y'):
    os.startfile(st)
    print("Thank you !! See You Back Soon!!!")
else : 
    print("Thank you !! See You Back Soon!!!")

