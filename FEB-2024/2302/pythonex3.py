import os
import platform
import  stat
import time
import re
from collections import Counter

def function1():
    # get os name, info, current directory
    #get list of file in this dir
    try:
        print("OS name: ", platform.system()) #return Window
        print("OS info: ", platform.uname()) #return tuple contain os infomation
        print("current directory :", os.getcwd()) #return current directory
        print("List file and folder in this path: ",os.listdir()) 
    except Exception:
        print("error: ",str(Exception))

def function2(path):
    #show up size, permission, owner, device, time info of a path
    try:
        info = os.stat(path) #get all info from path
        print("size :",info.st_size)
        print("permission :",stat.filemode(info.st_mode))
        print("owner: ",info.st_uid)
        print("device :",info.st_dev)
        print("Time first create ", time.ctime(info.st_ctime))
        print("Last mod time: ", time.ctime(info.st_mtime))
        print("Last accessed time: ", time.ctime(info.st_atime))
    except Exception:
        print("error:", str(Exception))

def function3(path):
    try:
        with open(path, 'r') as file:
            text = file.read() #read file and store to text
        uuid_pattern = r'UUID="ECUC:([\w-]+)"' #[\w-] means get everything with '-' parameter, then + means get unlimitted word until reach " in the last word
        """
The letter 'r' before a string in Python represents a "raw" string. This means that escape characters, such as \n for a new line or \t for a tab, will not be processed by Python as special characters but rather as regular characters.
In the case of regular expressions, using raw strings is very useful because regular expressions often use many backslash characters (). 
If you don't use raw strings, you will have to double the backslash characters (e.g., \) for Python to understand it as a literal backslash character, not an escape character. This can be confusing and hard to read. For example, the raw string r'\n' will be interpreted by Python as two characters: one backslash and one 'n', whereas the non-raw string '\n' will be interpreted by Python as a newline character.
        """
        replaced_text = re.sub(uuid_pattern, r'UUID="ECUC:8a8a8a8a-4b4b-4c4c-4d4d-12e12e12e12e"', text, flags=re.IGNORECASE)
        with open('replaced_text.xml', 'w') as output_file:
            output_file.write(replaced_text)
    except Exception :
        print("error: ", str(Exception))
    """
Function 3 working principle: it reads the file and stores it into a variable called text. 
Then, it constructs a UUID pattern as a raw string to be used in re.sub for comparison and replacement, and saves the result into replaced_text. 
Next, it creates a file named replaced_text.xml (the open function will create a new one if it doesn't exist yet) and assigns it a handle named output_file. 
Finally, it writes the replaced_text into the file.
    """

def function4(path):
    try:
        with open(path, 'r') as file:
            text = file.read()
        #tạo list lưu kết quả sau khi findall
        word_list = re.findall(r'</([\w-]+)>',text)
        word_count = Counter(word_list)
        with open('word_count.txt','w') as output_file:
            for word, count in word_count.items():
                output_file.write(f"Key: {word}, Value(Count): {count}\n")
            

    except Exception:
        print("error :",str(Exception))
    """
Function 4 working principle: it reads the file and stores it into a variable called text. 
Then, it creates a word list and uses Counter to count and store the word frequencies as a dictionary. 
Next, it creates a file named word_count and iterates through the dictionary to append the counts to the file.
    """

function1()
function2(os.getcwd())
function3(r'input_excer3.xml')
function4(r'input_excer3.xml')
