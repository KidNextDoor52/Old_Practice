#file = open(r"\Users\mccra\OneDrive\Documents\GitHub\Old_Practice\day 24\my_file.txt")
#contents = file.read()
#print(contents)
#file.close()
""" This is another easy way of doing this without the need of having to close the file and/or forgetting 
and using unneccessary resources from your computer"""
#with open(r"\Users\mccra\OneDrive\Documents\GitHub\Old_Practice\day 24\my_file.txt") as file:
#    contents = file.read()
#    print(contents)
#with open(r"\Users\mccra\OneDrive\Documents\GitHub\Old_Practice\day 24\my_file.txt", mode="w+") as file:
#    file.write("New text.")
#    file.seek(0)
#    contents = file.read()
#    print(contents)
import os




with open(r"\Users\mccra\OneDrive\Documents\GitHub\Old_Practice\day-24\my_file.txt", mode="a") as file:
    file.write("\nLEts keep going")

"""
This is the simplified way of using variables to get the current script path as well as construct the path to/for the new file
"""
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "new_file.txt")


with open(file_path, mode="w") as file:
    file.write("new_txt.")
