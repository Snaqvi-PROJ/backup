#!/home/saif/Documents/new_env/bin/python

def search4vowels(word):
  """ This is a test function """
  vowels = set('aeiou')
  return vowels.intersection(set(word))


def search4vowelswithdefaultargs(word='dudi'):
  """ This is a test function which search with default args """
  vowels = set('aeiou')
  return vowels.intersection(set(word))

