from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

def split_data(data, target, test_size=0.2, random_state=42):
    x = data.drop(columns=[target])
    y = data[target]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)

    return x_train, x_test, y_train, y_test

def Model_pipeline(num_columns, cat_columns, model):
    
    numeric_transform = Pipeline(steps=[("scaler", StandardScaler())])
    categoric_transform = Pipeline(steps=[("encode", OneHotEncoder())])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transform, num_columns),
            ("cat", categoric_transform, cat_columns)
        ]
    )

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("feature_selection", SelectKBest(score_func=f_classif)),
            ("model", model)
        ]
    )

def metric_model(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return accuracy, precision, recall, f1

def train_with_grid_search(model_type, num_columns, cat_columns, data):

    x_train, x_test, y_train, y_test = split_data(data, target="Attrition")

    num_columns = [col for col in num_columns if col in x_train.columns]
    cat_columns = [col for col in cat_columns if col in x_train.columns]

    param_grid_rfc = {
        "model__n_estimators": [10, 50, 100, 250, 500],
        "model__max_features": ["sqrt", "log2"],
        "feature_selection__k": [3, 5, "all"]
    }

    param_grid_lr = {
        "model__l1_ratio": [0],
        "model__C": [0.01, 0.1, 1, 10],
        "feature_selection__k": [3, 5, "all"]
    } 

    if model_type == "random_forest":
        param_grid = param_grid_rfc
        model = RandomForestClassifier()
    elif model_type == "logistic_regression":
        param_grid = param_grid_lr
        model = LogisticRegression()


    Pipeline = Model_pipeline(num_columns, cat_columns, model)

    grid_search = GridSearchCV(estimator=Pipeline, param_grid=param_grid)
    grid_search.fit(x_train, y_train)

    best_model = grid_search.best_estimator_

    if model_type == "logistic_regression":
        joblib.dump(best_model, "logistic_regression.dump")

    

    y_pred = best_model.predict(x_test)

    return metric_model(y_test, y_pred)
