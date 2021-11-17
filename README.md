# BlockThemNumbers
Turn a list of phone numbers into a vCard .vcf contact file to block all numbers at once

## Usage  
### List of phone numbers
Phone numbers must be in a pure text file, one number per line. Duplicates are eliminated within the script, as well as spaces in the number itself.

### Calling the script  
Call the script as follows:
```bash
python3 btn.py listofnumbers.txt outfile.vcf
```  
There is another option for the second argument to turn off all other output and print the .vcf file content to console
```bash
python3 btn.py listofnumbers.txt PIPE
```  

## Please Note
As of now, the number format is set to accept Swiss phone numbers (+41 12 234 56 78), which is checked by a regular expression.
Feel free to change this to your needs.
