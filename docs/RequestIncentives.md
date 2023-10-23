# RequestIncentives


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **str** |  | [optional] 
**incentives** | [**List[IncentiveIncentive]**](IncentiveIncentive.md) |  | [optional] 

## Example

```python
from freedompay_client.models.request_incentives import RequestIncentives

# TODO update the JSON string below
json = "{}"
# create an instance of RequestIncentives from a JSON string
request_incentives_instance = RequestIncentives.from_json(json)
# print the JSON string representation of the object
print RequestIncentives.to_json()

# convert the object into a dict
request_incentives_dict = request_incentives_instance.to_dict()
# create an instance of RequestIncentives from a dict
request_incentives_form_dict = request_incentives.from_dict(request_incentives_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


