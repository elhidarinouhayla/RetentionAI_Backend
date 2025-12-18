from google import genai
from ..config import GEMINI_API_KEY
from app.models.schemas import output_gemini



def retention_gemini(probability, prediction):


    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
    Contexte : ce salarié a un risque élevé de "churn_probability" de départ selon le modèle ML.  

    Tache : propose 3 actions concrètes et personnalisées pour le retenir dans l'entreprise,
    en tenant compte de son role, sa satisfaction, sa performance et son équilibre vie professionnelle/personnelle.  
    Rédige les actions de façon claire et opérationnelle pour un manager RH.

    exemple:
     "retention_plan": [
                    "Proposer 2 jours de télétravail",
                    "Réévaluer la charge de déplacement",
                    "Plan de formation personnalisé"
                ]
    """
    
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": output_gemini.model_json_schema()
    }
)
    

    output = output_gemini.model_validate_json(response.text)
 
    return  output
    
    
# prompt = "Salarié à risque élevé, département Sales, JobRole: Sales Executive, Performance: bonne, Satisfaction: moyenne"

# result = analyze_with_gemini(prompt)

# print(result)