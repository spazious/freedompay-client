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


class ShipTo(object):
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
        'company': 'str',
        'title': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'suffix': 'str',
        'street1': 'str',
        'street2': 'str',
        'street3': 'str',
        'street4': 'str',
        'city': 'str',
        'state': 'str',
        'postal_code': 'str',
        'country': 'str',
        'phone_number': 'str',
        'fax_number': 'str',
        'email': 'str',
        'ssn': 'str',
        'date_of_birth': 'str',
        'shipping_company': 'str',
        'shipping_method': 'str',
        'tracking_number': 'str'
    }

    attribute_map = {
        'company': 'company',
        'title': 'title',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'suffix': 'suffix',
        'street1': 'street1',
        'street2': 'street2',
        'street3': 'street3',
        'street4': 'street4',
        'city': 'city',
        'state': 'state',
        'postal_code': 'postalCode',
        'country': 'country',
        'phone_number': 'phoneNumber',
        'fax_number': 'faxNumber',
        'email': 'email',
        'ssn': 'ssn',
        'date_of_birth': 'dateOfBirth',
        'shipping_company': 'shippingCompany',
        'shipping_method': 'shippingMethod',
        'tracking_number': 'trackingNumber'
    }

    def __init__(self, company=None, title=None, first_name=None, middle_name=None, last_name=None, suffix=None, street1=None, street2=None, street3=None, street4=None, city=None, state=None, postal_code=None, country=None, phone_number=None, fax_number=None, email=None, ssn=None, date_of_birth=None, shipping_company=None, shipping_method=None, tracking_number=None, _configuration=None):  # noqa: E501
        """ShipTo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._company = None
        self._title = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._suffix = None
        self._street1 = None
        self._street2 = None
        self._street3 = None
        self._street4 = None
        self._city = None
        self._state = None
        self._postal_code = None
        self._country = None
        self._phone_number = None
        self._fax_number = None
        self._email = None
        self._ssn = None
        self._date_of_birth = None
        self._shipping_company = None
        self._shipping_method = None
        self._tracking_number = None
        self.discriminator = None

        if company is not None:
            self.company = company
        if title is not None:
            self.title = title
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if suffix is not None:
            self.suffix = suffix
        if street1 is not None:
            self.street1 = street1
        if street2 is not None:
            self.street2 = street2
        if street3 is not None:
            self.street3 = street3
        if street4 is not None:
            self.street4 = street4
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if phone_number is not None:
            self.phone_number = phone_number
        if fax_number is not None:
            self.fax_number = fax_number
        if email is not None:
            self.email = email
        if ssn is not None:
            self.ssn = ssn
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if shipping_company is not None:
            self.shipping_company = shipping_company
        if shipping_method is not None:
            self.shipping_method = shipping_method
        if tracking_number is not None:
            self.tracking_number = tracking_number

    @property
    def company(self):
        """Gets the company of this ShipTo.  # noqa: E501


        :return: The company of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ShipTo.


        :param company: The company of this ShipTo.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def title(self):
        """Gets the title of this ShipTo.  # noqa: E501


        :return: The title of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ShipTo.


        :param title: The title of this ShipTo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def first_name(self):
        """Gets the first_name of this ShipTo.  # noqa: E501


        :return: The first_name of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ShipTo.


        :param first_name: The first_name of this ShipTo.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this ShipTo.  # noqa: E501


        :return: The middle_name of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this ShipTo.


        :param middle_name: The middle_name of this ShipTo.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this ShipTo.  # noqa: E501


        :return: The last_name of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ShipTo.


        :param last_name: The last_name of this ShipTo.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def suffix(self):
        """Gets the suffix of this ShipTo.  # noqa: E501


        :return: The suffix of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this ShipTo.


        :param suffix: The suffix of this ShipTo.  # noqa: E501
        :type: str
        """

        self._suffix = suffix

    @property
    def street1(self):
        """Gets the street1 of this ShipTo.  # noqa: E501


        :return: The street1 of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._street1

    @street1.setter
    def street1(self, street1):
        """Sets the street1 of this ShipTo.


        :param street1: The street1 of this ShipTo.  # noqa: E501
        :type: str
        """

        self._street1 = street1

    @property
    def street2(self):
        """Gets the street2 of this ShipTo.  # noqa: E501


        :return: The street2 of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """Sets the street2 of this ShipTo.


        :param street2: The street2 of this ShipTo.  # noqa: E501
        :type: str
        """

        self._street2 = street2

    @property
    def street3(self):
        """Gets the street3 of this ShipTo.  # noqa: E501


        :return: The street3 of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._street3

    @street3.setter
    def street3(self, street3):
        """Sets the street3 of this ShipTo.


        :param street3: The street3 of this ShipTo.  # noqa: E501
        :type: str
        """

        self._street3 = street3

    @property
    def street4(self):
        """Gets the street4 of this ShipTo.  # noqa: E501


        :return: The street4 of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._street4

    @street4.setter
    def street4(self, street4):
        """Sets the street4 of this ShipTo.


        :param street4: The street4 of this ShipTo.  # noqa: E501
        :type: str
        """

        self._street4 = street4

    @property
    def city(self):
        """Gets the city of this ShipTo.  # noqa: E501


        :return: The city of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ShipTo.


        :param city: The city of this ShipTo.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this ShipTo.  # noqa: E501


        :return: The state of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShipTo.


        :param state: The state of this ShipTo.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def postal_code(self):
        """Gets the postal_code of this ShipTo.  # noqa: E501


        :return: The postal_code of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ShipTo.


        :param postal_code: The postal_code of this ShipTo.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this ShipTo.  # noqa: E501


        :return: The country of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ShipTo.


        :param country: The country of this ShipTo.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone_number(self):
        """Gets the phone_number of this ShipTo.  # noqa: E501


        :return: The phone_number of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ShipTo.


        :param phone_number: The phone_number of this ShipTo.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def fax_number(self):
        """Gets the fax_number of this ShipTo.  # noqa: E501


        :return: The fax_number of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number):
        """Sets the fax_number of this ShipTo.


        :param fax_number: The fax_number of this ShipTo.  # noqa: E501
        :type: str
        """

        self._fax_number = fax_number

    @property
    def email(self):
        """Gets the email of this ShipTo.  # noqa: E501


        :return: The email of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ShipTo.


        :param email: The email of this ShipTo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def ssn(self):
        """Gets the ssn of this ShipTo.  # noqa: E501


        :return: The ssn of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._ssn

    @ssn.setter
    def ssn(self, ssn):
        """Sets the ssn of this ShipTo.


        :param ssn: The ssn of this ShipTo.  # noqa: E501
        :type: str
        """

        self._ssn = ssn

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this ShipTo.  # noqa: E501


        :return: The date_of_birth of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this ShipTo.


        :param date_of_birth: The date_of_birth of this ShipTo.  # noqa: E501
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def shipping_company(self):
        """Gets the shipping_company of this ShipTo.  # noqa: E501


        :return: The shipping_company of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._shipping_company

    @shipping_company.setter
    def shipping_company(self, shipping_company):
        """Sets the shipping_company of this ShipTo.


        :param shipping_company: The shipping_company of this ShipTo.  # noqa: E501
        :type: str
        """

        self._shipping_company = shipping_company

    @property
    def shipping_method(self):
        """Gets the shipping_method of this ShipTo.  # noqa: E501


        :return: The shipping_method of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._shipping_method

    @shipping_method.setter
    def shipping_method(self, shipping_method):
        """Sets the shipping_method of this ShipTo.


        :param shipping_method: The shipping_method of this ShipTo.  # noqa: E501
        :type: str
        """

        self._shipping_method = shipping_method

    @property
    def tracking_number(self):
        """Gets the tracking_number of this ShipTo.  # noqa: E501


        :return: The tracking_number of this ShipTo.  # noqa: E501
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """Sets the tracking_number of this ShipTo.


        :param tracking_number: The tracking_number of this ShipTo.  # noqa: E501
        :type: str
        """

        self._tracking_number = tracking_number

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
        if issubclass(ShipTo, dict):
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
        if not isinstance(other, ShipTo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShipTo):
            return True

        return self.to_dict() != other.to_dict()
