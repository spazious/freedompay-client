# ApplePayInitRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | [optional] 
**button_type** | **str** |  | [optional] 
**button_color** | **str** |  | [optional] 
**total_price** | **str** |  | [optional] 
**auto_finalize_payment** | **bool** |  | [optional] 
**exclude_shipping_address** | **bool** |  | [optional] 
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
from freedompay_client.models.apple_pay_init_request import ApplePayInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplePayInitRequest from a JSON string
apple_pay_init_request_instance = ApplePayInitRequest.from_json(json)
# print the JSON string representation of the object
print ApplePayInitRequest.to_json()

# convert the object into a dict
apple_pay_init_request_dict = apple_pay_init_request_instance.to_dict()
# create an instance of ApplePayInitRequest from a dict
apple_pay_init_request_form_dict = apple_pay_init_request.from_dict(apple_pay_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


