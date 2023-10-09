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


class IncentiveIncentive(object):
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
        'presented': 'str',
        'accepted': 'str',
        'tender_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'presented': 'presented',
        'accepted': 'accepted',
        'tender_request_id': 'tenderRequestId'
    }

    def __init__(self, id=None, presented=None, accepted=None, tender_request_id=None, _configuration=None):  # noqa: E501
        """IncentiveIncentive - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._presented = None
        self._accepted = None
        self._tender_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if presented is not None:
            self.presented = presented
        if accepted is not None:
            self.accepted = accepted
        if tender_request_id is not None:
            self.tender_request_id = tender_request_id

    @property
    def id(self):
        """Gets the id of this IncentiveIncentive.  # noqa: E501


        :return: The id of this IncentiveIncentive.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncentiveIncentive.


        :param id: The id of this IncentiveIncentive.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def presented(self):
        """Gets the presented of this IncentiveIncentive.  # noqa: E501


        :return: The presented of this IncentiveIncentive.  # noqa: E501
        :rtype: str
        """
        return self._presented

    @presented.setter
    def presented(self, presented):
        """Sets the presented of this IncentiveIncentive.


        :param presented: The presented of this IncentiveIncentive.  # noqa: E501
        :type: str
        """

        self._presented = presented

    @property
    def accepted(self):
        """Gets the accepted of this IncentiveIncentive.  # noqa: E501


        :return: The accepted of this IncentiveIncentive.  # noqa: E501
        :rtype: str
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """Sets the accepted of this IncentiveIncentive.


        :param accepted: The accepted of this IncentiveIncentive.  # noqa: E501
        :type: str
        """

        self._accepted = accepted

    @property
    def tender_request_id(self):
        """Gets the tender_request_id of this IncentiveIncentive.  # noqa: E501


        :return: The tender_request_id of this IncentiveIncentive.  # noqa: E501
        :rtype: str
        """
        return self._tender_request_id

    @tender_request_id.setter
    def tender_request_id(self, tender_request_id):
        """Sets the tender_request_id of this IncentiveIncentive.


        :param tender_request_id: The tender_request_id of this IncentiveIncentive.  # noqa: E501
        :type: str
        """

        self._tender_request_id = tender_request_id

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
        if issubclass(IncentiveIncentive, dict):
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
        if not isinstance(other, IncentiveIncentive):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IncentiveIncentive):
            return True

        return self.to_dict() != other.to_dict()