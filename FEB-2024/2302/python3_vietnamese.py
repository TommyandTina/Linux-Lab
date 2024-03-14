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
        """Chữ r trước chuỗi trong Python đại diện cho một chuỗi “raw”. 
        Điều này có nghĩa là các ký tự thoát (escape characters), như \n cho một dòng mới hoặc \t cho một tab, sẽ không được Python xử lý như là các ký tự đặc biệt mà sẽ được xem như là các ký tự thông thường.
        Trong trường hợp của biểu thức chính quy (regular expression), việc sử dụng chuỗi raw rất hữu ích vì biểu thức chính quy thường sử dụng nhiều ký tự backslash (\). 
        Nếu không dùng chuỗi raw, bạn sẽ phải ghi đúp ký tự backslash (ví dụ: \\) để Python hiểu đó là một ký tự backslash thực sự, không phải là một ký tự thoát. 
        Điều này có thể gây rối và khó đọc. Ví dụ, chuỗi raw r'\n' sẽ được Python xem như là hai ký tự: một backslash và một chữ ‘n’, trong khi chuỗi không phải raw '\n' sẽ được Python xem như là một ký tự dòng mới.
        """
        replaced_text = re.sub(uuid_pattern, r'UUID="ECUC:8a8a8a8a-4b4b-4c4c-4d4d-12e12e12e12e"', text, flags=re.IGNORECASE)
        with open('replaced_text.xml', 'w') as output_file:
            output_file.write(replaced_text)
    except Exception :
        print("error: ", str(Exception))
    """
    function 3 working priciple: read file và lưu vào text, sau đó sẽ ghi mẫu uuid dưới dạng raw để đưa vào re.sub để so sánh và thay thế rồi lưu vào replaced_text. 
    kế đến sẽ tạo 1 file replaced_text.xml (hàm open nếu chưa có sẽ tạo mới) và đặt bí danh là output_file, cuối cùng chúng ta ghi replaced_text được lưu ở trên vào file
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
        function 4 working principle: read file và lưu vào text, sau đó tạo 
        word list  -> xài counter để đếm và lưu dưới dạng lưu dưới dạng dictionary
        -> tạo file word_count và cho chạy for để thêm vào file
    """

function1()
function2(os.getcwd())
function3(r'input_excer3.xml')
function4(r'input_excer3.xml')
