import json
import pytest
from unittest.mock import patch
from pathlib import Path

from backend.app.collectors.yc.models import YCStartup
from backend.app.collectors.yc.collector import _parse_json_item, run
from backend.app.collectors.yc.exporter import export_startups
from pydantic import ValidationError

def test_parse_json_item():
    item = {
        "name": "Airbnb",
        "one_liner": "Book places to stay and things to do.",
        "website": "https://www.airbnb.com",
        "batch": "Winter 2009",
        "industry": "Consumer",
        "all_locations": "San Francisco, CA, USA"
    }
    startup = _parse_json_item(item)
    assert startup.company_name == "Airbnb"
    assert startup.description == "Book places to stay and things to do."
    assert str(startup.website) == "https://www.airbnb.com/"
    assert startup.batch == "Winter 2009"
    assert startup.industry == "Consumer"
    assert startup.location == "San Francisco, CA, USA"

def test_model_validation():
    # Empty company name should fail
    with pytest.raises(ValidationError):
        YCStartup(company_name="")
        
    # Invalid URL should fail
    with pytest.raises(ValidationError):
        YCStartup(company_name="Test", website="not-a-url")

def test_export_startups(tmp_path):
    startups = [
        YCStartup(company_name="Airbnb", website="https://www.airbnb.com")
    ]
    output_path = tmp_path / "yc_startups.json"
    export_startups(startups, output_path=str(output_path))
    
    assert output_path.exists()
    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]["company_name"] == "Airbnb"

@patch("backend.app.collectors.yc.collector._fetch_json", return_value=[])
def test_empty_dataset_raises_error(mock_fetch):
    with pytest.raises(RuntimeError, match="YC collector did not find any startups – aborting"):
        run()
