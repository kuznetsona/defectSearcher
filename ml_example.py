import random

import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC


def dumb_deductive_classification(temperature: float, age: int, immunity: float):
    return 1 if temperature > 37.2 else 0


def actual_function(temperature: float, age: int, immunity: float):
    if temperature > 37.2:
        return 1
    elif temperature > 37 and age > 40:
        return 1
    elif immunity < 50:
        return 1
    else:
        return 0


def get_patient_dict(temperature, age, immunity):
    factors = dict(temperature=temperature, age=age, immunity=immunity)
    return dict(
        **factors,
        y=actual_function(**factors)
    )


def get_random_temperature() -> float:
    return round(random.uniform(35.5, 36.8), 1) if random.randint(1, 5) != 1 else round(random.uniform(37, 40), 1)


def get_random_age() -> float:
    return random.randint(1, 100)


def get_random_immunity() -> float:
    return random.randint(1, 100)


if __name__ == '__main__':
    # generate dataset
    random.seed(42)

    df = pd.DataFrame([
        get_patient_dict(
            temperature=get_random_temperature(),
            age=get_random_age(),
            immunity=get_random_immunity()
        )
        for _ in range(1000)
    ]
    )

    # model training & validation
    train_df, test_df = train_test_split(df, train_size=0.7)

    common_args = {'max_iter': [int(1e5)], 'random_state': [42]}
    param_grid = [{'C': [1e0, 1e1, 1e2, 1e3], 'kernel': ['linear'], **common_args}]

    clf_grid = GridSearchCV(SVC(), param_grid)
    clf_grid.fit(X=train_df.drop(columns=['y']), y=train_df['y'])
    clf = clf_grid.best_estimator_
    clf_params = clf_grid.best_params_

    # model testing
    y_ml_pred = clf.predict(test_df.drop(columns=['y']))
    y_deduct_pred = [dumb_deductive_classification(**row) for i, row in test_df.drop(columns=['y']).iterrows()]

    deductive_acc = metrics.accuracy_score(y_true=y_deduct_pred, y_pred=y_ml_pred)
    ml_acc = metrics.accuracy_score(y_true=test_df['y'], y_pred=y_ml_pred)

    print(f'manual deductive accuracy = {deductive_acc}')
    print(f'automatic ml accuracy     = {ml_acc}')

    imps_dict = dict(zip(('temperature', 'age', 'immunity'), clf._get_coef()[0]))
    print(f'ml feature importances = {imps_dict}')
