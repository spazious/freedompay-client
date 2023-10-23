# freedompay_client.ControlsApi

All URIs are relative to *https://hpc.uat.freedompay.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controls_init_v15**](ControlsApi.md#controls_init_v15) | **POST** /v1.5/controls/init | Initializes a payment request workflow.
[**controls_init_v15_0**](ControlsApi.md#controls_init_v15_0) | **POST** /v1.5/controls/init/paypal | Initializes a PayPal payment request workflow.
[**controls_init_v15_1**](ControlsApi.md#controls_init_v15_1) | **POST** /v1.5/controls/init/paybybank | Initializes a PayByBank payment request workflow.
[**init_apple_pay**](ControlsApi.md#init_apple_pay) | **POST** /v1.5/controls/init/apple | Initializes an ApplePay payment request workflow.
[**init_google_pay**](ControlsApi.md#init_google_pay) | **POST** /v1.5/controls/init/google | Initializes a Google Pay payment request workflow.


# **controls_init_v15**
> object controls_init_v15(request)

Initializes a payment request workflow.

### Example

```python
import time
import os
import freedompay_client
from freedompay_client.models.init_request import InitRequest
from freedompay_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay_client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)


# Enter a context with an instance of the API client
with freedompay_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freedompay_client.ControlsApi(api_client)
    request = freedompay_client.InitRequest() # InitRequest | Details about the payment request workflow and its controls.

    try:
        # Initializes a payment request workflow.
        api_response = api_instance.controls_init_v15(request)
        print("The response of ControlsApi->controls_init_v15:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ControlsApi->controls_init_v15: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**InitRequest**](InitRequest.md)| Details about the payment request workflow and its controls. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controls_init_v15_0**
> object controls_init_v15_0(request)

Initializes a PayPal payment request workflow.

### Example

```python
import time
import os
import freedompay_client
from freedompay_client.models.pay_pal_init_request import PayPalInitRequest
from freedompay_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay_client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)


# Enter a context with an instance of the API client
with freedompay_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freedompay_client.ControlsApi(api_client)
    request = freedompay_client.PayPalInitRequest() # PayPalInitRequest | Details about the payment request workflow and its controls.

    try:
        # Initializes a PayPal payment request workflow.
        api_response = api_instance.controls_init_v15_0(request)
        print("The response of ControlsApi->controls_init_v15_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ControlsApi->controls_init_v15_0: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PayPalInitRequest**](PayPalInitRequest.md)| Details about the payment request workflow and its controls. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controls_init_v15_1**
> object controls_init_v15_1(request)

Initializes a PayByBank payment request workflow.

### Example

```python
import time
import os
import freedompay_client
from freedompay_client.models.pay_by_bank_init_request import PayByBankInitRequest
from freedompay_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay_client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)


# Enter a context with an instance of the API client
with freedompay_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freedompay_client.ControlsApi(api_client)
    request = freedompay_client.PayByBankInitRequest() # PayByBankInitRequest | Details about the payment request workflow and its controls.

    try:
        # Initializes a PayByBank payment request workflow.
        api_response = api_instance.controls_init_v15_1(request)
        print("The response of ControlsApi->controls_init_v15_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ControlsApi->controls_init_v15_1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PayByBankInitRequest**](PayByBankInitRequest.md)| Details about the payment request workflow and its controls. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_apple_pay**
> object init_apple_pay(request)

Initializes an ApplePay payment request workflow.

### Example

```python
import time
import os
import freedompay_client
from freedompay_client.models.apple_pay_init_request import ApplePayInitRequest
from freedompay_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay_client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)


# Enter a context with an instance of the API client
with freedompay_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freedompay_client.ControlsApi(api_client)
    request = freedompay_client.ApplePayInitRequest() # ApplePayInitRequest | Details about the payment request workflow and its controls.

    try:
        # Initializes an ApplePay payment request workflow.
        api_response = api_instance.init_apple_pay(request)
        print("The response of ControlsApi->init_apple_pay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ControlsApi->init_apple_pay: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApplePayInitRequest**](ApplePayInitRequest.md)| Details about the payment request workflow and its controls. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_google_pay**
> object init_google_pay(request)

Initializes a Google Pay payment request workflow.

### Example

```python
import time
import os
import freedompay_client
from freedompay_client.models.google_pay_init_request import GooglePayInitRequest
from freedompay_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay_client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)


# Enter a context with an instance of the API client
with freedompay_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = freedompay_client.ControlsApi(api_client)
    request = freedompay_client.GooglePayInitRequest() # GooglePayInitRequest | Details about the payment request workflow and its controls.

    try:
        # Initializes a Google Pay payment request workflow.
        api_response = api_instance.init_google_pay(request)
        print("The response of ControlsApi->init_google_pay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ControlsApi->init_google_pay: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GooglePayInitRequest**](GooglePayInitRequest.md)| Details about the payment request workflow and its controls. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

