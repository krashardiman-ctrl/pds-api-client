
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

There is a bug with version 4.3.1 which make the following request generate a broken API package:

    openapi-generator generate -g python -i swagger.json --package-name pds.api_client --additional-properties=packageVersion=0.2.0

A fork and pull request has been made to correct that. To use the patched version, do:

    git clone https://github.com/tloubrieu-jpl/openapi-generator.git
    cd  openapi-generator
    ./mvnw clean package
    
Run the generation:

    java -jar /Users/loubrieu/tmp/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate  -g python-legacy -i swagger.json --package-name pds.api_client --additional-properties=packageVersion=0.6.1


    
  
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
    sphinx-apidoc -o source/api ../pds/api_client
    make html
    cp -r docs/build/html /tmp/
    
 Publish on github
 
    cd ..
    git checkout gh-pages
    cp -r /tmp/html/* . 
        
    
    
    
    
    
    