# ReversalRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos_sync_attempt_num** | **int** |  | [optional] 
**pos_sync_id** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.reversal_request import ReversalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReversalRequest from a JSON string
reversal_request_instance = ReversalRequest.from_json(json)
# print the JSON string representation of the object
print ReversalRequest.to_json()

# convert the object into a dict
reversal_request_dict = reversal_request_instance.to_dict()
# create an instance of ReversalRequest from a dict
reversal_request_form_dict = reversal_request.from_dict(reversal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


