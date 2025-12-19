import json
from app.services.gemini_service import retention_gemini


import json

def test_retention_gemini(mocker):

    fake_response = mocker.Mock()
    fake_response.text = json.dumps({
        "retention_plan": ["Aucun plan requis, rétention faible"]
    })

    mock_client = mocker.patch(
        "app.services.gemini_service.genai.Client"
    )

    mock_client.return_value.models.generate_content.return_value = fake_response

    result = retention_gemini(
        probability=0.25,
        prediction="RISCK_FAIBLE"
    )

    assert result.retention_plan == ["Aucun plan requis, rétention faible"]
