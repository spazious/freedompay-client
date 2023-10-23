<a name="__pageTop"></a>
# freedompay-client.apis.tags.controls_api.ControlsApi

All URIs are relative to *https://hpc.uat.freedompay.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controls_init_v15**](#controls_init_v15) | **post** /v1.5/controls/init | Initializes a payment request workflow.
[**controls_init_v15_0**](#controls_init_v15_0) | **post** /v1.5/controls/init/paypal | Initializes a PayPal payment request workflow.
[**controls_init_v15_1**](#controls_init_v15_1) | **post** /v1.5/controls/init/paybybank | Initializes a PayByBank payment request workflow.
[**init_apple_pay**](#init_apple_pay) | **post** /v1.5/controls/init/apple | Initializes an ApplePay payment request workflow.
[**init_google_pay**](#init_google_pay) | **post** /v1.5/controls/init/google | Initializes a Google Pay payment request workflow.

# **controls_init_v15**
<a name="controls_init_v15"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} controls_init_v15(request)

Initializes a payment request workflow.

### Example

```python
import freedompay-client
from freedompay-client.apis.tags import controls_api
from freedompay-client.model.init_request import InitRequest
from pprint import pprint
# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay-client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)

# Enter a context with an instance of the API client
with freedompay-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = controls_api.ControlsApi(api_client)

    # example passing only required values which don't have defaults set
    body = InitRequest(
        button=ButtonControl(
            integrated=True,
        ),
        button_type="Unknown",
        pay_pal=PayPalInitRequest(
            commit=True,
            disabled=True,
            disable_funding="disable_funding_example",
            intent="Unknown",
            invoice_number="invoice_number_example",
            payment_method_payee_preferred="Unknown",
            shipping_preference="Unknown",
            total_price="total_price_example",
            country_code="country_code_example",
            currency_code="currency_code_example",
            debug=True,
            locale="locale_example",
            culture_code="culture_code_example",
            es_key="es_key_example",
            legal=LegalControl(
                hide_checkbox=True,
                text_type="Unknown",
            ),
            store_id="store_id_example",
            styles="styles_example",
            terminal_id="terminal_id_example",
            validation_message_type="Unknown",
            reference_id="00000000-0000-0000-0000-000000000000",
        ),
        postal_code=PostalCodeControl(
            label_type="Unknown",
            placeholder_type="Unknown",
            validation_type="Unknown",
        ),
        pay_by_bank=PayByBankInitRequest(
            order_id="order_id_example",
            transaction_id="transaction_id_example",
            total_price="total_price_example",
            currency_code="currency_code_example",
            merchant_redirect_url="merchant_redirect_url_example",
            culture_code="culture_code_example",
            es_key="es_key_example",
            legal=LegalControl(),
            store_id="store_id_example",
            styles="styles_example",
            terminal_id="terminal_id_example",
            validation_message_type="Unknown",
            reference_id="00000000-0000-0000-0000-000000000000",
        ),
        fraud_check=FraudCheckOptions(
            enabled=True,
            kount=KountOptions(
                device_identifier="device_identifier_example",
            ),
        ),
        card_number=CardNumberControl(
            label_type="Unknown",
            mask_type="Default",
            placeholder_type="Unknown",
        ),
        consumer_authentication=ConsumerAuthentication(
            enabled=True,
            auto_map_to_free_way_request=True,
            fields=dict(
                "key": "key_example",
            ),
        ),
        dcc=DccOptions(
            is_enabled=True,
        ),
        expiration_date=ExpirationDateControl(
            label_type="Unknown",
            placeholder_type="Unknown",
            validation_type="Unknown",
        ),
        order_details=OrderDetails(
            transaction_total=3.14,
            currency_code="currency_code_example",
            order_number="order_number_example",
            order_description="order_description_example",
        ),
        security_code=SecurityCodeControl(
            label_type="Unknown",
            mask_type="Default",
            placeholder_type="Unknown",
            validation_type="Unknown",
        ),
        token_information=TokenInformation(
            token="token_example",
            expiration_month="expiration_month_example",
            expiration_year="expiration_year_example",
        ),
        card_icon_display_type="Unknown",
        payment_type="Unknown",
        workflow_type="Unknown",
        culture_code="culture_code_example",
        es_key="es_key_example",
        legal=LegalControl(),
        store_id="store_id_example",
        styles="styles_example",
        terminal_id="terminal_id_example",
        validation_message_type="Unknown",
        reference_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        # Initializes a payment request workflow.
        api_response = api_instance.controls_init_v15(
            body=body,
        )
        pprint(api_response)
    except freedompay-client.ApiException as e:
        print("Exception when calling ControlsApi->controls_init_v15: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InitRequest**](../../models/InitRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#controls_init_v15.ApiResponseFor200) | OK

#### controls_init_v15.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **controls_init_v15_0**
<a name="controls_init_v15_0"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} controls_init_v15_0(request)

Initializes a PayPal payment request workflow.

### Example

```python
import freedompay-client
from freedompay-client.apis.tags import controls_api
from freedompay-client.model.pay_pal_init_request import PayPalInitRequest
from pprint import pprint
# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay-client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)

# Enter a context with an instance of the API client
with freedompay-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = controls_api.ControlsApi(api_client)

    # example passing only required values which don't have defaults set
    body = PayPalInitRequest(
        commit=True,
        disabled=True,
        disable_funding="disable_funding_example",
        intent="Unknown",
        invoice_number="invoice_number_example",
        payment_method_payee_preferred="Unknown",
        shipping_preference="Unknown",
        total_price="total_price_example",
        country_code="country_code_example",
        currency_code="currency_code_example",
        debug=True,
        locale="locale_example",
        culture_code="culture_code_example",
        es_key="es_key_example",
        legal=LegalControl(
            hide_checkbox=True,
            text_type="Unknown",
        ),
        store_id="store_id_example",
        styles="styles_example",
        terminal_id="terminal_id_example",
        validation_message_type="Unknown",
        reference_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        # Initializes a PayPal payment request workflow.
        api_response = api_instance.controls_init_v15_0(
            body=body,
        )
        pprint(api_response)
    except freedompay-client.ApiException as e:
        print("Exception when calling ControlsApi->controls_init_v15_0: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PayPalInitRequest**](../../models/PayPalInitRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#controls_init_v15_0.ApiResponseFor200) | OK

#### controls_init_v15_0.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **controls_init_v15_1**
<a name="controls_init_v15_1"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} controls_init_v15_1(request)

Initializes a PayByBank payment request workflow.

### Example

```python
import freedompay-client
from freedompay-client.apis.tags import controls_api
from freedompay-client.model.pay_by_bank_init_request import PayByBankInitRequest
from pprint import pprint
# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay-client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)

# Enter a context with an instance of the API client
with freedompay-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = controls_api.ControlsApi(api_client)

    # example passing only required values which don't have defaults set
    body = PayByBankInitRequest(
        order_id="order_id_example",
        transaction_id="transaction_id_example",
        total_price="total_price_example",
        currency_code="currency_code_example",
        merchant_redirect_url="merchant_redirect_url_example",
        culture_code="culture_code_example",
        es_key="es_key_example",
        legal=LegalControl(
            hide_checkbox=True,
            text_type="Unknown",
        ),
        store_id="store_id_example",
        styles="styles_example",
        terminal_id="terminal_id_example",
        validation_message_type="Unknown",
        reference_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        # Initializes a PayByBank payment request workflow.
        api_response = api_instance.controls_init_v15_1(
            body=body,
        )
        pprint(api_response)
    except freedompay-client.ApiException as e:
        print("Exception when calling ControlsApi->controls_init_v15_1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PayByBankInitRequest**](../../models/PayByBankInitRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#controls_init_v15_1.ApiResponseFor200) | OK

#### controls_init_v15_1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **init_apple_pay**
<a name="init_apple_pay"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} init_apple_pay(request)

Initializes an ApplePay payment request workflow.

### Example

```python
import freedompay-client
from freedompay-client.apis.tags import controls_api
from freedompay-client.model.apple_pay_init_request import ApplePayInitRequest
from pprint import pprint
# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay-client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)

# Enter a context with an instance of the API client
with freedompay-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = controls_api.ControlsApi(api_client)

    # example passing only required values which don't have defaults set
    body = ApplePayInitRequest(
        currency_code="currency_code_example",
        button_type="Unknown",
        button_color="Unknown",
        total_price="total_price_example",
        auto_finalize_payment=True,
        exclude_shipping_address=True,
        culture_code="culture_code_example",
        es_key="es_key_example",
        legal=LegalControl(
            hide_checkbox=True,
            text_type="Unknown",
        ),
        store_id="store_id_example",
        styles="styles_example",
        terminal_id="terminal_id_example",
        validation_message_type="Unknown",
        reference_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        # Initializes an ApplePay payment request workflow.
        api_response = api_instance.init_apple_pay(
            body=body,
        )
        pprint(api_response)
    except freedompay-client.ApiException as e:
        print("Exception when calling ControlsApi->init_apple_pay: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplePayInitRequest**](../../models/ApplePayInitRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#init_apple_pay.ApiResponseFor200) | OK

#### init_apple_pay.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **init_google_pay**
<a name="init_google_pay"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} init_google_pay(request)

Initializes a Google Pay payment request workflow.

### Example

```python
import freedompay-client
from freedompay-client.apis.tags import controls_api
from freedompay-client.model.google_pay_init_request import GooglePayInitRequest
from pprint import pprint
# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay-client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)

# Enter a context with an instance of the API client
with freedompay-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = controls_api.ControlsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GooglePayInitRequest(
        billing_address=GoogleBillingAddressRequest(
            format="Unknown",
            is_required=True,
            is_phone_number_required=True,
        ),
        button_color="Unknown",
        button_type="Unknown",
        button_size_mode="Static",
        consumer_authentication=ConsumerAuthentication(
            enabled=True,
            auto_map_to_free_way_request=True,
            fields=dict(
                "key": "key_example",
            ),
        ),
        currency_code="currency_code_example",
        is_email_required=True,
        response_type="Unknown",
        total_price="total_price_example",
        culture_code="culture_code_example",
        es_key="es_key_example",
        legal=LegalControl(
            hide_checkbox=True,
            text_type="Unknown",
        ),
        store_id="store_id_example",
        styles="styles_example",
        terminal_id="terminal_id_example",
        validation_message_type="Unknown",
        reference_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        # Initializes a Google Pay payment request workflow.
        api_response = api_instance.init_google_pay(
            body=body,
        )
        pprint(api_response)
    except freedompay-client.ApiException as e:
        print("Exception when calling ControlsApi->init_google_pay: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GooglePayInitRequest**](../../models/GooglePayInitRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#init_google_pay.ApiResponseFor200) | OK

#### init_google_pay.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextHtml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

