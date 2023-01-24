import re
import tkinter
from tkinter import filedialog

del_switch = False
key_counter = 0
cert_counter = 0
pass_counter = 0
conf_file_mod = []

root = tkinter.Tk()
root.withdraw()

print("Welcome to Scrubber.\nPlease select a config.\n ")

file_path = filedialog.askopenfilename()
if file_path == '':
    print("Aborting open file.")
    exit(1)

print("Opening "+file_path+"\n")
#  Import conf file
with open(file_path, 'r') as reader:
    conf_file_test = reader.readline()
if 'config-version' not in conf_file_test:
    print('File not recognized as FortiGate config aborting.')
    exit(1)

with open(file_path, 'r') as reader:
    conf_file = reader.readlines()

for line in conf_file:
    if 'ENC ' in line:
        line_m = re.sub('ENC .*', 'ENC', line)
        line = line_m
        pass_counter += 1
        print(line)
    if 'END ENCRYPTED PRIVATE KEY' in line:
        del_switch = False
        key_counter += 1
    if 'END CERTIFICATE' in line:
        del_switch = False
        cert_counter += 1
    if del_switch is False:
        conf_file_mod += line
    if 'BEGIN ENCRYPTED PRIVATE KEY' in line:
        del_switch = True
    if 'BEGIN CERTIFICATE' in line:
        del_switch = True

print(key_counter)
print(pass_counter)
print(cert_counter)

write_path = (file_path.rsplit('/', 1))
file_name = write_path[-1]
name_list = file_name.split('_')
print(name_list)

name_list[2] = name_list[2][:4]+'_'+name_list[2][4:]
if 'phi' in name_list[1]:
    name_list[0] = 'PHI'
elif 'pit' in name_list[1]:
    name_list[0] = 'PIT'
name_list[1] = 'FW_Config'
name_list = '_'.join(name_list)
print(name_list)
write_path[-1] = name_list
write_path = '/'.join(write_path)
print("Saving file to: ",write_path)

with open(write_path, mode='wt', encoding='utf-8') as writer:
    for lines in conf_file_mod:
        writer.write(lines)
reader.close()
print("Done!")

 #   print(re.sub('ENC.*', 'ENC', line))
 #   print(re.sub(r"(-----BEGIN ENCRYPTED PRIVATE KEY-----)[^()]+(-----END ENCRYPTED PRIVATE KEY-----)","\n-----BEGIN ENCRYPTED PRIVATE KEY-----\n-----END ENCRYPTED PRIVATE KEY-----",text))