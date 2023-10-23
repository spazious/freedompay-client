# freedompay-client.model.google_pay_init_request.GooglePayInitRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**BillingAddress** | [**GoogleBillingAddressRequest**](GoogleBillingAddressRequest.md) | [**GoogleBillingAddressRequest**](GoogleBillingAddressRequest.md) |  | [optional] 
**ButtonColor** | str,  | str,  |  | [optional] must be one of ["Unknown", "Black", "White", ] 
**ButtonType** | str,  | str,  |  | [optional] must be one of ["Unknown", "Icon", "Buy", "Checkout", "Donate", "Order", "Pay", "Plain", "Subscribe", "Book", ] 
**ButtonSizeMode** | str,  | str,  |  | [optional] must be one of ["Static", "Fill", ] 
**ConsumerAuthentication** | [**ConsumerAuthentication**](ConsumerAuthentication.md) | [**ConsumerAuthentication**](ConsumerAuthentication.md) |  | [optional] 
**CurrencyCode** | str,  | str,  |  | [optional] 
**IsEmailRequired** | bool,  | BoolClass,  |  | [optional] 
**ResponseType** | str,  | str,  |  | [optional] must be one of ["Unknown", "Dictionary", "Raw", ] 
**TotalPrice** | str,  | str,  |  | [optional] 
**CultureCode** | str,  | str,  |  | [optional] 
**EsKey** | str,  | str,  |  | [optional] 
**Legal** | [**LegalControl**](LegalControl.md) | [**LegalControl**](LegalControl.md) |  | [optional] 
**StoreId** | str,  | str,  |  | [optional] 
**Styles** | str,  | str,  |  | [optional] 
**TerminalId** | str,  | str,  |  | [optional] 
**ValidationMessageType** | str,  | str,  |  | [optional] must be one of ["Unknown", "None", "Feedback", "Tooltip", ] 
**ReferenceId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

