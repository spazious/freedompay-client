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


class DccInfo(object):
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
        'enabled': 'str',
        'exchange_rate': 'str',
        'foreign_amount': 'str',
        'foreign_currency': 'str',
        'host_data': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'exchange_rate': 'exchangeRate',
        'foreign_amount': 'foreignAmount',
        'foreign_currency': 'foreignCurrency',
        'host_data': 'hostData'
    }

    def __init__(self, enabled=None, exchange_rate=None, foreign_amount=None, foreign_currency=None, host_data=None, _configuration=None):  # noqa: E501
        """DccInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enabled = None
        self._exchange_rate = None
        self._foreign_amount = None
        self._foreign_currency = None
        self._host_data = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if foreign_amount is not None:
            self.foreign_amount = foreign_amount
        if foreign_currency is not None:
            self.foreign_currency = foreign_currency
        if host_data is not None:
            self.host_data = host_data

    @property
    def enabled(self):
        """Gets the enabled of this DccInfo.  # noqa: E501


        :return: The enabled of this DccInfo.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DccInfo.


        :param enabled: The enabled of this DccInfo.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this DccInfo.  # noqa: E501


        :return: The exchange_rate of this DccInfo.  # noqa: E501
        :rtype: str
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this DccInfo.


        :param exchange_rate: The exchange_rate of this DccInfo.  # noqa: E501
        :type: str
        """

        self._exchange_rate = exchange_rate

    @property
    def foreign_amount(self):
        """Gets the foreign_amount of this DccInfo.  # noqa: E501


        :return: The foreign_amount of this DccInfo.  # noqa: E501
        :rtype: str
        """
        return self._foreign_amount

    @foreign_amount.setter
    def foreign_amount(self, foreign_amount):
        """Sets the foreign_amount of this DccInfo.


        :param foreign_amount: The foreign_amount of this DccInfo.  # noqa: E501
        :type: str
        """

        self._foreign_amount = foreign_amount

    @property
    def foreign_currency(self):
        """Gets the foreign_currency of this DccInfo.  # noqa: E501


        :return: The foreign_currency of this DccInfo.  # noqa: E501
        :rtype: str
        """
        return self._foreign_currency

    @foreign_currency.setter
    def foreign_currency(self, foreign_currency):
        """Sets the foreign_currency of this DccInfo.


        :param foreign_currency: The foreign_currency of this DccInfo.  # noqa: E501
        :type: str
        """

        self._foreign_currency = foreign_currency

    @property
    def host_data(self):
        """Gets the host_data of this DccInfo.  # noqa: E501


        :return: The host_data of this DccInfo.  # noqa: E501
        :rtype: str
        """
        return self._host_data

    @host_data.setter
    def host_data(self, host_data):
        """Sets the host_data of this DccInfo.


        :param host_data: The host_data of this DccInfo.  # noqa: E501
        :type: str
        """

        self._host_data = host_data

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
        if issubclass(DccInfo, dict):
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
        if not isinstance(other, DccInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DccInfo):
            return True

        return self.to_dict() != other.to_dict()
