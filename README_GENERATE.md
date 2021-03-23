
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

    openapi-generator generate -g python -i swagger.json --package-name pds.api_client --additional-properties=packageVersion=0.2.0
     
  
## Install it
    
    pip install -r requirements.txt
    python setup.py install
    
## Test it

    python client-demo.py
    
## Publish it on pypi

    python setup.py sdist bdist_wheel
    twine upload --repository testpypi dist/*
    
# Generate documentation 

    cd docs
    sphinx-apidoc -o docs/source/api pds/api_client
    make html
    
 Publish on github
 
    git checkout gh-pages
        
    
    
    
    
    
    