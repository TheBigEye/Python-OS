import base64

# sl = single line
def read_BIN_sl(File, line):

    File_get_data = open(File, "r")
    File_read_data = File_get_data.readlines()[line]
    File_bytes = File_read_data.encode("ascii")
    Data_bytes = base64.b64decode(File_bytes)
    Data = Data_bytes.decode("ascii")

    print(File)
    print(Data)


# Test
read_BIN_sl("Disk\Disk", 0)
