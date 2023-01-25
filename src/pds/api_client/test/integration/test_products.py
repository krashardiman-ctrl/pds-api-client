import unittest
from pds.api_client import Configuration
from pds.api_client import ApiClient

from pds.api_client.apis.paths.products import Products


class ProductsCase(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        configuration = Configuration()
        configuration.host = 'http://localhost:8080'
        api_client = ApiClient(configuration)
        self.products = Products(api_client)

    def test_products_by_keywords(self):
        results = self.products.get(
            query_params={'keywords': ['insight']},
            accept_content_types=('application/json',)
        ).body

        self.assertEqual(len(results.data), 17)  # add assertion here


if __name__ == '__main__':
    unittest.main()
