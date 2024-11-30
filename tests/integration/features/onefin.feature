Feature: Test Onefin Assesment API

  Scenario: Health check endpoint returns 200 OK
      Given the API is running
      When I request the health check endpoint
      Then the response status should be 200
      And the response body should indicate the service is ok

  Scenario: Create token with valid credentials
      Given the API is running
      When I request the token endpoint with valid credentials
      Then the response status should be 200
      And the response body should indicate access key

  Scenario: Fallback 400 for invalid credentails for register endpoint
      Given the API is running
      When I request the token endpoint with invalid credentials
      Then the response status should be 400
      And the response body should indicate detail key

  Scenario: Retrieve movies endpoint with valid token
      Given the API is running
      When I request the token endpoint with valid credentials
      When I request the movies endpoint with valid token
      Then the response status should be 200
      And the response body should contain the keys ["count", "next", "previous", "data"]

  Scenario: Fallback 401 for invalid credentials for movies endpoint
      Given the API is running
      When I request the invalid token
      When I request the movies endpoint with invalid token
      Then the response status should be 401
      And the response body should contain the keys ["detail", "code", "messages"]

  Scenario: Retrieve collection endpoint with valid token
      Given the API is running
      When I request the token endpoint with valid credentials
      When I request the collection endpoint with valid token
      Then the response status should be 200
      And the response body should contain the keys ["is_success", "data"]

  Scenario: Fallback 401 for invalid credentials for collection endpoint
      Given the API is running
      When I request the invalid token
      When I request the collection endpoint with invalid token
      Then the response status should be 401
      And the response body should contain the keys ["detail", "code", "messages"]

  Scenario: Create collection using collection endpoint with valid token
      Given the API is running
      When I request the token endpoint with valid credentials
      When I request post method of collection endpoint with valid token
      Then the response status should be 201
      And the response body should contain the keys ["collection_uuid"]
      When I request get method of detail collection endpoint with valid token
      Then the response status should be 200
      And the response body should contain the keys ["uuid", "title", "description", "movies"]


  Scenario: Fallback 401 for invalid credentials for create collection endpoint
      Given the API is running
      When I request the invalid token
      When I request post method of collection endpoint with invalid token
      Then the response status should be 401
      And the response body should contain the keys ["detail", "code", "messages"]

  Scenario: Retrieve collection detail endpoint with valid token
      Given the API is running
      When I request the token endpoint with valid credentials
      When I request get method of detail collection endpoint with valid token
      Then the response status should be 200
      And the response body should contain the keys ["uuid", "title", "description", "movies"]

  Scenario: Fallback 401 for invalid credentials for collection detail endpoint
      Given the API is running
      When I request the invalid token
      When I request get method of detail collection endpoint with invalid token
      Then the response status should be 401
      And the response body should contain the keys ["detail", "code", "messages"]

  Scenario: Update collection detail endpoint with valid token
      Given the API is running
      When I request the token endpoint with valid credentials
      When I request put method of detail collection endpoint with valid token
      Then the response status should be 200
      And the response body should contain the keys ["uuid", "title", "description", "movies"]
      And verify put request response

  Scenario: Fallback 401 for invalid credentials for collection detail endpoint
      Given the API is running
      When I request the invalid token
      When I request put method of detail collection endpoint with invalid token
      Then the response status should be 401
      And the response body should contain the keys ["detail", "code", "messages"]

  Scenario: Fallback 401 for invalid credentials for collection detail endpoint
      Given the API is running
      When I request the invalid token
      When I request delete method of detail collection endpoint with invalid token
      Then the response status should be 401
      And the response body should contain the keys ["detail", "code", "messages"]

  Scenario: Delete collection detail endpoint with valid token
      Given the API is running
      When I request the token endpoint with valid credentials
      When I request delete method of detail collection endpoint with valid token
      Then the response status should be 204
