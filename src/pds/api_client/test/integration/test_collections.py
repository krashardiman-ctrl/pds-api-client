import unittest
from pds.api_client.rest import ApiException
from pds.api_client import Configuration
from pds.api_client import ApiClient
from pds.api_client.api.collections_api import CollectionsApi


class CollectionsApiTestCase(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        configuration = Configuration()
        configuration.host = 'http://localhost:8080'
        api_client = ApiClient(configuration)
        self.collections = CollectionsApi(api_client)

    def test_all_collections(self):

        api_response = self.collections.get_collection(start=0, limit=20)
        assert len(api_response['data']) == 3
        assert api_response['summary']['hits'] == 3

        assert all(['id' in c for c in api_response['data']])

        # select one collection with lidvid 'urn:nasa:pds:insight_rad:data_calibrated::7.0'
        collection = [c for c in api_response['data'] if c['id'] == 'urn:nasa:pds:insight_rad:data_calibrated::7.0'][0]
        assert 'type' in collection
        assert collection['type'] == 'Product_Collection'

        assert 'title' in collection
        assert collection['title'] == 'InSight RAD Calibrated Data Collection'

    def test_collection_by_lidvid_all(self):
        collection = self.collections.collections_by_lidvid_all('urn:nasa:pds:insight_rad:data_calibrated::7.0')
        assert 'id' in collection
        assert collection['id'] == 'urn:nasa:pds:insight_rad:data_calibrated::7.0'

    @unittest.skip('does not work')
    def test_collection_by_lidvid_all_content_type(self):
        collection = self.collections.collections_by_lidvid_all(
            'urn:nasa:pds:insight_rad:data_calibrated::7.0',
            accept_content_types='application/vnd.nasa.pds.pds4+json'
        )
        assert 'id' in collection

if __name__ == '__main__':
    unittest.main()
