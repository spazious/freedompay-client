# TokenInformation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**expiration_month** | **str** |  | [optional] 
**expiration_year** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.token_information import TokenInformation

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInformation from a JSON string
token_information_instance = TokenInformation.from_json(json)
# print the JSON string representation of the object
print TokenInformation.to_json()

# convert the object into a dict
token_information_dict = token_information_instance.to_dict()
# create an instance of TokenInformation from a dict
token_information_form_dict = token_information.from_dict(token_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


