import os

for filename in os.listdir("."):
    if filename.startswith("BSP") and filename.endswith(".log"):
        splited_parts=filename.split("_")
        splited_parts = [each_part.replace("USB3F","USB2F") for each_part in splited_parts]
        new_filename = "_".join(splited_parts)
        os.rename(os.path.join(".",filename),os.path.join(".",new_filename))
        print(new_filename)