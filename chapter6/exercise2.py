# EXERCISE 2: 
# Pr(Document) - Probability that given a randomly selected category,
#                the document in question has a features count
#                greater than 0 for that category.
# Pr(Document) = (A)/(B) where:
# (A): Total number of categories whose features count is > 0 for that document
# (B): Total number of categories alltogether

def docprob(self,f,cat)
# total number of categories alltogether
  denominator=len(categories(self))
# total number of categories whose features count >  0 for that document
  categories_count=0
    if f in self.fc and cat in self.fc[f]: 
      categories_count+=1
      numerator=categories_count
	
  return float(numerator/denominator)
