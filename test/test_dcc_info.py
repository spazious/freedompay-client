# coding: utf-8

"""
    Hosted Payment Controls API Documentation v1.5

    The API for Hosted Payment Controls. To access the swagger.json file open the following link: https://hpc.uat.freedompay.com/api/swagger/docs/v1.5

    The version of the OpenAPI document: v1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from freedompay_client.models.dcc_info import DccInfo  # noqa: E501

class TestDccInfo(unittest.TestCase):
    """DccInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DccInfo:
        """Test DccInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DccInfo`
        """
        model = DccInfo()  # noqa: E501
        if include_optional:
            return DccInfo(
                enabled = '',
                exchange_rate = '',
                foreign_amount = '',
                foreign_currency = '',
                host_data = ''
            )
        else:
            return DccInfo(
        )
        """

    def testDccInfo(self):
        """Test DccInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
