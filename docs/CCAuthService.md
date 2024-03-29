# CCAuthService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trans_type** | **str** |  | [optional] 
**cof_indicator** | **str** |  | [optional] 
**cof_compliance_data** | **str** |  | [optional] 
**allow_partial** | **str** |  | [optional] 
**return_balance** | **str** |  | [optional] 
**auth_type** | **str** |  | [optional] 
**verbal_auth_code** | **str** |  | [optional] 
**ecom3ds** | **str** |  | [optional] 
**cavv** | **str** |  | [optional] 
**xid** | **str** |  | [optional] 
**orig_auth_amount** | **str** |  | [optional] 
**enable_avs** | **str** |  | [optional] 
**offline** | **str** |  | [optional] 
**offline_code** | **str** |  | [optional] 
**estimated** | **str** |  | [optional] 
**installment_number** | **str** |  | [optional] 
**installment_count** | **str** |  | [optional] 
**auth3dsformat** | **str** |  | [optional] 
**auth3dsjson** | **str** |  | [optional] 
**sca_exemptions** | **str** |  | [optional] 
**sca_upgrade** | **str** |  | [optional] 
**request_par** | **str** |  | [optional] 
**bill_payment** | **str** |  | [optional] 
**recurring** | **str** |  | [optional] 
**commerce_indicator** | **str** |  | [optional] 
**partial_payment_id** | **str** |  | [optional] 
**last_payment_flag** | **str** |  | [optional] 
**industry_datatype** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.cc_auth_service import CCAuthService

# TODO update the JSON string below
json = "{}"
# create an instance of CCAuthService from a JSON string
cc_auth_service_instance = CCAuthService.from_json(json)
# print the JSON string representation of the object
print CCAuthService.to_json()

# convert the object into a dict
cc_auth_service_dict = cc_auth_service_instance.to_dict()
# create an instance of CCAuthService from a dict
cc_auth_service_form_dict = cc_auth_service.from_dict(cc_auth_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


