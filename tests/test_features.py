
from equipment_failure.data import load_data
from equipment_failure.features import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
    prepare_features_target
)


def test_feature_target_separation():
    df = load_data()

    X, y = prepare_features_target(df)

    assert list(X.columns) == FEATURE_COLUMNS
    assert y.name == TARGET_COLUMN


def test_feature_target_shapes():
    df = load_data()

    X, y = prepare_features_target(df)

    assert X.shape == (10000, 6)
    assert y.shape == (10000,)


def test_target_values():
    df = load_data()

    X, y = prepare_features_target(df)

    assert set(y.unique()).issubset({0, 1})
