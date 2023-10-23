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

from freedompay_client.models.fraud_check_service import FraudCheckService  # noqa: E501

class TestFraudCheckService(unittest.TestCase):
    """FraudCheckService unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FraudCheckService:
        """Test FraudCheckService
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FraudCheckService`
        """
        model = FraudCheckService()  # noqa: E501
        if include_optional:
            return FraudCheckService(
                reference_id = '',
                option = '',
                mode = '',
                device_identifier = '',
                commerce_indicator = '',
                site_identifier = '',
                customer_since_date = '',
                estimated_total_amount = '',
                properties = [
                    freedompay_client.models.user_defined_field.UserDefinedField(
                        name = '', 
                        value = '', )
                    ],
                run_risk_model = '',
                order = '',
                void_threshold = '',
                auth_data = '',
                captcha_data = '',
                fail_count = '',
                failed_requests = [
                    ''
                    ],
                run = ''
            )
        else:
            return FraudCheckService(
        )
        """

    def testFraudCheckService(self):
        """Test FraudCheckService"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
