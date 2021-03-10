#!/home/saif/Documents/new_env/bin/python

my_name = "My Name is saof naqvi"
vowel = ['a', 'e', 'i', 'o', 'u']

"""
i = 0
for vowel_word in vowel:
  i = i + 1
  if vowel_word in my_name:
    print vowel_word

print i
"""

"""
found = []

for character in my_name:
  if character in vowel:
    if character not in found:
      found.append(character)

for found_vowel in found:
  print found_vowel
"""

"""
a = 6
while(1):
  a = a - 1
  print a
  if a == 0:
    exit(0)
  else:
   continue
"""

"""
name = "ali saif naqvi"

let = list(name)

for char in let[:3]:
  print '\t', char

for char in let[4:8]:
  print '\t'*2, char

for char in let[9:]:
  print '\t'*3, char
"""

"""
name = "this is a sentence that needs to be processed accordingly : ali saif naqvi"
let = list(name)

i = 1
for char in let:
  print '\t'*i, char
  if char == ' ':
    i = i + 1
  else:
    continue
"""

test_dict = { 
  "name" : "saif naqvi",
  "age" : "30",
  "occupation" : "engineer",
  "hobbies" : "cinofile"
}

"""
found_dict = {}
vowel = ['a', 'e', 'i', 'o', 'u']
my_word = "my name is saif naqvi and i am an engineer and i am proud of it "

for char in my_word:
  if char in vowel:
    found_dict.setdefault(char, 0)
    found_dict[char] += 1

print found_dict
"""


