# PayByBankInitRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**total_price** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**merchant_redirect_url** | **str** |  | [optional] 
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
from freedompay_client.models.pay_by_bank_init_request import PayByBankInitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayByBankInitRequest from a JSON string
pay_by_bank_init_request_instance = PayByBankInitRequest.from_json(json)
# print the JSON string representation of the object
print PayByBankInitRequest.to_json()

# convert the object into a dict
pay_by_bank_init_request_dict = pay_by_bank_init_request_instance.to_dict()
# create an instance of PayByBankInitRequest from a dict
pay_by_bank_init_request_form_dict = pay_by_bank_init_request.from_dict(pay_by_bank_init_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


