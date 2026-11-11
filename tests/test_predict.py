
from equipment_failure.data import load_data
from equipment_failure.features import FEATURE_COLUMNS
from equipment_failure.predict import predict_failure


def test_prediction_output():
    df = load_data()

    input_data = df[FEATURE_COLUMNS].iloc[0].to_dict()

    result = predict_failure(input_data)

    assert result["prediction"] in [0, 1]
    assert result["result"] in [
        "Machine Failure Predicted",
        "No Machine Failure Predicted"
    ]
    assert 0 <= result["failure_probability"] <= 1


def test_prediction_keys():
    df = load_data()

    input_data = df[FEATURE_COLUMNS].iloc[0].to_dict()

    result = predict_failure(input_data)

    assert set(result.keys()) == {
        "prediction",
        "result",
        "failure_probability"
    }
