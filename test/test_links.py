import json
import requests
import pytest

def test_rdesign_links(subtests):
    """Check all links are valid in reference design table"""
    pytest.skip("Not supported anymore")
    designs = json.load(open("fpga/referencedesigns.json"))
    for design in designs:
        for urlfield in ["HDLSource", "UserGuide", "HDLDoc", "LinuxDriverDoc"]:
            if design[urlfield] == "":
                with subtests.test(msg="Skipping Test", design=design['Board']):
                    pytest.skip(f"No URL for field {urlfield} of board {design['Board']} {design['Carrier']}")
                continue
            url = design[urlfield]
            with subtests.test(msg=f"Test url {url}", url=url):
                print(f"Testing {url}")
                response = requests.get(url)
                assert response.status_code != 404
