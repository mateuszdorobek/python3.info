# doctest: +SKIP_FILE

from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split


dataset = datasets.load_iris()
features = dataset.data
labels = dataset.target

data = train_test_split(features, labels, test_size=0.25, random_state=0)

features_train = data[0]
features_test = data[1]
labels_train = data[2]
labels_test = data[3]

model = KNeighborsClassifier()
scores = cross_val_score(model, features_train, labels_train, cv=5)
accuracy = scores.mean() * 100  # percent
stdev = scores.std() * 100      # percent

print(f'Accuracy is {accuracy:.2f}% (+/- {stdev:.2f}%)')
# Accuracy is 95.49% (+/- 4.98%)
