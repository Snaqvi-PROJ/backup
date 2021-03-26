#!/home/saif/Documents/head_first_project/bin/python

def search4vowels(word):
  """ This is a test function """
  vowels = set('aeiou')
  return vowels.intersection(set(word))


def search4vowelswithdefaultargs(word='dudi'):
  """ This is a test function which search with default args """
  vowels = set('aeiou')
  return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str='aeiou') -> set:
  """Returns the set of 'letters' found in 'phrase'."""
  return set(letters).intersection(set(phrase))
