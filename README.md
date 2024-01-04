# fuzzy-matching-workbook
This repository hosts notes on simple tools and concepts for streamlining the use of fuzzy logic in data cleaning and wrangling workflows. While R contains packages such as stringdist and especially fuzzyjoin that allow for data wrangling operations (e.g. joins) and mass comparisions with string distance matrices, such packages do not seem to have some other algorithms such as Sørensen Dice and Metaphone. At the same time, Python's fuzzywuzzy / TheFuzz package, while featureful, appears to lack many of the algorithms that are available in R, including Jaccard coefficient and Jaro-Winkler. The greatest variety of approaches seems to come from Python's jellyfish package, so, I have opted to replicate for Python some of the functionalities that are rather circumscribed to R, with the benefit of a greater availability of choice in algorithms. The intention is to update this repo with relevant solutions to data wrangling obstacles.

## Content
The following code and ideas are being developed, in varying states of development:
* A PyShiny application, or selections of code closely related to it, that allows a user to review matches and interactively approve or skip them, with feedback in the form of an updating dataframe of matches that excludes what has already been assigned. It should support comparisions grouped by some set of variables / columns. The motivation for supporting grouped operations stems from the need to match location names which are distinguished by the names of administrative levels (regions, provinces, states, etc.) above them. For the moment, the grouping ability requires that the variables that the data is grouped are exactly correct, rather than being another layer of fuzzy logic work.
  
* A function to match columns from two different datasets, with one column being designated as requiring matches (held constant without dropping rows), and the other column designated as potential matches (which may contain values that will never be matched, as the function is oriented around assigning one column to the other, but not necessarily the reverse. The ability to group by relevant variables should be there, even with there being two datasets involved.
  
* The above is supported by a limited expansion of jellyfish fuzzy logic functions to produce a list of scores comparing two lists of strings pair-wise.


