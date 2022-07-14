file_path = "/RISHI/H2K/FileIO/demofile.txt"
'''
open - mode
r - read - default
w - write - wipe out existing content and write new one
a - append - append the new text in original
x - create - file if not exists will be created - otherwise error

content type modes
t - text - default
b - binary

'''
file = open(file_path, 'rt')
# Fixed Length File Formats - file.read(30)
# Mainframes - GDG, Extracts
# print(file.read(30))
# print(file.read(30))
for eachLine in file:
    print(eachLine)
file.close()