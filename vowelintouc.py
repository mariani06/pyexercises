#Converting vowel from input string into uppercase
#using list to collect vowel
vowel = ['a', 'e', 'i', 'o', 'u']
inp = raw_input('Type your input here: ')
ch = list(inp)

for c in ch:
 if c in vowel:
  ch[ch.index(c)] = c.upper()
st = "".join(ch)
print(st)