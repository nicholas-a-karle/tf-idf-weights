#-------------------------------------------------------------------------
# AUTHOR: Nicholas Karle
# FILENAME: indexing.py
# SPECIFICATION: compute the tf-idf matrix
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math
from xml.dom.minidom import Identified

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0].split())

#Conducting stopword removal. Hint: use a set to define your stopwords.
stopWords = ["I", "She", "her", "They", "their", "and"]

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
stemming = {
    "love": "love",
    "loves": "love",
    "dog": "dog",
    "dogs": "dog",
    "cat": "cat",
    "cats": "cat"
}

#Identifying the index tf.

terms = ["love", "dog", "cat"]

tf = {"love": [0, 0, 0], "dog": [0, 0, 0], "cat": [0, 0, 0]}

for i in range(len(documents)):
    for term in documents[i]:
        if term not in stopWords:
            tf[stemming[term]][i] += 1

#DFs
df = {"love": 0, "dog": 0, "cat": 0}

for term in df:
    for fq in tf[term]:
        if fq != 0: df[term] += 1

#IDFs       
idf = {"love": 0, "dog": 0, "cat": 0}

for term in idf:
    idf[term] = math.log10(len(terms) / df[term])

#Building the document-term matrix by using the tf-idf weights.
#tf-idf weight = tf[term][doc#] * idf[term]
docTermMatrix = [[tf[term][i] * idf[term] for i in range(len(documents))] for term in terms]

#Printing the document-term matrix.
print(docTermMatrix)