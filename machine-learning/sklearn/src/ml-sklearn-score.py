# doctest: +SKIP_FILE

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
model.fit(features_train, labels_train)
model.predict(features_test)

score = model.score(features_test, labels_test)
accuracy = score * 100  # in percent

print(f'Accuracy is {accuracy:.2f}%')
# Accuracy is 97.37%
