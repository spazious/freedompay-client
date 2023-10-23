# CCCreditService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trans_type** | **str** |  | [optional] 
**offline** | **str** |  | [optional] 
**offline_code** | **str** |  | [optional] 
**return_balance** | **str** |  | [optional] 
**business_date** | **str** |  | [optional] 
**bill_payment** | **str** |  | [optional] 
**recurring** | **str** |  | [optional] 
**commerce_indicator** | **str** |  | [optional] 
**partial_payment_id** | **str** |  | [optional] 
**last_payment_flag** | **str** |  | [optional] 
**industry_datatype** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.cc_credit_service import CCCreditService

# TODO update the JSON string below
json = "{}"
# create an instance of CCCreditService from a JSON string
cc_credit_service_instance = CCCreditService.from_json(json)
# print the JSON string representation of the object
print CCCreditService.to_json()

# convert the object into a dict
cc_credit_service_dict = cc_credit_service_instance.to_dict()
# create an instance of CCCreditService from a dict
cc_credit_service_form_dict = cc_credit_service.from_dict(cc_credit_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


