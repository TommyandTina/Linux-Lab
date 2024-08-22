import os

# Define the directory
directory = "."

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the filename matches the pattern
    if filename.startswith("BSP") and filename.endswith(".txt"):
        # Split the filename by underscore
        parts = filename.split("_")
        # parts = [part.replace("Release BSP", "BSPv5.3.3") for part in parts]
        parts = [part.replace("E3-4D", "E3-4Dv1.1") for part in parts]
        # Remove the brackets from each part
        # parts = [part.replace("[", "").replace("]", "") for part in parts]

        # Join the parts back together with underscore
        new_filename = "_".join(parts)

        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

        # Print the new filename
        print(new_filename)

