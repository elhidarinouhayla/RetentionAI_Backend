# RetentionAI_Frontend





## Objectif du projet


Backend de RetentionAI, une application d’aide à la décision RH combinant machine learning supervisé et intelligence artificielle générative. Ce backend expose une API sécurisée permettant de prédire le risque de départ d’un employé et de générer des plans de rétention personnalisés.





## Structure du projet

```

backend/
.
├── app/
│   ├── services/
│   │   ├── classification.py         
│   │   └── gemini_service.py        
│   ├── auth.py              
│   ├── database.py           
│   ├── config.py              
│   ├── models.py              
│   |   ├──models.py 
|   |   └──schemas.py
│   └── main.py
├── ML/
│   ├── EDA.ipynb    
│   ├── pipeline.py
|   ├── Data                    
|   |  └──data.csv  
|    └── logistic_regression.plk
├── tests/
│   ├── test_mocke_gemini.py     
│   └── test_mock_predict.py 
├── .env                       
├── .gitignore                  
├── requirements.txt           
├── Dockerfile                  
└── README.md            



```





---



## Installation



1. Cloner le dépôt GitHub :  



```shell

    git clone https://github.com/elhidarinouhayla/RetentionAI_Backend.git

    cd project

```



2. Créer un environnement virtuel :



 - Linux / Mac :

```shell

    python -m venv venv

    source venv/bin/activate

```

 - Windows :

```shell

    python -m venv venv

    venv\Scripts\activate

```



3. Installer les dépendances :



```shell

    pip install -r requirements.txt

```



4. Lancer l’API en mode développement :



```shell

    uvicorn main:app --reload

```



 - L’API sera accessible à l’adresse : http://127.0.0.1:8000



 - Documentation interactive Swagger : http://127.0.0.1:8000/docs



Astuce : Le paramètre --reload permet à l’API de se mettre à jour automatiquement à chaque modification du code, très pratique pour le développement.





## Configuration



```shell

# Secrets de l'API (à remplacer par de vraies valeurs)
SECRET_KEY=votre_clef_secrete_jwt
ALGORITHM=HS256

# Configuration Gemini
GEMINI_API_KEY=votre_clef_api_gemini

# Configuration Hugging Face
HF_TOKEN=votre_token_huggingface

# Configuration Base de Données PostgreSQL
USER=user
PASSWORD=password
DATABASE=analyzer_db
HOST=localhost 
PORT=5432

```


## Endpoint:/register , /login et /generate_retention_plan
```
| Endpoint                   | Méthode | Description                                        |
| -------------------------- | ------- | -------------------------------------------------- |
| /register                  | POST    | Creer un utilisateur RH                            |
| /login                     | POST    | Authentification et récupération du token JWT      |
| /predict                   | POST    | Predit le risque de départ d’un employe            |
| /generate-retention-plan   | POST    | Genere un plan de rétention si le risque est eleve |

```

- Exemple post/predict

```shell
    {
  "Gender": "Male",
  "Age": 32,
  "Department": "Sales",
  "JobRole": "Sales Executive",
  "MonthlyIncome": 4500,
  "YearsAtCompany": 5,
  "JobSatisfaction": 3,
  "WorkLifeBalance": 3,
  "OverTime": "Yes",
  "BusinessTravel": "Travel_Rarely",
  "Education": 3,
  "EducationField": "Marketing",
  "EnvironmentSatisfaction": 3,
  "JobInvolvement": 3,
  "JobLevel": 2,
  "MaritalStatus": "Single",
  "PercentSalaryHike": 12,
  "PerformanceRating": 3,
  "RelationshipSatisfaction": 3,
  "StockOptionLevel": 1,
  "TotalWorkingYears": 8,
  "YearsInCurrentRole": 3,
  "YearsWithCurrManager": 2
}
```

- Reponce :
```shell
{
  "churn_probability": 0.78,
  "prediction": "RISCK_ELEVE"
}  
```

- Exemple post/generate_retention_plan :
```shell
  {
  "retention_plan": [
    "Proposer 2 jours de télétravail",
    "Réévaluer la charge de déplacement",
    "Plan de formation personnalisé"
  ]
}

```

## Tests Unitaires
Les tests sont cruciaux pour garantir la fiabilité du chaînage des services d'IA. Ils incluent un mocking complet des appels du modele entraine du ML et Gemini pour des tests rapides et isoles

- Mock machine learning
- Mock Gemini


### Commande pour lancer les tests :



```shell

pytest

```



## Dockerfile



Le Dockerfile permet de construire une image Docker pour le backend FastAPI.


Il fait les étapes suivantes :


  1. Utilise Python 3.11 comme base

  2. Définit le dossier de travail /app

  3. Copie le fichier requirements.txt et installe les dépendances Python

  4. Copie tout le code du backend dans l’image

  5. Expose le port 8000 pour l’API

  6. Lance le serveur Uvicorn à l’intérieur du conteneur


=> Cela permet de déployer facilement l’API sur n’importe quelle machine sans config supplémentaire



# Docker compose 

ona fait un docker compose pour orchester service backend, servise base de donne et service fronend

- la comande pour lancer un docker compose:

```shell
   docker-compose -- up build
```

