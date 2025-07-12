#---------------------------FILE NOT FOUND
#"""
#This error is due to a file not existing in the location or at all
#"""
#with open("a_file.txt") as file:
#    file.read

#try:
#    file = open("day-30/a_file.txt")
#    a_dictionary = {"key": "value"}
#    print(a_dictionary["key"])
#except FileNotFoundError:
#    file = open("day-30/a_file.txt", "w")
#    file.write("Something")
#except KeyError as error_message:
#    print(f"The key {error_message} does not exist")
#else:
#    content = file.read()
#    print(content)
#finally:
#    file.close()
#    print("File was close. ")

#try:
#    file = open("day-30/a_file.txt")
#    a_dictionary = {"key": "value"}
#    print(a_dictionary["key"])
#except FileNotFoundError:
#    file = open("day-30/a_file.txt", "w")
#    file.write("Something")
#except KeyError as error_message:
#    print(f"The key {error_message} does not exist")
#else:
#    content = file.read()
#    print(content)
#finally:
#    raise TypeError("This is an error that i made up")


#---------------------------Raise
#allows to raise your own exceptions


#---------------------------KEYERROR
#"""
#This error is due to a key value not existing
#"""
##a_dictionary = {"key": "value"}
##value = a_dictionary["non_existent_key"]
#
##----------------------------INDEX ERROR
#"""
#This is an error due to using an index that doesn't exist
#"""
##fruit_list = ["Apple", "Banana", "Pear"]
##fruit = fruit_list[3]
#
##----------------------------TYPE ERROR
#"""
#This error is due to the incorrect type being used
#"""
#text = 'abc'
#print(text + 1)




