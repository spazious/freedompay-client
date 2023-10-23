# freedompay_client.PaymentsApi

All URIs are relative to *https://hpc.uat.freedompay.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_acknowledge**](PaymentsApi.md#payments_acknowledge) | **POST** /v1.5/payments/acknowledge | 
[**payments_post_v13**](PaymentsApi.md#payments_post_v13) | **POST** /v1.5/payments | 
[**payments_reverse**](PaymentsApi.md#payments_reverse) | **POST** /v1.5/payments/reverse | 


# **payments_acknowledge**
> object payments_acknowledge(authorization, request)



### Example

```python
import time
import os
import freedompay_client
from freedompay_client.models.acknowledge_request import AcknowledgeRequest
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
    api_instance = freedompay_client.PaymentsApi(api_client)
    authorization = 'Bearer ' # str | A valid session key from a previously successful call to initialize a session. (default to 'Bearer ')
    request = freedompay_client.AcknowledgeRequest() # AcknowledgeRequest | 

    try:
        api_response = api_instance.payments_acknowledge(authorization, request)
        print("The response of PaymentsApi->payments_acknowledge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_acknowledge: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid session key from a previously successful call to initialize a session. | [default to &#39;Bearer &#39;]
 **request** | [**AcknowledgeRequest**](AcknowledgeRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_post_v13**
> object payments_post_v13(authorization, pos_sync_attempt_num=pos_sync_attempt_num, pos_sync_id=pos_sync_id, cc_auth=cc_auth, payment_key=payment_key, request_message=request_message, token_information=token_information)



### Example

```python
import time
import os
import freedompay_client
from freedompay_client.models.request_message import RequestMessage
from freedompay_client.models.token_information import TokenInformation
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
    api_instance = freedompay_client.PaymentsApi(api_client)
    authorization = 'Bearer ' # str | A valid session key from a previously successful call to initialize a session. (default to 'Bearer ')
    pos_sync_attempt_num = 56 # int |  (optional)
    pos_sync_id = 'pos_sync_id_example' # str |  (optional)
    cc_auth = 'cc_auth_example' # str |  (optional)
    payment_key = 'payment_key_example' # str |  (optional)
    request_message = freedompay_client.RequestMessage() # RequestMessage |  (optional)
    token_information = freedompay_client.TokenInformation() # TokenInformation |  (optional)

    try:
        api_response = api_instance.payments_post_v13(authorization, pos_sync_attempt_num=pos_sync_attempt_num, pos_sync_id=pos_sync_id, cc_auth=cc_auth, payment_key=payment_key, request_message=request_message, token_information=token_information)
        print("The response of PaymentsApi->payments_post_v13:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_post_v13: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid session key from a previously successful call to initialize a session. | [default to &#39;Bearer &#39;]
 **pos_sync_attempt_num** | **int**|  | [optional] 
 **pos_sync_id** | **str**|  | [optional] 
 **cc_auth** | **str**|  | [optional] 
 **payment_key** | **str**|  | [optional] 
 **request_message** | [**RequestMessage**](RequestMessage.md)|  | [optional] 
 **token_information** | [**TokenInformation**](TokenInformation.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_reverse**
> object payments_reverse(authorization, request)



### Example

```python
import time
import os
import freedompay_client
from freedompay_client.models.reversal_request import ReversalRequest
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
    api_instance = freedompay_client.PaymentsApi(api_client)
    authorization = 'Bearer ' # str | A valid session key from a previously successful call to initialize a session. (default to 'Bearer ')
    request = freedompay_client.ReversalRequest() # ReversalRequest | 

    try:
        api_response = api_instance.payments_reverse(authorization, request)
        print("The response of PaymentsApi->payments_reverse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_reverse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid session key from a previously successful call to initialize a session. | [default to &#39;Bearer &#39;]
 **request** | [**ReversalRequest**](ReversalRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

