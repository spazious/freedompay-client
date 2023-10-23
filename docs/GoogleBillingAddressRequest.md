# GoogleBillingAddressRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**is_phone_number_required** | **bool** |  | [optional] 

## Example

```python
from freedompay_client.models.google_billing_address_request import GoogleBillingAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleBillingAddressRequest from a JSON string
google_billing_address_request_instance = GoogleBillingAddressRequest.from_json(json)
# print the JSON string representation of the object
print GoogleBillingAddressRequest.to_json()

# convert the object into a dict
google_billing_address_request_dict = google_billing_address_request_instance.to_dict()
# create an instance of GoogleBillingAddressRequest from a dict
google_billing_address_request_form_dict = google_billing_address_request.from_dict(google_billing_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


