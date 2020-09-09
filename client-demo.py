from __future__ import print_function
import pds_api_client
from pds_api_client.rest import ApiException
from pds_api_client import Configuration
from pprint import pprint

# create an instance of the API class
configuration = Configuration()
configuration.host = 'http://localhost:8080/'
api_instance = pds_api_client.CollectionsApi(pds_api_client.ApiClient(configuration))

try:
    # capabilities api entry point, list the resources provided by the current API end-point.
    api_response = api_instance.get_collection(q="", start=0, limit=20)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->get_collection: %s\n" % e)