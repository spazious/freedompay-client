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

from freedompay_client.models.request_incentives import RequestIncentives  # noqa: E501

class TestRequestIncentives(unittest.TestCase):
    """RequestIncentives unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestIncentives:
        """Test RequestIncentives
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestIncentives`
        """
        model = RequestIncentives()  # noqa: E501
        if include_optional:
            return RequestIncentives(
                system_id = '',
                incentives = [
                    freedompay_client.models.incentive_incentive.IncentiveIncentive(
                        id = '', 
                        presented = '', 
                        accepted = '', 
                        tender_request_id = '', )
                    ]
            )
        else:
            return RequestIncentives(
        )
        """

    def testRequestIncentives(self):
        """Test RequestIncentives"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
