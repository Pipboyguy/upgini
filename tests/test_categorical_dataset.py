import os

import pandas as pd
import pytest

from upgini import Dataset, FileColumnMeaningType

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "test_data/categorical/",
)


@pytest.fixture
def etalon_definition():
    return {
        "phone_num": FileColumnMeaningType.MSISDN,
        "rep_date": FileColumnMeaningType.DATE,
        "target": FileColumnMeaningType.TARGET,
    }


@pytest.fixture
def etalon_search_keys():
    return [("phone_num", "rep_date")]


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "data.csv.gz"))
def test_categorical_dataset(datafiles, etalon_definition, etalon_search_keys):
    df = pd.read_csv(datafiles / "data.csv.gz")
    ds = Dataset(
        dataset_name="test Dataset",
        description="test",
        df=df,
        meaning_types=etalon_definition,
        search_keys=etalon_search_keys,
    )
    ds.validate()
    expected_valid_rows = 16913
    assert len(ds) == expected_valid_rows
