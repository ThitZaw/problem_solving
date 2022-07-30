from posixpath import split
import string


alpha_dict = set(string.ascii_lowercase)

pangram_str = 'We promptly judged antique ivory buckles for the next prize'
if len(alpha_dict) == len(set(pangram_str.replace(' ', '').lower())):
    print('pangram')
else:
    print('not pangram')