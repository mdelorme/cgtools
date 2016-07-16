# Name of the result file
out_filename = 'my_merged_file.py'

# Files to be included in order
files = ['file_1.py', 'file_2.py']

# Header and footer of the merged file
header = '''import sys
import math

'''
footer = ''' '''

# Token : includes everything in the filed listed above that lie between
#         two tokens. The program works as a state machine, it starts
#         copying when it finds a (stripped) line == token, and stops
#         when it finds a second one (or ends the file).
#         It is possible to activate copy multiple times if you want to omit
#         part of the code
token = '##/INCLUDE\##'


# The script part ... should be self explanatory
f_out = open(out_filename, 'w')
f_out.write(header)

for f in files:
    f_in = open(f, 'r')

    copying = False
    for l in f_in:
        if not copying and l.strip() != token:
            continue
        elif l.strip() == token:
            copying = not copying
        else:
            f_out.write(l)
    f_in.close()

f_out.write(footer)
f_out.close()
