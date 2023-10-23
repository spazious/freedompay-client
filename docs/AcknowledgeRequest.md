# AcknowledgeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos_sync_attempt_num** | **int** |  | [optional] 
**pos_sync_id** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.acknowledge_request import AcknowledgeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcknowledgeRequest from a JSON string
acknowledge_request_instance = AcknowledgeRequest.from_json(json)
# print the JSON string representation of the object
print AcknowledgeRequest.to_json()

# convert the object into a dict
acknowledge_request_dict = acknowledge_request_instance.to_dict()
# create an instance of AcknowledgeRequest from a dict
acknowledge_request_form_dict = acknowledge_request.from_dict(acknowledge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


