Feature: Test Onefin Assesment API

  Scenario: Health check endpoint returns 200 OK
      Given the API is running
      When I request the health check endpoint
      Then the response status should be 200
      And the response body should indicate the service is ok

  Scenario:
      Given the API is running
      When I request the token endpoint with valid credentials
      Then the response status should be 200
      And the response body should indicate access key

  Scenario:
      Given the API is running
      When I request the token endpoint with invalid credentials
      Then the response status should be 400
      And the response body should indicate detail key

  Scenario:
      Given the API is running
      When I request the token endpoint with valid credentials
      When I request the movies endpoint with valid token
      Then the response status should be 200
      And the response body should contain the keys ["count", "next", "previous", "data"]

  Scenario:
      Given the API is running
      When I request the invalid token
      When I request the movies endpoint with invalid token
      Then the response status should be 401
      And the response body should contain the keys ["detail", "code", "messages"]

  Scenario:
      Given the API is running
      When I request the token endpoint with valid credentials
      When I request the collection endpoint with valid token
      Then the response status should be 200
      And the response body should contain the keys ["is_success", "data"]

  Scenario:
      Given the API is running
      When I request the invalid token
      When I request the collection endpoint with invalid token
      Then the response status should be 401
      And the response body should contain the keys ["detail", "code", "messages"]