# InquiryService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verify_mode** | **str** |  | [optional] 
**fields** | **str** |  | [optional] 
**authorized_user** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.inquiry_service import InquiryService

# TODO update the JSON string below
json = "{}"
# create an instance of InquiryService from a JSON string
inquiry_service_instance = InquiryService.from_json(json)
# print the JSON string representation of the object
print InquiryService.to_json()

# convert the object into a dict
inquiry_service_dict = inquiry_service_instance.to_dict()
# create an instance of InquiryService from a dict
inquiry_service_form_dict = inquiry_service.from_dict(inquiry_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


