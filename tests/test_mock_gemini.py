import json
from app.services.gemini_service import retention_gemini


# def test_gemini(mocker):
#     fake_output = {
#                 "retention_plan": [
#                 "Proposer 2 jours de télétravail",
#                 "Réévaluer la charge de déplacement",
#                 "Plan de formation personnalisé"
#             ]
#               } 
    
#     fake_response = mocker.Mock()
#     fake_response.text = json.dumps(fake_output) 

#     fake_response.status_code = 200
#     fake_response.generate_content.return_value = fake_output

#     mock_client = mocker.Mock()
#     mock_client.models.generate_content.return_value = fake_response

#     mocker.patch(
#         "app.services.gemini_service.genai.Client",
#         return_value = mock_client
#     )

#     result = retention_gemini(
#         probability=0.78,
#         prediction="RISCK_ELEVE"
#     )


#     assert result == 




def test_retention_gemini(mocker):
    

    fake_response = mocker.Mock()
    fake_response.text = {
        "retention_plan": ["Aucun plan requis, rétention faible"]
                }
    

    mock_client = mocker.patch(
        "app.services.gemini_service.genai.Client"
    )
    
    mock_client.return_value.models.generate_content.return_value = fake_response


    result = retention_gemini(
        probability=0.25,
        prediction="RISCK_FAIBLE"
    )

    assert result.retention_plan == ["Aucun plan requis, rétention faible"]
