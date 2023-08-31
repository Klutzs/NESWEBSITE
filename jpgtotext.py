import os

folder_path = os.path.dirname(os.path.abspath(__file__))
output_file = "output.txt"
output_path = os.path.join(folder_path, output_file)

# A tuple containing the image extensions we want to save
image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff", ".webp")

print("Output file path:", output_path)

with open(output_path, "w") as f:
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_extensions):
            f.write(filename + "\n")
