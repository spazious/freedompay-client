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

from freedompay_client.models.network_data import NetworkData  # noqa: E501

class TestNetworkData(unittest.TestCase):
    """NetworkData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkData:
        """Test NetworkData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkData`
        """
        model = NetworkData()  # noqa: E501
        if include_optional:
            return NetworkData(
                network = '',
                stan = '',
                aci = '',
                tdcc = '',
                pcode = '',
                vcode = '',
                downgrade_code = '',
                cvc_error = '',
                data_error = '',
                auth_source = '',
                response_code = '',
                product_id = '',
                program_id = '',
                merchant_advice = '',
                service_option = '',
                fleet_prompts = '',
                custom_data = [
                    freedompay_client.models.network_custom_data.NetworkCustomData(
                        data = [
                            ''
                            ], 
                        code = '', )
                    ],
                mac = '',
                pos_seq_num = '',
                mac_key = '',
                pin_key = '',
                field_key = '',
                trans_date = '',
                trans_time = '',
                host_control_data = ''
            )
        else:
            return NetworkData(
        )
        """

    def testNetworkData(self):
        """Test NetworkData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()