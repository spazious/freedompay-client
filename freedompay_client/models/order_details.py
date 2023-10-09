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


class OrderDetails(object):
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
        'transaction_total': 'float',
        'currency_code': 'str',
        'order_number': 'str',
        'order_description': 'str'
    }

    attribute_map = {
        'transaction_total': 'TransactionTotal',
        'currency_code': 'CurrencyCode',
        'order_number': 'OrderNumber',
        'order_description': 'OrderDescription'
    }

    def __init__(self, transaction_total=None, currency_code=None, order_number=None, order_description=None, _configuration=None):  # noqa: E501
        """OrderDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_total = None
        self._currency_code = None
        self._order_number = None
        self._order_description = None
        self.discriminator = None

        if transaction_total is not None:
            self.transaction_total = transaction_total
        if currency_code is not None:
            self.currency_code = currency_code
        if order_number is not None:
            self.order_number = order_number
        if order_description is not None:
            self.order_description = order_description

    @property
    def transaction_total(self):
        """Gets the transaction_total of this OrderDetails.  # noqa: E501


        :return: The transaction_total of this OrderDetails.  # noqa: E501
        :rtype: float
        """
        return self._transaction_total

    @transaction_total.setter
    def transaction_total(self, transaction_total):
        """Sets the transaction_total of this OrderDetails.


        :param transaction_total: The transaction_total of this OrderDetails.  # noqa: E501
        :type: float
        """

        self._transaction_total = transaction_total

    @property
    def currency_code(self):
        """Gets the currency_code of this OrderDetails.  # noqa: E501


        :return: The currency_code of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this OrderDetails.


        :param currency_code: The currency_code of this OrderDetails.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def order_number(self):
        """Gets the order_number of this OrderDetails.  # noqa: E501


        :return: The order_number of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this OrderDetails.


        :param order_number: The order_number of this OrderDetails.  # noqa: E501
        :type: str
        """

        self._order_number = order_number

    @property
    def order_description(self):
        """Gets the order_description of this OrderDetails.  # noqa: E501


        :return: The order_description of this OrderDetails.  # noqa: E501
        :rtype: str
        """
        return self._order_description

    @order_description.setter
    def order_description(self, order_description):
        """Sets the order_description of this OrderDetails.


        :param order_description: The order_description of this OrderDetails.  # noqa: E501
        :type: str
        """

        self._order_description = order_description

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
        if issubclass(OrderDetails, dict):
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
        if not isinstance(other, OrderDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderDetails):
            return True

        return self.to_dict() != other.to_dict()
