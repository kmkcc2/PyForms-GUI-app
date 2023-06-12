import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, recall_score, roc_curve
from sklearn.tree import DecisionTreeClassifier
from analisys import data
from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlLabel,
    ControlText,
    ControlButton,
    ControlList
    )
class Classification(BaseWidget):
    def perform_classification(self, test_size_):
        # Wczytanie danych z dfFrame
        df = data.read()
        # Podział danych na cechy (X) i etykiety (y)
        X = df.drop('num', axis=1)
        y = df['num']

        # Podział danych na zbiór treningowy i zbiór testowy
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_, random_state=42)

        # Inicjalizacja klasyfikatora
        classifier = DecisionTreeClassifier()

        # Definicja siatki hiperparametrów
        param_grid = {
            'criterion': ['gini', 'entropy'],
            'max_depth': [None, 5, 10],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }

        # Inicjalizacja przeszukiwania siatki
        grid_search = GridSearchCV(classifier, param_grid, cv=5)

        # Dopasowanie modelu
        grid_search.fit(X_train, y_train)

        # Najlepsze parametry modelu
        best_params = grid_search.best_params_

        # Klasyfikacja na danych testowych
        y_pred = grid_search.predict(X_test)

        # Macierz pomyłek
        conf_matrix = confusion_matrix(y_test, y_pred)
        conf_data = []
        for row in conf_matrix:
            conf_data.append(row.tolist())
        self._mistake.value = conf_data

        # Tpr i Fpr
        TP = conf_matrix[1, 1]
        TN = conf_matrix[0, 0]
        FP = conf_matrix[0, 1]
        FN = conf_matrix[1, 0]
        tpr = round(TP/(TP + FN), 2)
        fpr = round(FP / (FP + TN),2)
        self._fprLabel.value = 'FPR: ' + str(fpr)
        self._tprLabel.value = 'TPR: ' + str(tpr)

        # Ocena jakości klasyfikatora
        accuracy = grid_search.score(X_test, y_test)
        return [best_params, accuracy, y_pred]
    def __init__(self):
        super(Classification, self).__init__('Statystyka')
        self.set_margin(50)
        self._title = ControlLabel("Najlepsze parametry modelu")
        self._test = ControlText("Test size (0;1): ")
        self._button = ControlButton("Generuj")
        self._button.value = self.__runEvent
        self._criteriaLabel = ControlLabel('Kryterium: ')
        self._depthLabel = ControlLabel('Max depth: ')
        self._leafLabel = ControlLabel('Min samples leaf: ')
        self._splitLabel = ControlLabel('Min samples split: ')
        self._accuLabel = ControlLabel('Dokładność klasyfikacji: ')
        self._fprLabel = ControlLabel('FPR: ')
        self._tprLabel = ControlLabel('TPR: ')
        self._mistake = ControlList('Macierz pomyłek')
        self._mistake.readonly = True

        self.formset = [
            ('_title', ' '),
            ('_test', '_button'),
            (' ', ' '),

            ([('_criteriaLabel'), ('_depthLabel'), ('_leafLabel'), ('_splitLabel'), ('_accuLabel'), ('_fprLabel'), ('_tprLabel')],' ', ' ', '_mistake', ' '),
        ]

    def __runEvent(self):
        try:
            if 0 < float(self._test.value) < 1:
                classification = self.perform_classification(float(self._test.value))
                dict = classification[0]
                accu = classification[1]
                self._criteriaLabel.value = "Kryterium: " + str(dict['criterion'])
                self._depthLabel.value = "Max depth: "+ str(dict['max_depth'])
                self._leafLabel.value = "Min samples leaf: " + str(dict['min_samples_leaf'])
                self._splitLabel.value = "Min samples split: " + str(dict['min_samples_split'])
                self._accuLabel.value = "Dokładność klasyfikacji: {:.2f}".format(accu)

            else:
                self.warning("Proszę wybrać liczbę z przedziału (0;1)")
        except:
            self.warning("Podane parametry nie są poprawne dla danego zbioru danych")



