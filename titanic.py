<<<<<<< HEAD
"""
Prediction de la survie d'un individu sur le Titanic
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import argparse
import os
from dotenv import load_dotenv

from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix

load_dotenv()
parser = argparse.ArgumentParser(description="Configuration du modèle")
parser.add_argument(
    "--N_TREES", 
    type=int, 
    default=20,  
    help="Un entier numérique pour le nombre d'arbres"
)

parser.add_argument(
    "--MAX_DEPTH", 
    type=int, 
    default=None, 
    help="Un entier numérique ou None pour la profondeur maximale"
)

args = parser.parse_args()

N_TREES = args.N_TREES
MAX_DEPTH = args.MAX_DEPTH
MAX_FEATURES = "sqrt"
JETON_API = os.getenv("JETON_API")


# IMPORT ET EXPLORATION DONNEES --------------------------------

TrainingData = pd.read_csv("data.csv")

TrainingData.isnull().sum()

# Statut socioéconomique
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
fig1_pclass = sns.countplot(data=TrainingData, x="Pclass", ax=axes[0]).set_title(
    "fréquence des Pclass"
)
fig2_pclass = sns.barplot(
    data=TrainingData, x="Pclass", y="Survived", ax=axes[1]
).set_title("survie des Pclass")

# Age
sns.histplot(data=TrainingData, x="Age", bins=15, kde=False).set_title(
    "Distribution de l'âge"
)
plt.show()

=======
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix


TrainingData = pd.read_csv("data.csv")

TrainingData.head()


TrainingData["Ticket"].str.split("/").str.len()

TrainingData["Name"].str.split(",").str.len()

n_trees = 20
max_depth = None
max_features = "sqrt"

TrainingData.isnull().sum()


## Un peu d'exploration et de feature engineering

### Statut socioéconomique

fig, axes = plt.subplots(
    1, 2, figsize=(12, 6)
)  # layout matplotlib 1 ligne 2 colonnes taile 16*8
fig1_pclass = sns.countplot(data=TrainingData, x="Pclass", ax=axes[0]).set_title(
    "fréquence des Pclass"
)
fig2_pclass = sns.barplot(
    data=TrainingData, x="Pclass", y="Survived", ax=axes[1]
).set_title("survie des Pclass")


### Age

sns.histplot(data=TrainingData, x="Age", bins=15, kde=False).set_title(
    "Distribution de l'âge"
)
plt.show()

## Encoder les données imputées ou transformées.


numeric_features = ["Age", "Fare"]
categorical_features = ["Embarked", "Sex"]

numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", MinMaxScaler()),
    ]
)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder()),
    ]
)


preprocessor = ColumnTransformer(
    transformers=[
        ("Preprocessing numerical", numeric_transformer, numeric_features),
        (
            "Preprocessing categorical",
            categorical_transformer,
            categorical_features,
        ),
    ]
)

pipe = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=20)),
    ]
)
>>>>>>> af94539cbb6d79e63deb4192cc22ae61ca903183

# SPLIT TRAIN/TEST --------------------------------

<<<<<<< HEAD
# On _split_ notre _dataset_ d'apprentisage
=======
# splitting samples
y = TrainingData["Survived"]
X = TrainingData.drop("Survived", axis="columns")

# On _split_ notre _dataset_ d'apprentisage pour faire de la validation croisée une partie pour apprendre une partie pour regarder le score.
>>>>>>> af94539cbb6d79e63deb4192cc22ae61ca903183
# Prenons arbitrairement 10% du dataset en test et 90% pour l'apprentissage.

y = TrainingData["Survived"]
X = TrainingData.drop("Survived", axis="columns")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)


# PIPELINE ----------------------------

<<<<<<< HEAD
# Définition des variables
numeric_features = ["Age", "Fare"]
categorical_features = ["Embarked", "Sex"]

# Variables numériques
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", MinMaxScaler()),
    ]
)

# Variables catégorielles
categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder()),
    ]
)

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("Preprocessing numerical", numeric_transformer, numeric_features),
        (
            "Preprocessing categorical",
            categorical_transformer,
            categorical_features,
        ),
    ]
)

# Pipeline
pipe = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=N_TREES)),
    ]
)


# ESTIMATION ET EVALUATION ----------------------

pipe.fit(X_train, y_train)

# score
=======


# Ici demandons d'avoir 20 arbres
pipe.fit(X_train, y_train)


# calculons le score sur le dataset d'apprentissage et sur le dataset de test (10% du dataset d'apprentissage mis de côté)
# le score étant le nombre de bonne prédiction
>>>>>>> af94539cbb6d79e63deb4192cc22ae61ca903183
rdmf_score = pipe.score(X_test, y_test)
print(f"{rdmf_score:.1%} de bonnes réponses sur les données de test pour validation")
<<<<<<< HEAD

=======
>>>>>>> af94539cbb6d79e63deb4192cc22ae61ca903183
print(20 * "-")
print("matrice de confusion")
print(confusion_matrix(y_test, pipe.predict(X_test)))
