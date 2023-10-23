# GooglePayInitRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address** | [**GoogleBillingAddressRequest**](GoogleBillingAddressRequest.md) |  | [optional] 
**button_color** | **str** |  | [optional] 
**button_type** | **str** |  | [optional] 
**button_size_mode** | **str** |  | [optional] 
**consumer_authentication** | [**ConsumerAuthentication**](ConsumerAuthentication.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**is_email_required** | **bool** |  | [optional] 
**response_type** | **str** |  | [optional] 
**total_price** | **str** |  | [optional] 
**culture_code** | **str** |  | [optional] 
**es_key** | **str** |  | [optional] 
**legal** | [**LegalControl**](LegalControl.md) |  | [optional] 
**store_id** | **str** |  | [optional] 
**styles** | **str** |  | [optional] 
**terminal_id** | **str** |  | [optional] 
**validation_message_type** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.google_pay_init_request import GooglePayInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePayInitRequest from a JSON string
google_pay_init_request_instance = GooglePayInitRequest.from_json(json)
# print the JSON string representation of the object
print GooglePayInitRequest.to_json()

# convert the object into a dict
google_pay_init_request_dict = google_pay_init_request_instance.to_dict()
# create an instance of GooglePayInitRequest from a dict
google_pay_init_request_form_dict = google_pay_init_request.from_dict(google_pay_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


