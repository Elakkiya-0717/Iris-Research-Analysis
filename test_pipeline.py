import pandas as pd

def validate_and_prepare(data):
    required = {"species", "petal_length"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    result = data.copy()
    result["petal_length"] = pd.to_numeric(result["petal_length"], errors="coerce")
    result = result[result["species"].isin(["setosa", "versicolor", "virginica"])]
    return result.dropna(subset=["species", "petal_length"]).copy()

def test_valid_synthetic_rows_are_kept():
    data = pd.DataFrame({"species":["setosa","versicolor","virginica"],"petal_length":[1.2,3.4,5.1]})
    assert len(validate_and_prepare(data)) == 3

def test_missing_or_invalid_outcomes_are_excluded():
    data = pd.DataFrame({"species":["setosa","versicolor"],"petal_length":[1.2,"bad"]})
    result = validate_and_prepare(data)
    assert len(result) == 1 and result.iloc[0]["species"] == "setosa"

def test_unknown_species_is_excluded():
    data = pd.DataFrame({"species":["setosa","unknown"],"petal_length":[1.2,2.0]})
    assert validate_and_prepare(data)["species"].tolist() == ["setosa"]

def test_missing_column_raises():
    try:
        validate_and_prepare(pd.DataFrame({"species":["setosa"]}))
    except ValueError as exc:
        assert "petal_length" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
