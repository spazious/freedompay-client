# NetworkData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**stan** | **str** |  | [optional] 
**aci** | **str** |  | [optional] 
**tdcc** | **str** |  | [optional] 
**pcode** | **str** |  | [optional] 
**vcode** | **str** |  | [optional] 
**downgrade_code** | **str** |  | [optional] 
**cvc_error** | **str** |  | [optional] 
**data_error** | **str** |  | [optional] 
**auth_source** | **str** |  | [optional] 
**response_code** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**program_id** | **str** |  | [optional] 
**merchant_advice** | **str** |  | [optional] 
**service_option** | **str** |  | [optional] 
**fleet_prompts** | **str** |  | [optional] 
**custom_data** | [**List[NetworkCustomData]**](NetworkCustomData.md) |  | [optional] 
**mac** | **str** |  | [optional] 
**pos_seq_num** | **str** |  | [optional] 
**mac_key** | **str** |  | [optional] 
**pin_key** | **str** |  | [optional] 
**field_key** | **str** |  | [optional] 
**trans_date** | **str** |  | [optional] 
**trans_time** | **str** |  | [optional] 
**host_control_data** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.network_data import NetworkData

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkData from a JSON string
network_data_instance = NetworkData.from_json(json)
# print the JSON string representation of the object
print NetworkData.to_json()

# convert the object into a dict
network_data_dict = network_data_instance.to_dict()
# create an instance of NetworkData from a dict
network_data_form_dict = network_data.from_dict(network_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


