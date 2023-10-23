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

from freedompay_client.models.item import Item  # noqa: E501

class TestItem(unittest.TestCase):
    """Item unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Item:
        """Test Item
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Item`
        """
        model = Item()  # noqa: E501
        if include_optional:
            return Item(
                discount_amount = '',
                discount_flag = '',
                tax_included_flag = '',
                product_code = '',
                product_upc = '',
                product_sku = '',
                product_name = '',
                product_description = '',
                product_make = '',
                product_model = '',
                product_part_number = '',
                commodity_code = '',
                product_year = '',
                product_serial1 = '',
                product_serial2 = '',
                product_serial3 = '',
                customer_asset_id = '',
                category = '',
                sub_category = '',
                unit_price = '',
                quantity = '',
                total_amount = '',
                tax_amount = '',
                promo_code = '',
                freight_amount = '',
                unit_of_measure = '',
                sale_code = '',
                custom_format_id = '',
                custom1 = '',
                custom2 = '',
                custom3 = '',
                custom4 = '',
                custom5 = '',
                custom6 = '',
                custom7 = '',
                custom8 = '',
                custom9 = '',
                pay_alloc = '',
                alloc_code = '',
                eid_indicator = '',
                orig_unit_price = '',
                orig_total_amount = '',
                eid_detail = [
                    freedompay_client.models.eid_detail.EIDDetail(
                        discount_key = '', 
                        code = '', 
                        qty = '', 
                        offset = '', 
                        total_amount = '', )
                    ],
                tax_detail = [
                    freedompay_client.models.tax_detail_item.TaxDetailItem(
                        type = '', 
                        amount = '', )
                    ],
                id = '',
                tag = ''
            )
        else:
            return Item(
        )
        """

    def testItem(self):
        """Test Item"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
