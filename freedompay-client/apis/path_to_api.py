import typing_extensions

from freedompay-client.paths import PathValues
from freedompay-client.apis.paths.v1_5_controls_init import V15ControlsInit
from freedompay-client.apis.paths.v1_5_controls_init_apple import V15ControlsInitApple
from freedompay-client.apis.paths.v1_5_controls_init_google import V15ControlsInitGoogle
from freedompay-client.apis.paths.v1_5_controls_init_paypal import V15ControlsInitPaypal
from freedompay-client.apis.paths.v1_5_controls_init_paybybank import V15ControlsInitPaybybank
from freedompay-client.apis.paths.v1_5_payments import V15Payments
from freedompay-client.apis.paths.v1_5_payments_reverse import V15PaymentsReverse
from freedompay-client.apis.paths.v1_5_payments_acknowledge import V15PaymentsAcknowledge

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_5_CONTROLS_INIT: V15ControlsInit,
        PathValues.V1_5_CONTROLS_INIT_APPLE: V15ControlsInitApple,
        PathValues.V1_5_CONTROLS_INIT_GOOGLE: V15ControlsInitGoogle,
        PathValues.V1_5_CONTROLS_INIT_PAYPAL: V15ControlsInitPaypal,
        PathValues.V1_5_CONTROLS_INIT_PAYBYBANK: V15ControlsInitPaybybank,
        PathValues.V1_5_PAYMENTS: V15Payments,
        PathValues.V1_5_PAYMENTS_REVERSE: V15PaymentsReverse,
        PathValues.V1_5_PAYMENTS_ACKNOWLEDGE: V15PaymentsAcknowledge,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_5_CONTROLS_INIT: V15ControlsInit,
        PathValues.V1_5_CONTROLS_INIT_APPLE: V15ControlsInitApple,
        PathValues.V1_5_CONTROLS_INIT_GOOGLE: V15ControlsInitGoogle,
        PathValues.V1_5_CONTROLS_INIT_PAYPAL: V15ControlsInitPaypal,
        PathValues.V1_5_CONTROLS_INIT_PAYBYBANK: V15ControlsInitPaybybank,
        PathValues.V1_5_PAYMENTS: V15Payments,
        PathValues.V1_5_PAYMENTS_REVERSE: V15PaymentsReverse,
        PathValues.V1_5_PAYMENTS_ACKNOWLEDGE: V15PaymentsAcknowledge,
    }
)
