import os

def generate_includetext_field(file_path, base_path):
    # Tạo đường dẫn tương đối
    relative_path = os.path.relpath(file_path, base_path)
    # Tạo trường INCLUDETEXT
    includetext_field = f'{{INCLUDETEXT "{relative_path}" \* MERGEFORMAT}}'
    return includetext_field

def collect_docx_paths(folder_path):
    docx_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".docx"):
                file_path = os.path.join(root, file)
                docx_paths.append(file_path)
    return docx_paths

def main():
    folder_path = r"‪/mnt/c/Users/long.trinh-tien/Documents/Linux-Lab/"  # Thay đổi đường dẫn đến thư mục của bạn
    docx_paths = collect_docx_paths(folder_path)
    
    for docx_path in docx_paths:
        includetext_field = generate_includetext_field(docx_path, folder_path)
        print(includetext_field)

if __name__ == "__main__":
    main()
