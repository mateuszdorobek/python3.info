# doctest: +SKIP_FILE

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics, datasets


dataset = datasets.load_iris()
features = dataset.data
labels = dataset.target

data = train_test_split(features, labels, test_size=0.25, random_state=0)

features_train = data[0]
features_test = data[1]
labels_train = data[2]
labels_test = data[3]


model = KNeighborsClassifier(n_neighbors=5)
model.fit(features_train, labels_train)
labels_predicted = model.predict(features_test)

accuracy = metrics.accuracy_score(labels_test, labels_predicted)
print(accuracy)
# 0.9736842105263158
