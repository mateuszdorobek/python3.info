# doctest: +SKIP_FILE

from sklearn.tree import DecisionTreeClassifier


features = [
    (5.1, 3.5, 1.4, 0.2),  # setosa
    (7.0, 3.2, 4.7, 1.4),  # versicolor
    (6.3, 3.3, 6.0, 2.5),  # virginica
    (4.9, 3.0, 1.4, 0.2),  # setosa
    (4.7, 3.2, 1.3, 0.2),  # setosa
    (6.4, 3.2, 4.5, 1.5),  # versicolor
    (7.1, 3.0, 5.9, 2.1),  # virginica
    (6.9, 3.1, 4.9, 1.5),  # versicolor
    (5.8, 2.7, 5.1, 1.9),  # virginica
]

labels = [
    'setosa',
    'versicolor',
    'virginica',
    'setosa',
    'setosa',
    'versicolor',
    'virginica',
    'versicolor',
    'virginica'
]


model = DecisionTreeClassifier()
model.fit(features, labels)

to_predict = [
    (5.6, 2.3, 4.1, 2.9)
]

result = model.predict(to_predict)
print(result)
# ['virginica']
