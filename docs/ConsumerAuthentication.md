# ConsumerAuthentication


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**auto_map_to_free_way_request** | **bool** |  | [optional] 
**fields** | **Dict[str, str]** |  | [optional] 

## Example

```python
from freedompay_client.models.consumer_authentication import ConsumerAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerAuthentication from a JSON string
consumer_authentication_instance = ConsumerAuthentication.from_json(json)
# print the JSON string representation of the object
print ConsumerAuthentication.to_json()

# convert the object into a dict
consumer_authentication_dict = consumer_authentication_instance.to_dict()
# create an instance of ConsumerAuthentication from a dict
consumer_authentication_form_dict = consumer_authentication.from_dict(consumer_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


