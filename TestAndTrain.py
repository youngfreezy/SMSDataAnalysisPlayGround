import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_table('smsspamcollection/SMSSpamCollection',
					sep="\t",
					header=None,
					names=['label', 'sms_message'])

df.label = df.label.map({'ham':0, 'spam':1})


X_train, X_test, Y_train, Y_test = train_test_split(df['sms_message'],
													df['label'],
													random_state=1)

# print('num rows in total set: {}'.format(df.shape[0]))
# print('num rows in training set: {}'.format(X_train.shape[0]))
# print('num rows in test set: {}'.format(X_test.shape[0]))

count_vector = CountVectorizer()

training_data = count_vector.fit_transform(X_train)

testing_data = count_vector.transform(X_test)

print(testing_data, training_data)

naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, Y_train)

predictions = naive_bayes.predict(testing_data)

print(predictions)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print('Accuracy score: ', format(accuracy_score(Y_test, predictions)))
print('Precision score: ', format(precision_score(Y_test, predictions)))
print('Recall score: ', format(recall_score(Y_test, predictions)))
print('F1 score: ', format(f1_score(Y_test, predictions)))