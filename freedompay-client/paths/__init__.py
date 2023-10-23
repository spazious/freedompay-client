# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from freedompay-client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_5_CONTROLS_INIT = "/v1.5/controls/init"
    V1_5_CONTROLS_INIT_APPLE = "/v1.5/controls/init/apple"
    V1_5_CONTROLS_INIT_GOOGLE = "/v1.5/controls/init/google"
    V1_5_CONTROLS_INIT_PAYPAL = "/v1.5/controls/init/paypal"
    V1_5_CONTROLS_INIT_PAYBYBANK = "/v1.5/controls/init/paybybank"
    V1_5_PAYMENTS = "/v1.5/payments"
    V1_5_PAYMENTS_REVERSE = "/v1.5/payments/reverse"
    V1_5_PAYMENTS_ACKNOWLEDGE = "/v1.5/payments/acknowledge"
