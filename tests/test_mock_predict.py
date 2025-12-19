from app.services.predict_service import predict_probability
import json

def test_predict(mocker):

    fake_data = mocker.Mock()
    fake_data.dict.return_value = {
                "Gender": "Male",
                "Age": 32,
                 "Department": "Sales"
                 }


    fake_model = mocker.Mock()
    fake_model.predict_proba.return_value = [[0.33, 0.67]]
    

    mocker.patch(
        "app.services.predict_service.model",
         fake_model
    )

    result = predict_probability(fake_data)

    assert result == 0.67