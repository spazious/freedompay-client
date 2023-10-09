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


class MobileService(object):
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
        'feature_flags1': 'str',
        'feature_flags2': 'str',
        'function_code': 'str',
        'check_id': 'str',
        'accept_tip': 'str',
        'open_tab': 'str',
        'payment_session_id': 'str',
        'mha_callback_key': 'str',
        'qrseq': 'str',
        'bar_data': 'str',
        'bar_type': 'str',
        'confirm_pay_seq': 'str',
        'pay_seq': 'str',
        'applied_discount_amount': 'str',
        'run': 'str'
    }

    attribute_map = {
        'feature_flags1': 'featureFlags1',
        'feature_flags2': 'featureFlags2',
        'function_code': 'functionCode',
        'check_id': 'checkId',
        'accept_tip': 'acceptTip',
        'open_tab': 'openTab',
        'payment_session_id': 'paymentSessionId',
        'mha_callback_key': 'mhaCallbackKey',
        'qrseq': 'qrseq',
        'bar_data': 'barData',
        'bar_type': 'barType',
        'confirm_pay_seq': 'confirmPaySeq',
        'pay_seq': 'paySeq',
        'applied_discount_amount': 'appliedDiscountAmount',
        'run': 'run'
    }

    def __init__(self, feature_flags1=None, feature_flags2=None, function_code=None, check_id=None, accept_tip=None, open_tab=None, payment_session_id=None, mha_callback_key=None, qrseq=None, bar_data=None, bar_type=None, confirm_pay_seq=None, pay_seq=None, applied_discount_amount=None, run=None, _configuration=None):  # noqa: E501
        """MobileService - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._feature_flags1 = None
        self._feature_flags2 = None
        self._function_code = None
        self._check_id = None
        self._accept_tip = None
        self._open_tab = None
        self._payment_session_id = None
        self._mha_callback_key = None
        self._qrseq = None
        self._bar_data = None
        self._bar_type = None
        self._confirm_pay_seq = None
        self._pay_seq = None
        self._applied_discount_amount = None
        self._run = None
        self.discriminator = None

        if feature_flags1 is not None:
            self.feature_flags1 = feature_flags1
        if feature_flags2 is not None:
            self.feature_flags2 = feature_flags2
        if function_code is not None:
            self.function_code = function_code
        if check_id is not None:
            self.check_id = check_id
        if accept_tip is not None:
            self.accept_tip = accept_tip
        if open_tab is not None:
            self.open_tab = open_tab
        if payment_session_id is not None:
            self.payment_session_id = payment_session_id
        if mha_callback_key is not None:
            self.mha_callback_key = mha_callback_key
        if qrseq is not None:
            self.qrseq = qrseq
        if bar_data is not None:
            self.bar_data = bar_data
        if bar_type is not None:
            self.bar_type = bar_type
        if confirm_pay_seq is not None:
            self.confirm_pay_seq = confirm_pay_seq
        if pay_seq is not None:
            self.pay_seq = pay_seq
        if applied_discount_amount is not None:
            self.applied_discount_amount = applied_discount_amount
        if run is not None:
            self.run = run

    @property
    def feature_flags1(self):
        """Gets the feature_flags1 of this MobileService.  # noqa: E501


        :return: The feature_flags1 of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._feature_flags1

    @feature_flags1.setter
    def feature_flags1(self, feature_flags1):
        """Sets the feature_flags1 of this MobileService.


        :param feature_flags1: The feature_flags1 of this MobileService.  # noqa: E501
        :type: str
        """

        self._feature_flags1 = feature_flags1

    @property
    def feature_flags2(self):
        """Gets the feature_flags2 of this MobileService.  # noqa: E501


        :return: The feature_flags2 of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._feature_flags2

    @feature_flags2.setter
    def feature_flags2(self, feature_flags2):
        """Sets the feature_flags2 of this MobileService.


        :param feature_flags2: The feature_flags2 of this MobileService.  # noqa: E501
        :type: str
        """

        self._feature_flags2 = feature_flags2

    @property
    def function_code(self):
        """Gets the function_code of this MobileService.  # noqa: E501


        :return: The function_code of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._function_code

    @function_code.setter
    def function_code(self, function_code):
        """Sets the function_code of this MobileService.


        :param function_code: The function_code of this MobileService.  # noqa: E501
        :type: str
        """

        self._function_code = function_code

    @property
    def check_id(self):
        """Gets the check_id of this MobileService.  # noqa: E501


        :return: The check_id of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._check_id

    @check_id.setter
    def check_id(self, check_id):
        """Sets the check_id of this MobileService.


        :param check_id: The check_id of this MobileService.  # noqa: E501
        :type: str
        """

        self._check_id = check_id

    @property
    def accept_tip(self):
        """Gets the accept_tip of this MobileService.  # noqa: E501


        :return: The accept_tip of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._accept_tip

    @accept_tip.setter
    def accept_tip(self, accept_tip):
        """Sets the accept_tip of this MobileService.


        :param accept_tip: The accept_tip of this MobileService.  # noqa: E501
        :type: str
        """

        self._accept_tip = accept_tip

    @property
    def open_tab(self):
        """Gets the open_tab of this MobileService.  # noqa: E501


        :return: The open_tab of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._open_tab

    @open_tab.setter
    def open_tab(self, open_tab):
        """Sets the open_tab of this MobileService.


        :param open_tab: The open_tab of this MobileService.  # noqa: E501
        :type: str
        """

        self._open_tab = open_tab

    @property
    def payment_session_id(self):
        """Gets the payment_session_id of this MobileService.  # noqa: E501


        :return: The payment_session_id of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._payment_session_id

    @payment_session_id.setter
    def payment_session_id(self, payment_session_id):
        """Sets the payment_session_id of this MobileService.


        :param payment_session_id: The payment_session_id of this MobileService.  # noqa: E501
        :type: str
        """

        self._payment_session_id = payment_session_id

    @property
    def mha_callback_key(self):
        """Gets the mha_callback_key of this MobileService.  # noqa: E501


        :return: The mha_callback_key of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._mha_callback_key

    @mha_callback_key.setter
    def mha_callback_key(self, mha_callback_key):
        """Sets the mha_callback_key of this MobileService.


        :param mha_callback_key: The mha_callback_key of this MobileService.  # noqa: E501
        :type: str
        """

        self._mha_callback_key = mha_callback_key

    @property
    def qrseq(self):
        """Gets the qrseq of this MobileService.  # noqa: E501


        :return: The qrseq of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._qrseq

    @qrseq.setter
    def qrseq(self, qrseq):
        """Sets the qrseq of this MobileService.


        :param qrseq: The qrseq of this MobileService.  # noqa: E501
        :type: str
        """

        self._qrseq = qrseq

    @property
    def bar_data(self):
        """Gets the bar_data of this MobileService.  # noqa: E501


        :return: The bar_data of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._bar_data

    @bar_data.setter
    def bar_data(self, bar_data):
        """Sets the bar_data of this MobileService.


        :param bar_data: The bar_data of this MobileService.  # noqa: E501
        :type: str
        """

        self._bar_data = bar_data

    @property
    def bar_type(self):
        """Gets the bar_type of this MobileService.  # noqa: E501


        :return: The bar_type of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._bar_type

    @bar_type.setter
    def bar_type(self, bar_type):
        """Sets the bar_type of this MobileService.


        :param bar_type: The bar_type of this MobileService.  # noqa: E501
        :type: str
        """

        self._bar_type = bar_type

    @property
    def confirm_pay_seq(self):
        """Gets the confirm_pay_seq of this MobileService.  # noqa: E501


        :return: The confirm_pay_seq of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._confirm_pay_seq

    @confirm_pay_seq.setter
    def confirm_pay_seq(self, confirm_pay_seq):
        """Sets the confirm_pay_seq of this MobileService.


        :param confirm_pay_seq: The confirm_pay_seq of this MobileService.  # noqa: E501
        :type: str
        """

        self._confirm_pay_seq = confirm_pay_seq

    @property
    def pay_seq(self):
        """Gets the pay_seq of this MobileService.  # noqa: E501


        :return: The pay_seq of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._pay_seq

    @pay_seq.setter
    def pay_seq(self, pay_seq):
        """Sets the pay_seq of this MobileService.


        :param pay_seq: The pay_seq of this MobileService.  # noqa: E501
        :type: str
        """

        self._pay_seq = pay_seq

    @property
    def applied_discount_amount(self):
        """Gets the applied_discount_amount of this MobileService.  # noqa: E501


        :return: The applied_discount_amount of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._applied_discount_amount

    @applied_discount_amount.setter
    def applied_discount_amount(self, applied_discount_amount):
        """Sets the applied_discount_amount of this MobileService.


        :param applied_discount_amount: The applied_discount_amount of this MobileService.  # noqa: E501
        :type: str
        """

        self._applied_discount_amount = applied_discount_amount

    @property
    def run(self):
        """Gets the run of this MobileService.  # noqa: E501


        :return: The run of this MobileService.  # noqa: E501
        :rtype: str
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this MobileService.


        :param run: The run of this MobileService.  # noqa: E501
        :type: str
        """

        self._run = run

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
        if issubclass(MobileService, dict):
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
        if not isinstance(other, MobileService):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MobileService):
            return True

        return self.to_dict() != other.to_dict()
