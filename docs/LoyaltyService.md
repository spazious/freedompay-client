# LoyaltyService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** |  | [optional] 
**card_number** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**id_block** | **str** |  | [optional] 
**id_ksn** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.loyalty_service import LoyaltyService

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyService from a JSON string
loyalty_service_instance = LoyaltyService.from_json(json)
# print the JSON string representation of the object
print LoyaltyService.to_json()

# convert the object into a dict
loyalty_service_dict = loyalty_service_instance.to_dict()
# create an instance of LoyaltyService from a dict
loyalty_service_form_dict = loyalty_service.from_dict(loyalty_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


