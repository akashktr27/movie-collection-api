import requests
import json
from behave import given, when, then

@given("the API is running")
def step_given_api_is_running(context):
    context.base_url = "http://127.0.0.1:8000"

@when("I request the health check endpoint")
def step_when_request_health_check(context):
    endpoint = f"{context.base_url}/health"
    context.response = requests.get(url=endpoint)

@when("I request the token endpoint with valid credentials")
def step_when_request_health_check(context):
    endpoint = f"{context.base_url}/register"
    payload = json.dumps({
        "username": "admin",
        "password": "admin"
    })
    headers = {
        "Content-type": "application/json"
    }
    context.response = requests.post(url=endpoint, headers=headers, data=payload)
    assert context.response.status_code == 200, "Failed to authenticate and retrieve token"
    context.token = context.response.json()["access"]

@when("I request the invalid token")
def get_invalid_token(context):
    context.invalid_token = "invalid_token_string"


@when("I request the token endpoint with invalid credentials")
def step_when_request_health_check(context):
    endpoint = f"{context.base_url}/register"
    payload = json.dumps({
        "username": "username",
        "password": "wrongpassword"
    })
    headers = {
        "Content-type": "application/json"
    }
    context.response = requests.post(url=endpoint, headers=headers, data=payload)
    assert context.response.status_code == 400, "Failed to authenticate and retrieve token"


@when("I request the movies endpoint with valid token")
def step_when_request_health_check(context):
    endpoint = f"{context.base_url}/movies"
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {context.token}"
    }
    context.response = requests.get(url=endpoint, headers=headers)
    response_data = context.response.json()
    assert context.response.status_code == 200, "Failed to authenticate and retrieve token"
    required_keys = {"count", "next", "previous", "data"}

    if isinstance(response_data, dict):
        assert required_keys.issubset(response_data.keys()), "Missing required key"

@when("I request the movies endpoint with invalid token")
def step_when_request_health_check(context):
    endpoint = f"{context.base_url}/movies"
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {context.invalid_token}"
    }
    context.response = requests.get(url=endpoint, headers=headers)

@when("I request the collection endpoint with valid token")
def step_when_request_health_check(context):
    endpoint = f"{context.base_url}/collection"
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {context.token}"
    }
    context.response = requests.get(url=endpoint, headers=headers)
    assert context.response.status_code == 200, "Failed to authenticate and retrieve token"


@when("I request get method of detail collection endpoint with valid token")
def collection_detail(context):

    collection_uuid = context.shared_data.get("collection_uuid")
    context.logger.info(collection_uuid)
    endpoint = f"{context.base_url}/collection/{collection_uuid}"
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {context.token}"
    }
    context.response = requests.get(url=endpoint, headers=headers)
    assert context.response.status_code == 200, "Failed to authenticate and retrieve token"

@when("I request get method of detail collection endpoint with invalid token")
def collection_detail(context):

    collection_uuid = context.shared_data.get("collection_uuid")
    context.logger.info(collection_uuid)
    endpoint = f"{context.base_url}/collection/{collection_uuid}"
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {context.invalid_token}"
    }
    context.response = requests.get(url=endpoint, headers=headers)

@when("I request post method of collection endpoint with valid token")
def collection_post_validkey(context):
    endpoint = f"{context.base_url}/collection"
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {context.token}"
    }
    payload = json.dumps(context.collection)
    context.response = requests.post(url=endpoint, headers=headers, data=payload)
    context.logger.info(context.response)
    context.collection_uuid = context.response.json()["collection_uuid"]
    context.shared_data["collection_uuid"] = context.collection_uuid  # Save globally

    assert context.response.status_code == 201, "Failed to authenticate and retrieve token"

@when("I request post method of collection endpoint with invalid token")
def collection_post_invalidkey(context):
    endpoint = f"{context.base_url}/collection"
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {context.invalid_token}"
    }
    payload = json.dumps(context.collection)
    context.response = requests.post(url=endpoint, headers=headers, data=payload)

@when("I request the collection endpoint with invalid token")
def step_when_request_health_check(context):
    endpoint = f"{context.base_url}/collection"
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {context.invalid_token}"
    }
    context.response = requests.get(url=endpoint, headers=headers)


@then('the response status should be {expected_status_code:d}')
def step_then_response_status(context, expected_status_code):
    assert context.response.status_code == expected_status_code, \
        f"Expected {expected_status_code}, but got {context.response.status_code}"

@then("the response body should indicate the service is ok")
def step_then_response_body(context):
    response_json = context.response.json()
    assert response_json.get("status") == "OK", f"Unexpected response body: {response_json}"

@then("the response body should indicate access key")
def step_then_response_body(context):
    response_data = context.response.json()
    required_keys = {"access"}
    if isinstance(response_data, dict):
        assert required_keys.issubset(response_data.keys()), "Missing required key access"

@then("the response body should indicate detail key")
def step_then_response_body(context):
    response_data = context.response.json()
    required_keys = {"detail"}
    if isinstance(response_data, dict):
        assert required_keys.issubset(response_data.keys()), "Missing required key detail"

@then('the response body should contain the keys {keys}')
def step_then_response_body_contains_keys(context, keys):
    expected_keys = eval(keys)
    response_json = context.response.json()
    missing_keys = [key for key in expected_keys if key not in response_json]
    assert not missing_keys, f"Missing keys in response: {missing_keys}"


