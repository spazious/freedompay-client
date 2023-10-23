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

from freedompay_client.models.pay_pal_init_request import PayPalInitRequest  # noqa: E501

class TestPayPalInitRequest(unittest.TestCase):
    """PayPalInitRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayPalInitRequest:
        """Test PayPalInitRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayPalInitRequest`
        """
        model = PayPalInitRequest()  # noqa: E501
        if include_optional:
            return PayPalInitRequest(
                commit = True,
                disabled = True,
                disable_funding = '',
                intent = 'Unknown',
                invoice_number = '',
                payment_method_payee_preferred = 'Unknown',
                shipping_preference = 'Unknown',
                total_price = '',
                country_code = '',
                currency_code = '',
                debug = True,
                locale = '',
                culture_code = '',
                es_key = '',
                legal = freedompay_client.models.legal_control.LegalControl(
                    hide_checkbox = True, 
                    text_type = 'Unknown', ),
                store_id = '',
                styles = '',
                terminal_id = '',
                validation_message_type = 'Unknown',
                reference_id = '00000000-0000-0000-0000-000000000000'
            )
        else:
            return PayPalInitRequest(
        )
        """

    def testPayPalInitRequest(self):
        """Test PayPalInitRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
