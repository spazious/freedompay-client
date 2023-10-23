# FleetData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**vehicle_id** | **str** |  | [optional] 
**vehicle_tag** | **str** |  | [optional] 
**driver_id** | **str** |  | [optional] 
**odo** | **str** |  | [optional] 
**dl_num** | **str** |  | [optional] 
**dl_state** | **str** |  | [optional] 
**dl_name** | **str** |  | [optional] 
**po_number** | **str** |  | [optional] 
**invoice_num** | **str** |  | [optional] 
**trip_num** | **str** |  | [optional] 
**unit_num** | **str** |  | [optional] 
**trailer_hours** | **str** |  | [optional] 
**dob** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**misc1** | **str** |  | [optional] 
**misc2** | **str** |  | [optional] 
**cash_back** | **str** |  | [optional] 
**job_num** | **str** |  | [optional] 
**maint_id** | **str** |  | [optional] 
**dept** | **str** |  | [optional] 
**vin** | **str** |  | [optional] 
**tractor_num** | **str** |  | [optional] 
**hubo** | **str** |  | [optional] 
**trailer_num** | **str** |  | [optional] 
**custom1** | **str** |  | [optional] 
**custom2** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.fleet_data import FleetData

# TODO update the JSON string below
json = "{}"
# create an instance of FleetData from a JSON string
fleet_data_instance = FleetData.from_json(json)
# print the JSON string representation of the object
print FleetData.to_json()

# convert the object into a dict
fleet_data_dict = fleet_data_instance.to_dict()
# create an instance of FleetData from a dict
fleet_data_form_dict = fleet_data.from_dict(fleet_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


