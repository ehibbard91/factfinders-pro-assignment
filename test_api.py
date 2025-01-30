import requests

# URL for the API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"


def test_get_api_response_code():
    response = requests.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"


def test_get_api_response_body():
    response = requests.get(url)

    # Get the response JSON
    response_data = response.json()

    # Assert that the response body contains the expected data
    assert response_data['id'] == 1, f"Expected id to be 1, but got {response_data['id']}"
    assert 'title' in response_data, "Expected title to be in the response body"
    assert 'body' in response_data, "Expected body to be in the response body"