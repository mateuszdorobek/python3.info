# doctest: +SKIP_FILE

from sklearn import datasets
from sklearn.model_selection import train_test_split


dataset = datasets.load_iris()
# dataset = datasets.load_breast_cancer()
# dataset = datasets.load_diabetes()
# dataset = datasets.load_boston()
# dataset = datasets.load_wine()

features = dataset.data
labels = dataset.target

data = train_test_split(features, labels, test_size=0.25, random_state=0)
features_train = data[0]
features_test = data[1]
labels_train = data[2]
labels_test = data[3]


# This is the most frequent form
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.25, random_state=0)
