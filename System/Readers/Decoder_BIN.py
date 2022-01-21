import base64

# sl = single line
def read_BIN_sl(File, line):


    File_get_data = open(File, "r")
    File_read_data = File_get_data.readlines()[line]
    File_bytes = File_read_data.encode("ascii")
    Data_bytes = base64.b64decode(File_bytes)
    Data = Data_bytes.decode("ascii")

    # close for open
    File_get_data.close()

    print(File)
    print(Data)
