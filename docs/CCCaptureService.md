# CCCaptureService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchasing_level** | **str** |  | [optional] 
**is_split_transaction** | **str** |  | [optional] 
**use_merchant_creds** | **str** |  | [optional] 
**business_date** | **str** |  | [optional] 
**partial_payment_id** | **str** |  | [optional] 
**last_payment_flag** | **str** |  | [optional] 
**industry_datatype** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.cc_capture_service import CCCaptureService

# TODO update the JSON string below
json = "{}"
# create an instance of CCCaptureService from a JSON string
cc_capture_service_instance = CCCaptureService.from_json(json)
# print the JSON string representation of the object
print CCCaptureService.to_json()

# convert the object into a dict
cc_capture_service_dict = cc_capture_service_instance.to_dict()
# create an instance of CCCaptureService from a dict
cc_capture_service_form_dict = cc_capture_service.from_dict(cc_capture_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


