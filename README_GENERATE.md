
# Scope

Automatically generates a python client library from OpenApi specification of the PDS federated API (see https://app.swaggerhub.com/apis/PDS_APIs/pds_federated_api/0.0#/info) 

# Requisites

  - code generator https://github.com/OpenAPITools/openapi-generator
  - python 3.7
  
# Procedure

## Get repository updates

First time

    git clone https://github.com/NASA-PDS/pds-api-client.git

Then:

    git pull    


## Generate the library

    openapi-generator generate -g python -i swagger.json --package-name pds.api_client
  
 Change manually the version in setup.py accordingly with the swagger specification version.
  
## Install it
    
    pip install -r requirements.txt
    python setup.py install
    
## Test it

    python client-demo.py
    
## Publish it on pypi

    python setup.py sdist bdist_wheel
    twine upload --repository testpypi dist/*
    
## To do 

    Publish the documentation and make it accessible from pypi deployment.
    
    
    
    
    
    
    