# EXERCISE 1

# function to remove all unecessary whitespaces, tabs, newlines and other "whitespace-like" characters
# and any trailing whitespaces

import re

def separatewords(self, text):
  re.sub('\s+', ' ', text).strip()
  return text
