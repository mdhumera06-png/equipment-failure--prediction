from equipment_failure.data import load_data


def test_load_data():
    df = load_data()

    assert df is not None
    assert df.shape == (10000, 14)


def test_required_columns():
    df = load_data()

    required_columns = [
        "Type",
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
        "Machine failure"
    ]

    for column in required_columns:
        assert column in df.columns


def test_no_missing_values():
    df = load_data()

    assert df.isnull().sum().sum() == 0