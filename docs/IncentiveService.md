# IncentiveService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **str** |  | [optional] 
**consumer_identifier_type** | **str** |  | [optional] 
**consumer_identifier** | **str** |  | [optional] 
**additional_data** | **str** |  | [optional] 
**additional_data_type** | **str** |  | [optional] 
**incentives** | [**List[IncentiveIncentive]**](IncentiveIncentive.md) |  | [optional] 
**trans_type** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.incentive_service import IncentiveService

# TODO update the JSON string below
json = "{}"
# create an instance of IncentiveService from a JSON string
incentive_service_instance = IncentiveService.from_json(json)
# print the JSON string representation of the object
print IncentiveService.to_json()

# convert the object into a dict
incentive_service_dict = incentive_service_instance.to_dict()
# create an instance of IncentiveService from a dict
incentive_service_form_dict = incentive_service.from_dict(incentive_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


