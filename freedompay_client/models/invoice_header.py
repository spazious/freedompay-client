# coding: utf-8

"""
    Hosted Payment Controls API Documentation v1.5

    The API for Hosted Payment Controls. To access the swagger.json file open the following link: https://hpc.uat.freedompay.com/api/swagger/docs/v1.5  # noqa: E501

    OpenAPI spec version: v1.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from freedompay_client.configuration import Configuration


class InvoiceHeader(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'invoice_number': 'str',
        'invoice_date': 'str',
        'merchant_descriptor': 'str',
        'merchant_descriptor_contact': 'str',
        'merchant_descriptor_url': 'str',
        'purchaser_code': 'str',
        'purchaser_order_date': 'str',
        'goods_indicator': 'str',
        'customer_po': 'str',
        'product_code_standard': 'str',
        'eid_indicator': 'str'
    }

    attribute_map = {
        'invoice_number': 'invoiceNumber',
        'invoice_date': 'invoiceDate',
        'merchant_descriptor': 'merchantDescriptor',
        'merchant_descriptor_contact': 'merchantDescriptorContact',
        'merchant_descriptor_url': 'merchantDescriptorUrl',
        'purchaser_code': 'purchaserCode',
        'purchaser_order_date': 'purchaserOrderDate',
        'goods_indicator': 'goodsIndicator',
        'customer_po': 'customerPO',
        'product_code_standard': 'productCodeStandard',
        'eid_indicator': 'eidIndicator'
    }

    def __init__(self, invoice_number=None, invoice_date=None, merchant_descriptor=None, merchant_descriptor_contact=None, merchant_descriptor_url=None, purchaser_code=None, purchaser_order_date=None, goods_indicator=None, customer_po=None, product_code_standard=None, eid_indicator=None, _configuration=None):  # noqa: E501
        """InvoiceHeader - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._invoice_number = None
        self._invoice_date = None
        self._merchant_descriptor = None
        self._merchant_descriptor_contact = None
        self._merchant_descriptor_url = None
        self._purchaser_code = None
        self._purchaser_order_date = None
        self._goods_indicator = None
        self._customer_po = None
        self._product_code_standard = None
        self._eid_indicator = None
        self.discriminator = None

        if invoice_number is not None:
            self.invoice_number = invoice_number
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if merchant_descriptor is not None:
            self.merchant_descriptor = merchant_descriptor
        if merchant_descriptor_contact is not None:
            self.merchant_descriptor_contact = merchant_descriptor_contact
        if merchant_descriptor_url is not None:
            self.merchant_descriptor_url = merchant_descriptor_url
        if purchaser_code is not None:
            self.purchaser_code = purchaser_code
        if purchaser_order_date is not None:
            self.purchaser_order_date = purchaser_order_date
        if goods_indicator is not None:
            self.goods_indicator = goods_indicator
        if customer_po is not None:
            self.customer_po = customer_po
        if product_code_standard is not None:
            self.product_code_standard = product_code_standard
        if eid_indicator is not None:
            self.eid_indicator = eid_indicator

    @property
    def invoice_number(self):
        """Gets the invoice_number of this InvoiceHeader.  # noqa: E501


        :return: The invoice_number of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this InvoiceHeader.


        :param invoice_number: The invoice_number of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def invoice_date(self):
        """Gets the invoice_date of this InvoiceHeader.  # noqa: E501


        :return: The invoice_date of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this InvoiceHeader.


        :param invoice_date: The invoice_date of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._invoice_date = invoice_date

    @property
    def merchant_descriptor(self):
        """Gets the merchant_descriptor of this InvoiceHeader.  # noqa: E501


        :return: The merchant_descriptor of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._merchant_descriptor

    @merchant_descriptor.setter
    def merchant_descriptor(self, merchant_descriptor):
        """Sets the merchant_descriptor of this InvoiceHeader.


        :param merchant_descriptor: The merchant_descriptor of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._merchant_descriptor = merchant_descriptor

    @property
    def merchant_descriptor_contact(self):
        """Gets the merchant_descriptor_contact of this InvoiceHeader.  # noqa: E501


        :return: The merchant_descriptor_contact of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._merchant_descriptor_contact

    @merchant_descriptor_contact.setter
    def merchant_descriptor_contact(self, merchant_descriptor_contact):
        """Sets the merchant_descriptor_contact of this InvoiceHeader.


        :param merchant_descriptor_contact: The merchant_descriptor_contact of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._merchant_descriptor_contact = merchant_descriptor_contact

    @property
    def merchant_descriptor_url(self):
        """Gets the merchant_descriptor_url of this InvoiceHeader.  # noqa: E501


        :return: The merchant_descriptor_url of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._merchant_descriptor_url

    @merchant_descriptor_url.setter
    def merchant_descriptor_url(self, merchant_descriptor_url):
        """Sets the merchant_descriptor_url of this InvoiceHeader.


        :param merchant_descriptor_url: The merchant_descriptor_url of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._merchant_descriptor_url = merchant_descriptor_url

    @property
    def purchaser_code(self):
        """Gets the purchaser_code of this InvoiceHeader.  # noqa: E501


        :return: The purchaser_code of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._purchaser_code

    @purchaser_code.setter
    def purchaser_code(self, purchaser_code):
        """Sets the purchaser_code of this InvoiceHeader.


        :param purchaser_code: The purchaser_code of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._purchaser_code = purchaser_code

    @property
    def purchaser_order_date(self):
        """Gets the purchaser_order_date of this InvoiceHeader.  # noqa: E501


        :return: The purchaser_order_date of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._purchaser_order_date

    @purchaser_order_date.setter
    def purchaser_order_date(self, purchaser_order_date):
        """Sets the purchaser_order_date of this InvoiceHeader.


        :param purchaser_order_date: The purchaser_order_date of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._purchaser_order_date = purchaser_order_date

    @property
    def goods_indicator(self):
        """Gets the goods_indicator of this InvoiceHeader.  # noqa: E501


        :return: The goods_indicator of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._goods_indicator

    @goods_indicator.setter
    def goods_indicator(self, goods_indicator):
        """Sets the goods_indicator of this InvoiceHeader.


        :param goods_indicator: The goods_indicator of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._goods_indicator = goods_indicator

    @property
    def customer_po(self):
        """Gets the customer_po of this InvoiceHeader.  # noqa: E501


        :return: The customer_po of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._customer_po

    @customer_po.setter
    def customer_po(self, customer_po):
        """Sets the customer_po of this InvoiceHeader.


        :param customer_po: The customer_po of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._customer_po = customer_po

    @property
    def product_code_standard(self):
        """Gets the product_code_standard of this InvoiceHeader.  # noqa: E501


        :return: The product_code_standard of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._product_code_standard

    @product_code_standard.setter
    def product_code_standard(self, product_code_standard):
        """Sets the product_code_standard of this InvoiceHeader.


        :param product_code_standard: The product_code_standard of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._product_code_standard = product_code_standard

    @property
    def eid_indicator(self):
        """Gets the eid_indicator of this InvoiceHeader.  # noqa: E501


        :return: The eid_indicator of this InvoiceHeader.  # noqa: E501
        :rtype: str
        """
        return self._eid_indicator

    @eid_indicator.setter
    def eid_indicator(self, eid_indicator):
        """Sets the eid_indicator of this InvoiceHeader.


        :param eid_indicator: The eid_indicator of this InvoiceHeader.  # noqa: E501
        :type: str
        """

        self._eid_indicator = eid_indicator

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InvoiceHeader, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InvoiceHeader):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvoiceHeader):
            return True

        return self.to_dict() != other.to_dict()
