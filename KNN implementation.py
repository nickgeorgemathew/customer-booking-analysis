#k nearest neighbours
import numpy as np
from collections import Counter
def euc_sum(x1,x2):
    distance=np.sqrt(np.sum((x1-x2)**2))
    return distance
class KNN:
    def __init__(self,k=3):
        self.k=k
    # fit function to fit x and y
    def fit(self,X,y):
        self.X_train= X
        self.y_train=y
    # function that does the prediction
    def predict(self,X):
        # list of predictions for all the values in the testing data X 
        predictions=[self._predict(x) for x in X ]
        return predictions
        
    def _predict(self,x):
        # calculates the distance between the data we need to predict x and the training data X_train
        distances=[euc_sum(x,x_train) for x_train in self.X_train]
        # 
        k_indices=np.argsort(distances)[:self.k]
        # 
        k_nearest_labels=[self.y_train[i] for i in k_indices]
        # 
        most_common=Counter(k_nearest_labels).most_common()
        return most_common


        