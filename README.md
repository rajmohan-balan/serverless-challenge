# serverless-challenge

An arbitrary collection of roles and users. Function to accept parent id and returns child nodes.




# Pre-requisites

* Docker
* Docker Compose
* Make



## Checkout

```bash
git clone https://github.com/rajmohan-balan/serverless-challenge.git
cd ./serverless-challenge
```

## Configure

Generate a new .env file.

```bash
make .env
```



## Dependencies

Installation of dev dependency packages to run the function locally using **serverless-offline-python**

```bash
make deps
```



## Build

Build package is compile the source code and bundle into package folder and setting up venv to run python:

```bash
make build
```



Run the service locally:

```bash
make offline
```



## API Requests



###### /getSubOrdinates:

```
curl --location --request POST 'http://0.0.0.0:3000/getSubOrdinates' \
--header 'Content-Type: application/json' \
--data-raw '{
    "parentId": 3
}'
```

###### /setRoles:

```
curl --location --request POST 'http://0.0.0.0:3000/setRoles' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "Id": 1,
        "Name": "System Administrator",
        "Parent": 0
    },
    {
        "Id": 2,
        "Name": "Location Manager",
        "Parent": 1
    },
    {
        "Id": 3,
        "Name": "Supervisor",
        "Parent": 2
    },
    {
        "Id": 4,
        "Name": "Employee",
        "Parent": 3
    },
    {
        "Id": 5,
        "Name": "Trainer",
        "Parent": 3
    }
]'
```



###### /setUsers:

```
curl --location --request POST 'http://0.0.0.0:3000/setUsers' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "Id": 1,
        "Name": "Adam Admin",
        "Role": 1
    },
    {
        "Id": 2,
        "Name": "Emily Employee",
        "Role": 4
    },
    {
        "Id": 3,
        "Name": "Sam Supervisor",
        "Role": 3
    },
    {
        "Id": 4,
        "Name": "Mary Manager",
        "Role": 2
    },
    {
        "Id": 5,
        "Name": "Steve Trainer",
        "Role": 5
    }
]'
```

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.getpostman.com/collections/63002181d27bb85c1965)

## Lint

```bash
make pylint
```

## 

## Unit Test

```bash
make testUnit
```

## 

## Unit Test with Code Coverage

```bash
make testUnitWithCoverage
```

## 

## Integration Test

```bash
make testIntegration
```

## 