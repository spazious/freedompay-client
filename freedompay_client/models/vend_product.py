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


class VendProduct(object):
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
        'id': 'str',
        'tag': 'str',
        'product_code': 'str',
        'unit_of_measure': 'str',
        'unit_price': 'str',
        'max_qty': 'str',
        'options': 'str',
        'price_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tag': 'tag',
        'product_code': 'productCode',
        'unit_of_measure': 'unitOfMeasure',
        'unit_price': 'unitPrice',
        'max_qty': 'maxQty',
        'options': 'options',
        'price_code': 'priceCode'
    }

    def __init__(self, id=None, tag=None, product_code=None, unit_of_measure=None, unit_price=None, max_qty=None, options=None, price_code=None, _configuration=None):  # noqa: E501
        """VendProduct - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._tag = None
        self._product_code = None
        self._unit_of_measure = None
        self._unit_price = None
        self._max_qty = None
        self._options = None
        self._price_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tag is not None:
            self.tag = tag
        if product_code is not None:
            self.product_code = product_code
        if unit_of_measure is not None:
            self.unit_of_measure = unit_of_measure
        if unit_price is not None:
            self.unit_price = unit_price
        if max_qty is not None:
            self.max_qty = max_qty
        if options is not None:
            self.options = options
        if price_code is not None:
            self.price_code = price_code

    @property
    def id(self):
        """Gets the id of this VendProduct.  # noqa: E501


        :return: The id of this VendProduct.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VendProduct.


        :param id: The id of this VendProduct.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def tag(self):
        """Gets the tag of this VendProduct.  # noqa: E501


        :return: The tag of this VendProduct.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this VendProduct.


        :param tag: The tag of this VendProduct.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def product_code(self):
        """Gets the product_code of this VendProduct.  # noqa: E501


        :return: The product_code of this VendProduct.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this VendProduct.


        :param product_code: The product_code of this VendProduct.  # noqa: E501
        :type: str
        """

        self._product_code = product_code

    @property
    def unit_of_measure(self):
        """Gets the unit_of_measure of this VendProduct.  # noqa: E501


        :return: The unit_of_measure of this VendProduct.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """Sets the unit_of_measure of this VendProduct.


        :param unit_of_measure: The unit_of_measure of this VendProduct.  # noqa: E501
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def unit_price(self):
        """Gets the unit_price of this VendProduct.  # noqa: E501


        :return: The unit_price of this VendProduct.  # noqa: E501
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this VendProduct.


        :param unit_price: The unit_price of this VendProduct.  # noqa: E501
        :type: str
        """

        self._unit_price = unit_price

    @property
    def max_qty(self):
        """Gets the max_qty of this VendProduct.  # noqa: E501


        :return: The max_qty of this VendProduct.  # noqa: E501
        :rtype: str
        """
        return self._max_qty

    @max_qty.setter
    def max_qty(self, max_qty):
        """Sets the max_qty of this VendProduct.


        :param max_qty: The max_qty of this VendProduct.  # noqa: E501
        :type: str
        """

        self._max_qty = max_qty

    @property
    def options(self):
        """Gets the options of this VendProduct.  # noqa: E501


        :return: The options of this VendProduct.  # noqa: E501
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this VendProduct.


        :param options: The options of this VendProduct.  # noqa: E501
        :type: str
        """

        self._options = options

    @property
    def price_code(self):
        """Gets the price_code of this VendProduct.  # noqa: E501


        :return: The price_code of this VendProduct.  # noqa: E501
        :rtype: str
        """
        return self._price_code

    @price_code.setter
    def price_code(self, price_code):
        """Sets the price_code of this VendProduct.


        :param price_code: The price_code of this VendProduct.  # noqa: E501
        :type: str
        """

        self._price_code = price_code

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
        if issubclass(VendProduct, dict):
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
        if not isinstance(other, VendProduct):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VendProduct):
            return True

        return self.to_dict() != other.to_dict()