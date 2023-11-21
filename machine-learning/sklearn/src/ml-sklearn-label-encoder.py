# doctest: +SKIP_FILE

from sklearn import preprocessing


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

labels_names = [
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

label_encoder = preprocessing.LabelEncoder()
labels = label_encoder.fit_transform(labels_names)
# array([0, 1, 2, 0, 0, 1, 2, 1, 2])

list(label_encoder.classes_)
# ['setosa', 'versicolor', 'virginica']

# 0: setosa
# 1: versicolor
# 2: virginica

list(label_encoder.inverse_transform([2, 2, 1]))
# ['virginica', 'virginica', 'setosa']
