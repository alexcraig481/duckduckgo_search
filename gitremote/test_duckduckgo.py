import pytest
import requests


def test_us_presidents_search():
    """Confirming results include last names of all presidents"""
    us_presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Van Buren", "Harrison",
                     "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant",
                     "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison", "McKinley", "Roosevelt", "Taft",
                     "Wilson", "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy",
                     "Johnson", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"]

    # Define url
    url = 'https://api.duckduckgo.com/?q="presidents of the united states"&format=json'

    # Send GET request and capture response
    response = requests.get(url)

    # Capture response data in jason format
    response_dict = response.json()

    # Capture Related Topics list of dictionaries
    internal_links = response_dict["RelatedTopics"]

    # Loop through the list to access dictionaries - append value of key 'Text' to list
    search_result_text = ""
    for link in internal_links:
        search_result_text += link["Text"]

    # Assert statement
    for president in us_presidents:
        assert president in search_result_text
