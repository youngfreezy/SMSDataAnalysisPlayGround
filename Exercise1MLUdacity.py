import pandas as pd 

df = pd.read_table('smsspamcollection/SMSSpamCollection',
					sep="\t",
					header=None,
					names=['label', 'sms_message'])

df.label = df.label.map({'ham':0, 'spam':1})

# print(df.head())
# print(df.shape)

documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

lower_cased = []
for i in documents:
	lower_cased.append(i.lower())
# print(lower_cased)

no_punctation = []
import string

for i in lower_cased:
	no_punctation.append(i.translate(string.maketrans('', ''), string.punctuation))
# print(no_punctation)

pre_processed_documents = []
for i in no_punctation:
		pre_processed_documents.append(i.split(' '))
# print(pre_processed_documents)

frequency_list = [];
import pprint
from collections import Counter

for i in pre_processed_documents:
	frequency_counts = Counter(i)
	frequency_list.append(frequency_counts)

pprint.pprint(frequency_list);

from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer()
print(count_vector)
count_vector.fit(documents)
count_vector.get_feature_names();

doc_array = count_vector.transform(documents).toarray()
print(doc_array)

frequency_matrix = pd.DataFrame(doc_array, columns = count_vector.get_feature_names())

print(frequency_matrix)