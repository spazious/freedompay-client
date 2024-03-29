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

from freedompay_client.models.security_code_control import SecurityCodeControl  # noqa: E501

class TestSecurityCodeControl(unittest.TestCase):
    """SecurityCodeControl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecurityCodeControl:
        """Test SecurityCodeControl
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecurityCodeControl`
        """
        model = SecurityCodeControl()  # noqa: E501
        if include_optional:
            return SecurityCodeControl(
                label_type = 'Unknown',
                mask_type = 'Default',
                placeholder_type = 'Unknown',
                validation_type = 'Unknown'
            )
        else:
            return SecurityCodeControl(
        )
        """

    def testSecurityCodeControl(self):
        """Test SecurityCodeControl"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
