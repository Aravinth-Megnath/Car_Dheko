from sklearn.base import BaseEstimator, TransformerMixin
class CleanTyreType(BaseEstimator, TransformerMixin):
    def __init__(self, column='Tyre Type'):
        self.column = column
        self.tyre_dict = {  # Dictionary as an instance variable
            'tubeless,radial': 'Tubeless + Radial',
            'radial,tubeless': 'Tubeless + Radial',
            'tubeless, radial': 'Tubeless + Radial',
            'tubeless tyres,radial': 'Tubeless + Radial',
            'tubeless radials tyre': 'Tubeless + Radial',
            'tubeless radial': 'Tubeless + Radial',
            'radial,tubless': 'Tubeless + Radial',
            'tubeless. runflat': 'Tubeless + Runflat',
            'tubeless,runflat': 'Tubeless + Runflat',
            'tubeless radials tyre': 'Tubeless + Runflat',
            'runflat, radial': 'Runflat + Radial',
            'runflat': 'Runflat',
            'radial': 'Radial',
            'tubeless': 'Tubeless',
            'unknown': 'Unknown',
            'radial with tube': 'Radial with Tube',
            'tubeless, all terrain': 'Tubeless + All Terrain',
            'tubeless tyres mud terrain': 'Tubeless + Mud Terrain'
        }

    def fit(self, X, y=None):
        return self  # No fitting required, just return self

    def transform(self, X):
        X = X.copy()  # Avoid modifying original DataFrame
        X[self.column] = X[self.column].astype(str).apply(self.clean_tyre)  # Apply cleaning
        return X

    def clean_tyre(self, x):
        x = x.lower().strip()
        return self.tyre_dict.get(x, 'Other')  # Return cleaned value or 'Other' if not found
