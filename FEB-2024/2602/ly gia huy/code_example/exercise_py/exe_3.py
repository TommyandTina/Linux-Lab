# 1. Function 1: get the name of the operating system (Platform independent), information of current operating system, 
# current working directory, print files and directories in the current directory and raises error in the case of invalid or inaccessible file names and paths.
# 2. Function 2: get the size, permissions, owner, device, created, last modified and last accessed date time of a specified path
# 3. Function 3: Using RegEx Module to replace all values of UUID to "ECUC:8a8a8a8a-4b4b-4c4c-4d4d-12e12e12e12e"
# 4. Function 4:  count the frequency of words in right of bracket '<; or '</' of input file then write the result in a new text file. 
# Example: <REFINED-MODULE-DEF-REF DEST="ECUC-MODULE-DEF">/AUTOSAR/EcucDefs/Can</REFINED-MODULE-DEF-REF>
# The word is "REFINED-MODULE-DEF-REF"
# 5. Click to icon to download input file

import os
import platform
import pwd
import grp
import time
import re
from collections import Counter

def os_infor():
    print("OS system:", platform.system())
    print("OS information:", platform.platform())
    print("Current working directory:", os.getcwd())

    try:
        print("\nFiles and Directories in", os.getcwd(), ":")
        for item in os.listdir('.'):
            print(item)
    except Exception as e:
        print("Error accessing or listing directory:", e)
        
def path_details(path):
    stats = os.stat(path)
    print("Size:", stats.st_size, "bytes")
    print("Permissions:", oct(stats.st_mode)[-3:])
    print("Owner:", pwd.getpwuid(stats.st_uid).pw_name)
    print("Group:", grp.getgrgid(stats.st_gid).gr_name)
    print("Device:", stats.st_dev)
    print("Created:", time.ctime(stats.st_ctime))
    print("Last modified:", time.ctime(stats.st_mtime))
    print("Last accessed:", time.ctime(stats.st_atime))

def replace_uuids(input_text):
    uuid_pattern = r'\b[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}\b'
    replaced_text = re.sub(uuid_pattern, "ECUC:8a8a8a8a-4b4b-4c4c-4d4d-12e12e12e12e", input_text)
    return replaced_text


def count_words(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Updated pattern to include hyphen-connected words
    words = re.findall(r'<\/?([-\w]+)', content)
    word_count = Counter(words)

    with open(output_file, 'w') as out:
        for word, count in word_count.items():
            out.write(f"{word}: {count}\n")

print(".....OS Information and Directory Listing.....")
os_infor() 
print(".....File/Directory Details.....")
path_details("/home/huy.ly-gia/LYGIAHUY_BV/exercise_lgh/example_code/example.py")

print(".....Replace UUIDs with a Specific UUID Using RegEx.....")
print(replace_uuids("8a8a8a8a-4b4b-4c4c-4d4d-12e12e12e12e"))

print(".....Count Frequency of Words.....")
count_words("./read_e3.txt","./write_e3.txt")
