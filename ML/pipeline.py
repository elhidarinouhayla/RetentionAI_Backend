from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
import joblib

# split du data

def split_data(data, target, test_size=0.2, random_state=42):
    x = data.drop(columns=[target])
    y = data[target]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)

    return x_train, x_test, y_train, y_test

# realisation du pipeline sklearn

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

# Metriques d'evaluation

def metric_model(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return accuracy, precision, recall, f1


# Courbe ROC

def roc_curve_model(model, x_test, y_test):

    y_proba = model.predict_proba(x_test)[:, 1]
    fpr, tpr, _  = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)

    return fpr, tpr, roc_auc
