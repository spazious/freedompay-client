# MobileService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_flags1** | **str** |  | [optional] 
**feature_flags2** | **str** |  | [optional] 
**function_code** | **str** |  | [optional] 
**check_id** | **str** |  | [optional] 
**accept_tip** | **str** |  | [optional] 
**open_tab** | **str** |  | [optional] 
**payment_session_id** | **str** |  | [optional] 
**mha_callback_key** | **str** |  | [optional] 
**qrseq** | **str** |  | [optional] 
**bar_data** | **str** |  | [optional] 
**bar_type** | **str** |  | [optional] 
**confirm_pay_seq** | **str** |  | [optional] 
**pay_seq** | **str** |  | [optional] 
**applied_discount_amount** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.mobile_service import MobileService

# TODO update the JSON string below
json = "{}"
# create an instance of MobileService from a JSON string
mobile_service_instance = MobileService.from_json(json)
# print the JSON string representation of the object
print MobileService.to_json()

# convert the object into a dict
mobile_service_dict = mobile_service_instance.to_dict()
# create an instance of MobileService from a dict
mobile_service_form_dict = mobile_service.from_dict(mobile_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


