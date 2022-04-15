import unittest
from pds.api_client import Configuration
from pds.api_client import ApiClient
from pds.api_client.api.bundles_collections_api import BundlesCollectionsApi


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # create an instance of the API class
        configuration = Configuration()
        configuration.host = 'http://localhost:8081'
        api_client = ApiClient(configuration)
        self.bundlesCollections = BundlesCollectionsApi(api_client)

    def test_collections_of_a_bundle_default(self):

        results = self.bundlesCollections.collections_of_a_bundle(
            'urn:nasa:pds:insight_rad::2.1',
            fields=['ops:Data_File_Info.ops:file_ref']
        )
        for collection in results.data:
            urls = collection.properties['ops:Data_File_Info.ops:file_ref']
            for url in urls:
                #TODO: make actual assert verification
                print(url)


if __name__ == '__main__':
    unittest.main()
