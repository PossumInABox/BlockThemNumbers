import sys
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

vcard_text_1 = """BEGIN:VCARD
VERSION:3.0
N:Center;Call;;;
FN:Call Center
ORG:Huso AG;"""

vcard_text_2 = """UID:54bf498910eb6b1
X-ABUID:43BBB008-34F6-4A69-B39D-72EB660829F2:ABPerson
END:VCARD"""

if (len(sys.argv) < 3):
    print(f"{bcolors.FAIL}Usage:{bcolors.ENDC} arg1: path to file containg numbers, 1 per line | arg2: path to output file, .vcf file extension is added automatically if missing | Optional value for arg2: PIPE : turns of all other output and prints content of vcard file to StdOut")
    exit()

filepath_in = sys.argv[1]
filepath_out = sys.argv[2]

pipe = False
if filepath_out == 'PIPE':
    pipe = True

# check for file extension
if (not filepath_out.endswith(".vcf") and not pipe):
    filepath_out += ".vcf"
    print(f"{bcolors.WARNING}Filename fixed:{bcolors.ENDC} {sys.argv[2]} {bcolors.WARNING}->{bcolors.ENDC} {filepath_out}")

f_in = open(filepath_in, "r")
phone_numbers = list(set(f_in.read().split("\n")))
f_in.close()

tel_list = []
for number in phone_numbers:
    number = number.replace(" ", "")
    if re.search(r"\+41[1-9]{2}[0-9]{7}", number) != None:
        tel_list.append("TEL;type=WORK;type=VOICE;type=pref:" + number)
    elif (number == ""):
        #do nothing, say nothing, only dreams now
        0
    else:
        if not pipe:
            print(f"{bcolors.WARNING}Problem with number:{bcolors.ENDC} {number} -> wrong format, use i.e. +41781234567 (spaces will be removed automatically)")

vcard_text = vcard_text_1 + "\n" + "\n".join(tel_list) + "\n" + vcard_text_2

f_out = open(filepath_out, "w")
f_out.write(vcard_text)
f_out.close()
if not pipe:
    print(f"{bcolors.OKGREEN}Success:{bcolors.ENDC} {len(tel_list)} Phone numbers written to {filepath_out}")
else:
    print(vcard_text)
