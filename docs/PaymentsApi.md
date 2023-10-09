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
from __future__ import print_function
import time
import freedompay_client
from freedompay_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = freedompay_client.PaymentsApi()
authorization = 'Bearer ' # str | A valid session key from a previously successful call to initialize a session. (default to Bearer )
request = freedompay_client.AcknowledgeRequest() # AcknowledgeRequest | 

try:
    # 
    api_response = api_instance.payments_acknowledge(authorization, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->payments_acknowledge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid session key from a previously successful call to initialize a session. | [default to Bearer ]
 **request** | [**AcknowledgeRequest**](AcknowledgeRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_post_v13**
> object payments_post_v13(authorization, request)



### Example
```python
from __future__ import print_function
import time
import freedompay_client
from freedompay_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = freedompay_client.PaymentsApi()
authorization = 'Bearer ' # str | A valid session key from a previously successful call to initialize a session. (default to Bearer )
request = freedompay_client.PostRequest() # PostRequest | 

try:
    # 
    api_response = api_instance.payments_post_v13(authorization, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->payments_post_v13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid session key from a previously successful call to initialize a session. | [default to Bearer ]
 **request** | [**PostRequest**](PostRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_reverse**
> object payments_reverse(authorization, request)



### Example
```python
from __future__ import print_function
import time
import freedompay_client
from freedompay_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = freedompay_client.PaymentsApi()
authorization = 'Bearer ' # str | A valid session key from a previously successful call to initialize a session. (default to Bearer )
request = freedompay_client.ReversalRequest() # ReversalRequest | 

try:
    # 
    api_response = api_instance.payments_reverse(authorization, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->payments_reverse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid session key from a previously successful call to initialize a session. | [default to Bearer ]
 **request** | [**ReversalRequest**](ReversalRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

