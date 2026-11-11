from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


# Test 1: Check whether the API is running
def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Equipment Failure Prediction API is running!"
    }


# Test 2: Check prediction with valid input
def test_valid_prediction():
    response = client.post(
        "/predict",
        json={
            "Type": "M",
            "Air_temperature": 300.0,
            "Process_temperature": 310.0,
            "Rotational_speed": 1500,
            "Torque": 40.0,
            "Tool_wear": 100
        }
    )

    assert response.status_code == 200

    result = response.json()

    assert result["prediction"] in [0, 1]
    assert "result" in result
    assert 0 <= result["failure_probability"] <= 1


# Test 3: Check prediction with invalid machine type
def test_invalid_machine_type():
    response = client.post(
        "/predict",
        json={
            "Type": "Z",
            "Air_temperature": 300.0,
            "Process_temperature": 310.0,
            "Rotational_speed": 1500,
            "Torque": 40.0,
            "Tool_wear": 100
        }
    )

    assert response.status_code == 422