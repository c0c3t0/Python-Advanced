import os

dir_info = {}
files = [el for el in os.listdir() if os.path.isfile(el)]
for file in files:
    file_name, extension = os.path.splitext(file)
    if extension not in dir_info:
        dir_info[extension] = []
    dir_info[extension].append(file_name)

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', "report.txt")
with open(desktop, 'w') as output_file:
    for extension, file_names in sorted(dir_info.items()):
        output_file.write(f"{extension}")
        output_file.write("\n")
        for file_name in file_names:
            output_file.write(f"- - - {file_name}{extension}")
            output_file.write("\n")