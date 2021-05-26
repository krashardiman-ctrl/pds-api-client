from __future__ import print_function
from pds.api_client.rest import ApiException
from pds.api_client import Configuration
from pds.api_client import ApiClient
from pds.api_client import CollectionsApi
from pprint import pprint

# create an instance of the API class
configuration = Configuration()
configuration.host = 'http://pds-gamma.jpl.nasa.gov/api/'
#configuration.host = 'http://localhost:8080/'
api_client = ApiClient(configuration)
collections = CollectionsApi(api_client)

try:
    api_response = collections.get_collection(start=0, limit=20)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->get_collection: %s\n" % e)