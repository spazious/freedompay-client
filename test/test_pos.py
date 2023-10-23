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

from freedompay_client.models.pos import Pos  # noqa: E501

class TestPos(unittest.TestCase):
    """Pos unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Pos:
        """Test Pos
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Pos`
        """
        model = Pos()  # noqa: E501
        if include_optional:
            return Pos(
                register_number = '',
                entry_mode = '',
                track1 = '',
                track2 = '',
                track3 = '',
                track_ksn = '',
                sequence_number = '',
                card_present = '',
                track1e = '',
                track2e = '',
                track1len = '',
                track2len = '',
                tracke = '',
                enc_mode = '',
                msr_type = '',
                payment_date = '',
                chip_data = '',
                issuer_script_results = '',
                caps = '',
                fallback_reason = '',
                sig_data = ''
            )
        else:
            return Pos(
        )
        """

    def testPos(self):
        """Test Pos"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()