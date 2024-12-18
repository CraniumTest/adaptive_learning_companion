from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class PersonalizationModel:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestRegressor()

    def preprocess_data(self):
        # Assuming dataset has 'features' and 'outcomes'
        X = self.data.drop(['outcome'], axis=1)
        y = self.data['outcome']
        return train_test_split(X, y, test_size=0.2)

    def train_model(self):
        X_train, X_test, y_train, y_test = self.preprocess_data()
        self.model.fit(X_train, y_train)
        return self.model.score(X_test, y_test)

# Implementation
# data_handler = DataHandler('student_data.csv')
# student_data = data_handler.load_data()
# model = PersonalizationModel(student_data)
# accuracy = model.train_model()
# print(f"Model accuracy: {accuracy}")
