# InvoiceHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** |  | [optional] 
**invoice_date** | **str** |  | [optional] 
**merchant_descriptor** | **str** |  | [optional] 
**merchant_descriptor_contact** | **str** |  | [optional] 
**merchant_descriptor_url** | **str** |  | [optional] 
**purchaser_code** | **str** |  | [optional] 
**purchaser_order_date** | **str** |  | [optional] 
**goods_indicator** | **str** |  | [optional] 
**customer_po** | **str** |  | [optional] 
**product_code_standard** | **str** |  | [optional] 
**eid_indicator** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.invoice_header import InvoiceHeader

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceHeader from a JSON string
invoice_header_instance = InvoiceHeader.from_json(json)
# print the JSON string representation of the object
print InvoiceHeader.to_json()

# convert the object into a dict
invoice_header_dict = invoice_header_instance.to_dict()
# create an instance of InvoiceHeader from a dict
invoice_header_form_dict = invoice_header.from_dict(invoice_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


