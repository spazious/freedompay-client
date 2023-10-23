# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import freedompay-client
from freedompay-client.paths.v1_5_controls_init_paypal import post  # noqa: E501
from freedompay-client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV15ControlsInitPaypal(ApiTestMixin, unittest.TestCase):
    """
    V15ControlsInitPaypal unit test stubs
        Initializes a PayPal payment request workflow.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()