#Enhanced vowel from input string into uppercase convertion
#using dictionary and one-line code for terminal execution
import sys
vowel = {'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}

print "".join([vowel[c] if c in vowel else c for c in sys.argv[1]])