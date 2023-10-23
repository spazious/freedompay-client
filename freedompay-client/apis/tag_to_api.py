import typing_extensions

from freedompay-client.apis.tags import TagValues
from freedompay-client.apis.tags.controls_api import ControlsApi
from freedompay-client.apis.tags.payments_api import PaymentsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues._CONTROLS: ControlsApi,
        TagValues._PAYMENTS: PaymentsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues._CONTROLS: ControlsApi,
        TagValues._PAYMENTS: PaymentsApi,
    }
)
