import requests

#HTTP 101
"""
[Status Codes]
200 OK
201 NO CONTENT
400 BAD REQUEST
404 NOT FOUND
403 FORBIDDEN
500 INTERNAL SERVER ERROR

[Methods]
    {GET} 
        -- It requests the data from a specified resource
        -- Very Little Data can be sent from Client to Server (Like so and so page)
        -- Can be bookmarked and cached
    {POST}
        -- It submits the data to a specified 
        -- Large Data can be sent since BODY of the request is used
        -- Cannot be Bookmarked or Cached
    {HEAD}
        -- This doesn't return body data. Only Headers.
        -- Used by browsers to determine if a page exists without using up a lot of data.
"""

## GET Request -- Content
get_response = requests.get('https://rogue-workshop.herokuapp.com/')
print(get_response.status_code)
print(get_response.content) # this is always bytes object


## GET Request -- JSON Endpoint
json_response = requests.get('https://rogue-workshop.herokuapp.com/JSON/')
print(json_response.status_code)
print(json_response.content)

##POST Request -- JSON Endpoint
data = {'request':'time'}
post_request = requests.post('https://rogue-workshop.herokuapp.com/JSON/', json=data)
print(post_request.status_code)
print(post_request.json())


