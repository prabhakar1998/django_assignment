
# Usage

The webapp is live and running on aws ec2 instance.
The webapp can be accessed using URL http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/

API documentation: 
     The api documentation can be checked using  http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/


###Endpoints

####Service Provider API's

1. api/providers/

Method: GET
Link: http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/api/providers/
Response code: 200
Example response body
```json
[
  {
    "id": 2,
    "name": "Provider 2",
    "email": "user2@gmail.com",
    "phone_number": "+917611182253",
    "language": "En",
    "currency": "USD",
    "created_at": "2021-07-11T07:10:27.771110Z",
    "updated_at": "2021-07-11T07:10:27.775267Z"
  },
  {
    "id": 1,
    "name": "Alex",
    "email": "alex@gmail.com",
    "phone_number": "+919655782265",
    "language": "En",
    "currency": "INR",
    "created_at": "2021-07-11T07:09:56.565910Z",
    "updated_at": "2021-07-11T07:11:27.081010Z"
  }
]
```

2. api/providers/

Method: POST
Link: http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/api/providers/
Response code: 201
Example Post data
```json
{
"id": 2,
"name": "Provider 2",
"email": "user2@gmail.com",
"phone_number": "+917611182253",
"language": "En",
"currency": "USD",
}
```
Example response body
```json
{
"id": 2,
"name": "Provider 2",
"email": "user2@gmail.com",
"phone_number": "+917611182253",
"language": "En",
"currency": "USD",
"created_at": "2021-07-11T07:10:27.771110Z",
"updated_at": "2021-07-11T07:10:27.775267Z"
}
```

3. api/providers/{id}/

Method: GET
Link: http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/api/providers/2/
Response code: 200
Example response body
```json
{
"id": 2,
"name": "Provider 2",
"email": "user2@gmail.com",
"phone_number": "+917611182253",
"language": "En",
"currency": "USD",
"created_at": "2021-07-11T07:10:27.771110Z",
"updated_at": "2021-07-11T07:10:27.775267Z"
}
```

4. api/providers/{id}/

Method: PATCH
Link: http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/api/providers/2/
Response code: 200
Example response body
```json
{
  "name": "Provider 2",
  "email": "user2@gmail.com",
  "phone_number": "+917611182253",
  "language": "En",
  "currency": "INR",
}
```

5. api/providers/{id}/

Method: DELETE
Link: http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/api/providers/3/
Response code: 204
Example response body

####Service Area API's

1. api/service-areas/

Method: GET
Link: http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/api/service-areas/
Response code: 200
Example response body
```json
[
  {
    "id": 1,
    "service_provider": 1,
    "provider_name": "Alex",
    "name": "Example Area 1",
    "price": "400.00",
    "service_area": "SRID=4326;POLYGON ((8.162841796875 28.23664944401447, 8.206787109375 28.30438068296278, 7.086181640625 24.0765591202954, 11.18408203125 24.09661861127878, 11.62353515625 27.91676664124907, 8.162841796875 28.23664944401447))",
    "created_at": "2021-07-11T07:28:23.073157Z",
    "updated_at": "2021-07-11T07:28:23.077652Z"
  }
]

```

2. api/service-areas/

Method: POST
Link: http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/api/service-areas/
Response code: 201
Example post data
```json
{
    "service_provider": 1,
    "provider_name": "Alex",
    "name": "Example Area 1",
    "price": "400.00",
    "service_area": "SRID=4326;POLYGON ((8.162841796875 28.23664944401447, 8.206787109375 28.30438068296278, 7.086181640625 24.0765591202954, 11.18408203125 24.09661861127878, 11.62353515625 27.91676664124907, 8.162841796875 28.23664944401447))",
}
```

Example response body
```json
{
    "service_provider": 1,
    "provider_name": "Alex",
    "name": "Example Area 1",
    "price": "400.00",
    "service_area": "SRID=4326;POLYGON ((8.162841796875 28.23664944401447, 8.206787109375 28.30438068296278, 7.086181640625 24.0765591202954, 11.18408203125 24.09661861127878, 11.62353515625 27.91676664124907, 8.162841796875 28.23664944401447))",
    "created_at": "2021-07-11T07:28:23.073157Z",
    "updated_at": "2021-07-11T07:28:23.077652Z"
}
```

3. api/service-areas/{id}/

Method: GET
Link: http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/api/service-areas/1/
Response code: 200
Example response body
```json
{
"id": 1,
"service_provider": 1,
"provider_name": "Alex",
"name": "Example Area 1",
"price": "400.00",
"service_area": "SRID=4326;POLYGON ((8.162841796875 28.23664944401447, 8.206787109375 28.30438068296278, 7.086181640625 24.0765591202954, 11.18408203125 24.09661861127878, 11.62353515625 27.91676664124907, 8.162841796875 28.23664944401447))",
"created_at": "2021-07-11T07:28:23.073157Z",
"updated_at": "2021-07-11T07:28:23.077652Z"
}
```

4. api/service-areas/{id}/

Method: PATCH
Link: http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/api/service-areas/1/
Response code: 200
Example response body
```json
{
"id": 1,
"service_provider": 1,
"provider_name": "Alex",
"name": "Example Area 1",
"price": "500.00",
"service_area": "SRID=4326;POLYGON ((8.162841796875 28.23664944401447, 8.206787109375 28.30438068296278, 7.086181640625 24.0765591202954, 11.18408203125 24.09661861127878, 11.62353515625 27.91676664124907, 8.162841796875 28.23664944401447))",
"created_at": "2021-07-11T07:28:23.073157Z",
"updated_at": "2021-07-11T07:28:23.077652Z"
}
```

5. api/service-areas/{id}/

Method: DELETE
Link: http://ec2-18-118-13-226.us-east-2.compute.amazonaws.com/api/service-areas/2/
Response code: 204
Example response body


# Installation
### Prerequisites
- Install `docker` and `docker-compose`.
### Setup code
- Clone the project using 
	```git clone https://github.com/prabhakar1998/service_area.git```
### Setup docker container
- In the root directory run command `make build`. This builds and starts the app.
- Enter an interactive session on the container  by running `make container` to create super user, run tests and migrate db in the container.
     - Apply migrations  by running `make migrate`
     - Create super user by running `make createsuperuser`
     - Run the tests by running `make test` .
     - Run the development server by running `make run` 
### API Doc 
- To view API doc and use REST API endpoints, Open `http://localhost:8000` in browser and 
   check swagger UI page.
  which can be used to  call REST API endpoints.
- Login with the super user credentials. Use all the API end points using `Try it out`
