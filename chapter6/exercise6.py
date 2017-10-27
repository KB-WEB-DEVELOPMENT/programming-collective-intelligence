# EXERCISE 6: - add the following lines to the function entryfeatures(entry) - p 137

import re

longwords=[s.lower( ) for s in splitter.split(entry['summary']) if len(s)>2]

for i in range(len(longwords)):
    if len(longwords[i])>40:
       f['LONG WORD(S)']= longwords[i]
       f['WORD TOO LONG']=1

# https://stackoverflow.com/questions/11786997/list-how-to-find-number-of-times-an-item-appears for Python 2.7+
repeated_words_list={}
words_some_repeated=[s.lower( ) for s in splitter.split(entry['summary']) if len(s)>2 and len(s)<20]
set_words_some_repeated=set(words_some_repeated)

for i in set_words_some_repeated:
   repeated_words_list[i]= words_some_repeated.count(i)

for word,word_use in repeated_words_list.items():
   if word_use>10:   
      f['WORD(S) USED EXCSSIVELY']= word
      f['EXCESSIVE USE OF WORDS']=1  
	
return f
