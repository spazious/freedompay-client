# coding: utf-8

"""
    Hosted Payment Controls API Documentation v1.5

    The API for Hosted Payment Controls. To access the swagger.json file open the following link: https://hpc.uat.freedompay.com/api/swagger/docs/v1.5  # noqa: E501

    The version of the OpenAPI document: v1.5
    Generated by: https://openapi-generator.tech
"""

from freedompay-client.paths.v1_5_controls_init.post import ControlsInitV15
from freedompay-client.paths.v1_5_controls_init_paypal.post import ControlsInitV150
from freedompay-client.paths.v1_5_controls_init_paybybank.post import ControlsInitV151
from freedompay-client.paths.v1_5_controls_init_apple.post import InitApplePay
from freedompay-client.paths.v1_5_controls_init_google.post import InitGooglePay


class ControlsApi(
    ControlsInitV15,
    ControlsInitV150,
    ControlsInitV151,
    InitApplePay,
    InitGooglePay,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass