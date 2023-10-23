# IncentiveIncentive


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**presented** | **str** |  | [optional] 
**accepted** | **str** |  | [optional] 
**tender_request_id** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.incentive_incentive import IncentiveIncentive

# TODO update the JSON string below
json = "{}"
# create an instance of IncentiveIncentive from a JSON string
incentive_incentive_instance = IncentiveIncentive.from_json(json)
# print the JSON string representation of the object
print IncentiveIncentive.to_json()

# convert the object into a dict
incentive_incentive_dict = incentive_incentive_instance.to_dict()
# create an instance of IncentiveIncentive from a dict
incentive_incentive_form_dict = incentive_incentive.from_dict(incentive_incentive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


