
from sklearn.neighbors import KNeighborsClassifier

def build_knn():
    return KNeighborsClassifier(n_neighbors=5, metric='euclidean')
