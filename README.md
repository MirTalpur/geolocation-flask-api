[![Build Status](https://travis-ci.org/MirTalpur/geolocation-flask-api.svg?branch=master)](https://travis-ci.org/MirTalpur/geolocation-flask-api)
# geolocation-flask-api
Leverages Google Geo location and Geo coder API to create RESTFUL endpoints for latitude and longitude data given a physical address

# Pre-reqs
### Virtualenv
Is an virtual environment which will let configure different python projects easily and manage dependencies much simpler.

### Install pip (recommended)
Pip is a package management system used to install and manage software packages, such as those found in the Python Package Index.
Although pip isn't necessary it is highly recommended for local development

### Docker
Docker allows for containerized applications.

# Local Development
Local development can be done using ```requirments.txt```
### Setup

#### Create a virtualenv
```virtualenv <project_name>```

#### Start using the virtualenv
```source <project_name>/bin/activate```

#### Install requirments
```pip install -r requirements.txt```

#### Export ENV Variables (not needed if you want to build just with docker)
```
EXPORT GOOGLE_API_KEY=<YOUR_GOOGLE_KEY>
EXPORT GEOCODER_APP_ID=<YOUR_GEOCODER_APP_ID>
EXPORT GEOCODER_APP_CODE=<YOUR_GEOCODER_APP_CODE>
```

#### Update main.env with api keys from google maps API and App ID and App Code from developer.here
This is needed for docker
```
GOOGLE_API_KEY=<YOUR_GOOGLE_KEY>
GEOCODER_APP_ID=<YOUR_GEOCODER_APP_ID>
GEOCODER_APP_CODE=<YOUR_GEOCODER_APP_CODE>
```

#### Run geolocation __init__.py
```python geolocation/__init__.py```


Now the application will be running on localhost and port 3000

# API endpoints
#### Endpoint
#### Post and Get
```v1/geolocation```

#### Return data
```json
{
    "data": [
        {
            "latitude": 39.66154,
            "longitude": -124.49674
        }
    ]
}
```

#### Get requires query parameter of address
```
curl v1/geolocation?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA
```

#### Post requires body of address
```
curl --data "address=1600 Amphitheatre Parkway,Mountain+View,CA" v1/geolocation
```

# Tests
The tests require the package of geolocation be available for use. Use setup.py to achieve this
```
pip install --editable .
export FLASK_APP=geolocation
export FLASK_DEBUG=true
flask run
```
And than we can run the tests
```
python tests/test_geolocation.py 
```

# To run with docker from Docker repository
With docker we can build the image locally and run it however, the image is already in a public docker repo so we 
can just simply run it with updated values in main.env
### Note we can just use Docker to do our entire development locally as well

#### Run docker image from public docker repo
```docker run -d --env-file=main.env -p 4000:3000 hskalee123/geolocation:latest```

#### Build docker image locally and than run from root directory
```
docker build -t geolocation .
docker run -d --env-file=main.env -p 4000:3000 geolocation
```

```
curl --data "address=1600 Amphitheatre Parkway,Mountain+View,CA" localhost:4000/v1/geolocation
```
