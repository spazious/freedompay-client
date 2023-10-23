# PayPalInitRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**disable_funding** | **str** |  | [optional] 
**intent** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**payment_method_payee_preferred** | **str** |  | [optional] 
**shipping_preference** | **str** |  | [optional] 
**total_price** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**debug** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
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
from freedompay_client.models.pay_pal_init_request import PayPalInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayPalInitRequest from a JSON string
pay_pal_init_request_instance = PayPalInitRequest.from_json(json)
# print the JSON string representation of the object
print PayPalInitRequest.to_json()

# convert the object into a dict
pay_pal_init_request_dict = pay_pal_init_request_instance.to_dict()
# create an instance of PayPalInitRequest from a dict
pay_pal_init_request_form_dict = pay_pal_init_request.from_dict(pay_pal_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


