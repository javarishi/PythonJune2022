file_path_a = "/RISHI/H2K/FileIO/demofile_a.txt"
file_path_w = "/RISHI/H2K/FileIO/demofile_w.txt"
file_path_x = "/RISHI/H2K/FileIO/demofile_x.txt"
afile = open(file_path_a, 'at')
wfile = open(file_path_w, 'w')
xfile = open(file_path_x, 'x')
for line in range(1, 10):
    afile.write("Append File - This is Line {}".format(line))
    afile.write("\n")
    wfile.write("Write File - This is Line {}".format(line))
    wfile.write("\n")
afile.close()
wfile.close()
xfile.close()