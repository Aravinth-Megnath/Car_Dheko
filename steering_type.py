from sklearn.base import BaseEstimator, TransformerMixin

class CleaningSteeringType(BaseEstimator, TransformerMixin):
    def __init__(self, column='Steering Type'):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X[self.column] = X[self.column].apply(self.clean_steering)
        return X

    def clean_steering(self, x):
        if x == 'Electrical':
            return 'Electric'
        elif x == 'power':
            return 'Power'
        elif x == 'electric':
            return 'Electric'
        else:
            return x


    