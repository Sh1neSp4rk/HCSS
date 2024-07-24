### HeavyBid Estimate Insights
#### GET
* GET /api/v2/integration/businessunits/{businessUnitId}/activities
* GET /api/v2/integration/businessunits/{businessUnitId}/activities/{id}
* GET /api/v2/integration/businessunits/{businessUnitId}/activitycodebook
* GET /api/v2/integration/businessunits/{businessUnitId}/activitycodebook/{id}
* GET /api/v2/integration/businessunits/{businessUnitId}/activitycodebookresource
* GET /api/v2/integration/businessunits/{businessUnitId}/activitycodebookresource/{id}
* GET /api/v2/integration/businessunits/{businessUnitId}/estimates/{estimateId}/attachments
* GET /api/v2/integration/businessunits/{businessUnitId}/estimates/{estimateId}/attachments/{attachmentId}
* GET /api/v2/integration/businessunits/{businessUnitId}/biditemcodebook
* GET /api/v2/integration/businessunits/{businessUnitId}/biditemcodebook/{id}
* GET /api/v2/integration/businessunits/{businessUnitId}/biditems
* GET /api/v2/integration/businessunits/{businessUnitId}/biditems/{id}
* GET /api/v2/integration/businessunits
* GET /api/v2/integration/businessunits/{businessUnitId}/estimates
* GET /api/v2/integration/businessunits/{businessUnitId}/estimates/{id}
* GET /api/v2/integration/businessunits/{businessUnitId}/estimates/{id}/kpis
* GET /api/v2/integration/businessunits/{businessUnitId}/materialcodebook
* GET /api/v2/integration/businessunits/{businessUnitId}/materialcodebook/{id}
* GET /api/v2/integration/businessunits/{businessUnitId}/partitions
* GET /api/v2/integration/businessunits/{businessUnitId}/partitions/{id}
* GET /api/v2/integration/businessunits/{businessUnitId}/resources
* GET /api/v2/integration/businessunits/{businessUnitId}/resources/{id}
#### PUT
* PUT /api/v2/integration/businessunits/{businessUnitId}/materialcodebook/{id}

### HeavyBid Pre-Construction
#### GET
* GET /api/v1/businessUnits
* GET /api/v1/businessUnits/{businessUnitId}/Projects
* GET /api/v1/businessUnits/{businessUnitId}/Projects/{id}
* GET /api/v1/businessUnits/{businessUnitId}/Schemas
* GET /api/v1/businessUnits/{businessUnitId}/Schemas/{id}
#### POST
* POST /api/v1/businessUnits/{businessUnitId}/Projects
* POST /api/v1/businessUnits/{businessUnitId}/Projects/range
* POST /api/v1/businessUnits/{businessUnitId}/reports/projects/{projectId}/projectDetails
* POST /api/v1/businessUnits/{businessUnitId}/Schemas/updateFieldAlias
#### PUT
* PUT /api/v1/businessUnits/{businessUnitId}/Projects/{id}
#### PATCH
* PATCH /api/v1/businessUnits/{businessUnitId}/Projects/{id}
#### DELETE
* DELETE /api/v1/businessUnits/{businessUnitId}/Projects/{id}
* DELETE /api/v1/businessUnits/{businessUnitId}/Projects/range

### HeavyJob
#### GET
* GET /api/v1/accessGroup
* GET /api/v1/jobs/{jobId}/advancedBudgets/material
* GET /api/v1/jobs/{jobId}/advancedBudgets/subcontract
* GET /api/v1/jobs/{jobId}/advancedBudgets/custom
* GET /api/v1/businessUnits
* GET /api/v1/businessUnits/{id}/preferences
* GET /api/v1/jobs/{jobId}/costs
* GET /api/v1/jobCosts
* GET /api/v1/costCodes/{costCodeId}/costs
* GET /api/v1/businessUnits/{businessUnitId}/costAdjustments
* GET /api/v1/costCodes
* GET /api/v1/costCodeSetupFilters
* GET /api/v1/costCodeTags
* GET /api/v1/costTypeQuantities/materialInstalled
* GET /api/v1/costTypeQuantities/subcontractWorked
* GET /api/v1/costTypeQuantities/adjustments
* GET /api/v1/businessUnits/{businessUnitId}/costCategories
* GET /api/v1/businessUnits/{businessUnitId}/costTypes/custom
* GET /api/v1/jobs/{jobId}/costTypes/jobCustom
* GET /api/v1/costTypes/jobCustom/{id}
* GET /api/v1/businessUnits/{businessUnitId}/employees
* GET /api/v1/employees
* GET /api/v1/businessUnits/{businessUnitId}/equipment
* GET /api/v1/businessUnits/{businessUnitId}/equipment/types
* GET /api/v1/forecastInfo
* GET /api/v1/forecasts/{forecastId}
* GET /api/v1/businessUnits/{businessUnitId}/attendanceHourTags
* GET /api/v1/businessUnits/{businessUnitId}/nonuseHourTags
* GET /api/v1/jobs
* GET /api/v1/jobEmployees
* GET /api/v1/jobEquipment
* GET /api/v1/businessUnits/{businessUnitId}/costTypes/material
* GET /api/v1/jobs/{jobId}/costTypes/jobMaterial
* GET /api/v1/costTypes/jobMaterial/{id}
* GET /api/v1/businessUnits/{businessUnitId}/payclass
* GET /api/v1/payItems
* GET /api/v2/payItems
* GET /api/v1/jobs/{jobId}/purchaseOrders
* GET /api/v1/purchaseOrders
* GET /api/v1/purchaseOrderItems
* GET /api/v1/purchaseOrders/{purchaseOrderId}/details/material
* GET /api/v1/businessUnits/{businessUnitId}/costTypes/subcontract
* GET /api/v1/jobs/{jobId}/costTypes/jobSubcontract
* GET /api/v1/costTypes/jobSubcontract/{id}
* GET /api/v1/timeCardApprovalInfo
* GET /api/v1/timeCardInfo
* GET /api/v1/timeCards/{id}
* GET /api/v1/businessUnits/{businessUnitId}/missingTimeCards
* GET /api/v1/timeCardEquipment
* GET /api/v1/users/{id}
* GET /api/v1/vendors
* GET /api/v2/vendors
* GET /api/v1/jobs/{jobId}/vendorContracts
* GET /api/v1/vendorContracts
* GET /api/v1/vendorContracts/{vendorContractId}/details
* GET /api/v1/vendorContractItems
#### POST
* POST /api/v1/accountingValues/search
* POST /api/v1/rateSetGroupAccountingValues/search
* POST /api/v1/advancedBudgets/material
* POST /api/v1/advancedBudgets/subcontract
* POST /api/v1/advancedBudgets/custom
* POST /api/v1/attachment
* POST /api/v1/bulkCreateJobsRequest/search
* POST /api/v1/singleCreateJobsRequest/search
* POST /api/v1/jobCosts/advancedRequest
* POST /api/v2/jobCosts/advancedRequest
* POST /api/v1/jobCostsToDate/search
* POST /api/v1/jobCostCustomCosts/advancedRequest
* POST /api/v1/businessUnits/{businessUnitId}/costAdjustments
* POST /api/v1/costCodes
* POST /api/v2/costCodes/advancedRequest
* POST /api/v1/costCodes/search
* POST /api/v1/costCode/progress/advancedRequest
* POST /api/v1/costCodeTags/advancedRequest
* POST /api/v1/costCodeTimeCardTransactions/advancedRequest
* POST /api/v1/costCodeTransactionAdjustments/advancedRequest
* POST /api/v1/businessUnits/{businessUnitId}/costCategories
* POST /api/v1/businessUnits/{businessUnitId}/costTypes/custom
* POST /api/v1/jobs/{jobId}/costTypes/jobCustom
* POST /api/v1/costTypes/customInstalled/advancedRequest
* POST /api/v1/costTypes/customReceived/advancedRequest
* POST /api/v1/diaries/search
* POST /api/v1/employees/advancedRequest
* POST /api/v1/equipment/advancedRequest
* POST /api/v1/businessUnits/{businessUnitId}/equipment/types
* POST /api/v1/hours/employees
* POST /api/v1/hours/equipment
* POST /api/v1/jobs/advanced
* POST /api/v1/businessUnits/{businessUnitId}/costTypes/material
* POST /api/v1/jobs/{jobId}/costTypes/jobMaterial
* POST /api/v1/costTypes/materialInstalled/advancedRequest
* POST /api/v1/costTypes/materialReceived/advancedRequest
* POST /api/v1/payItems
* POST /api/v1/jobs/{jobId}/purchaseOrders
* POST /api/v1/purchaseOrders/{purchaseOrderId}/details/material
* POST /api/v1/quantityAdjustment
* POST /api/v1/businessUnits/{businessUnitId}/costTypes/subcontract
* POST /api/v1/jobs/{jobId}/costTypes/jobSubcontract
* POST /api/v1/costTypes/subcontractWork/advancedRequest
* POST /api/v1/userAccessGroup/search
* POST /api/v1/vendors
* POST /api/v1/jobs/{jobId}/vendorContracts
* POST /api/v1/vendorContracts/{vendorContractId}/details
#### PUT
* PUT /api/v1/businessUnits/{id}/preferences
* PUT /api/v1/costCodes/{costCodeId}/costs
* PUT /api/v1/costAdjustments/{id}
* PUT /api/v1/costTypes/custom/{id}
* PUT /api/v1/costTypes/jobCustom/{id}
* PUT /api/v1/diaries
* PUT /api/v1/businessUnits/{businessUnitId}/equipment/{equipmentId}
* PUT /api/v1/costTypes/material/{id}
* PUT /api/v1/costTypes/jobMaterial/{id}
* PUT /api/v1/purchaseOrders/{id}
* PUT /api/v1/purchaseOrders/details/material/{id}
* PUT /api/v1/costTypes/subcontract/{id}
* PUT /api/v1/costTypes/jobSubcontract/{id}
* PUT /api/v1/timeCards/{id}
* PUT /api/v1/vendors/{id}
* PUT /api/v1/vendorContracts/{id}
* PUT /api/v1/vendorContracts/details/{id}
#### DELETE
* DELETE /api/v1/costAdjustments/{id}
* DELETE /api/v1/costCodeTags
* DELETE /api/v1/costTypes/custom/{id}
* DELETE /api/v1/costTypes/jobCustom/{id}
* DELETE /api/v1/employees
* DELETE /api/v1/jobEmployees
* DELETE /api/v1/jobEquipment
* DELETE /api/v1/costTypes/material/{id}
* DELETE /api/v1/costTypes/jobMaterial/{id}
* DELETE /api/v1/releaseOrders/approvalRules/approvers
* DELETE /api/v1/costTypes/subcontract/{id}
* DELETE /api/v1/costTypes/jobSubcontract/{id}
* DELETE /api/v1/vendors/{id}
#### PATCH
* PATCH /api/v1/costCodes
* PATCH /api/v1/costCodes/customCostTypes
* PATCH /api/v1/costCodeTags
* PATCH /api/v1/costTypeQuantities/customReceived/{id}
* PATCH /api/v1/jobs
* PATCH /api/v1/jobEmployees
* PATCH /api/v1/jobEquipment
* PATCH /api/v1/costTypeItems
* PATCH /api/v1/payClasses/{id}
* PATCH /api/v1/payItems
* PATCH /api/v1/userAccessGroup

### HCSS Safety
#### GET
* GET /v1/incidents/{id}
* GET /v1/incidents
* GET /v2/incidents/{id}
* GET /v1/meetings
#### PUT
* PUT /v1/incidents/{id}

### HCSS Skills
#### GET
* GET /v1/employeeSkills/employee/{employeeCode}
* GET /v1/employeeSkills/skill/{courseCodeOrName}
* GET /v1/employeeSkills
* GET /v1/skills/{courseCodeOrName}
* GET /v1/skills
#### POST
* POST /v1/employeeSkills
* POST /v1/employeeSkills/import
* POST /v1/skills
* POST /v1/skills/import
#### PUT
* PUT /v1/skills/{courseCodeOrName}
#### DELETE
* DELETE /v1/skills/{courseCodeOrName}

### Equipment360
#### GET
* GET /api/v1/businessUnits
* GET /api/v1/costs/fuel
* GET /api/v1/costs/workOrders
* GET /api/v1/costs/workOrdersExtended
* GET /api/v1/customField
* GET /api/v1/customFieldCategories
* GET /api/v1/customFieldList
* GET /api/v1/employees
* GET /api/v1/employees/{id}
* GET /api/v1/equipment
* GET /api/v1/equipment/{id}
* GET /api/v1/equipmentType
* GET /api/v1/invoice
* GET /api/v1/jobs
* GET /api/v1/locations
* GET /api/v1/maintenanceRequest
* GET /api/v1/meterReading
* GET /api/v1/parts
* GET /api/v1/partLocations
* GET /api/v1/partInventory
* GET /api/v1/purchaseOrders
* GET /api/v1/purchaseOrders/{purchaseOrderId}/details
* GET /api/v1/tags
* GET /api/v1/timeCards
* GET /api/v1/unitOfMeasure
* GET /api/v1/vendors
* GET /api/v1/workOrders
* GET /api/v1/workOrders/{id}
* GET /api/v1/workOrderPurchases
* GET /api/v1/workOrderSchedules
#### POST
* POST /api/v1/customField
* POST /api/v1/employees
* POST /api/v1/equipment
* POST /api/v1/equipmentTransfer
* POST /api/v1/equipmentType
* POST /api/v1/invoice
* POST /api/v1/jobs
* POST /api/v1/locations
* POST /api/v1/maintenanceRequest
* POST /api/v1/meterReading
* POST /api/v1/parts
* POST /api/v1/partCostEntry
* POST /api/v1/partCostEntries/{partCostEntryId}/details
* POST /api/v1/partInventory
* POST /api/v1/purchaseOrder
* POST /api/v1/purchaseOrders/{purchaseOrderId}/details
* POST /api/v1/purchaseOrders/{purchaseOrderId}/notes
* POST /api/v1/subletVendorCostEntry
* POST /api/v1/subletVendorCostEntries/{subletVendorCostEntryId}/details
* POST /api/v1/vendors
* POST /api/v1/workOrders
* POST /api/v1/workOrders/{workOrderId}/notes
#### PUT
* PUT /api/v1/employees/{id}
* PUT /api/v1/equipment/{id}
* PUT /api/v1/invoice
* PUT /api/v1/jobs/{id}
* PUT /api/v1/locations/{id}
* PUT /api/v1/parts/{id}
* PUT /api/v1/vendors/{id}
* PUT /api/v1/workOrder/{id}

### HCSS Telematics
#### GET
* GET /api/v1/equipment

### Identity
#### POST
* POST /connect/token
#### GET
* GET /connect/authorize

### Setups
#### GET
* GET /api/v1/AccountingTemplate
* GET /api/v1/BusinessUnit
* GET /api/v1/BusinessUnit/default
* GET /api/v1/CostCode
* GET /api/v1/Employee
* GET /api/v1/Equipment
* GET /api/v1/Job
* GET /api/v1/PayClass
* GET /api/v1/RateSet/Employee
* GET /api/v1/RateSet/PayClass
* GET /api/v1/RateSet/Equipment
* GET /api/v1/RateSet/CostAdjustment
* GET /api/v1/RateSetGroup
* GET /api/v1/Storage/Config
* GET /api/v1/Storage/DataCommand
#### POST
* POST /api/v1/CostCode/bulk
* POST /api/v1/BusinessUnit
* POST /api/v1/CostCode
* POST /api/v1/Employee
* POST /api/v1/Equipment
* POST /api/v1/Job
* POST /api/v1/PayClass
* POST /api/v1/RateSet/Employee
* POST /api/v1/RateSet/PayClass
* POST /api/v1/RateSet/Equipment
* POST /api/v1/RateSet/CostAdjustment
* POST /api/v1/RateSetGroup
#### PATCH
* PATCH /api/v1/CostCode
#### PUT
* PUT /api/v1/CostCode/{id}
* PUT /api/v1/Employee/{id}
* PUT /api/v1/Equipment/{id}
* PUT /api/v1/Job/{id}
* PUT /api/v1/PayClass/{id}
* PUT /api/v1/RateSet/Employee/{id}
* PUT /api/v1/RateSet/PayClass/{id}
* PUT /api/v1/RateSet/Equipment/{id}
* PUT /api/v1/RateSet/CostAdjustment/{id}
* PUT /api/v1/RateSetGroup/{id}
* PUT /api/v1/Storage/Config
* PUT /api/v1/Storage/DataCommand
* PUT /api/v1/Storage/Log/{name}

### Users
#### GET
* GET /api/v1/BusinessUnits
* GET /api/v1/Jobs/GetJobsByBusinessUnit
* GET /api/v1/Roles
* GET /api/v1/SubscriptionGroups
* GET /api/v1/Users
* GET /api/v1/Users/{id}
* GET /api/v1/Users/userName/{userName}
#### POST
* POST /api/v1/Users
#### PATCH
* PATCH /api/v1/Users/{id}
#### DELETE
* DELETE /api/v1/Users/{id}

### Webhooks
#### GET
* GET /api/v1/setups
* GET /api/v1/precon/{businessUnitId}
* GET /api/v1/heavyjob
#### POST
* POST /api/v1/setups
* POST /api/v1/precon/{businessUnitId}
* POST /api/v1/heavyjob
#### PUT
* PUT /api/v1/setups
* PUT /api/v1/precon/{businessUnitId}
* PUT /api/v1/heavyjob
#### DELETE
* DELETE /api/v1/setups
* DELETE /api/v1/precon/{businessUnitId}
* DELETE /api/v1/heavyjob

### Attachments
#### GET
* GET /api/v1/Files/{fileId}
#### POST
* POST /api/v1/Files

### Contacts
#### DELETE
* DELETE /api/v1/products/{contactId}/products
* DELETE /api/v1/contacts/{contactId}
* DELETE /api/v1/offices/{officeId}
* DELETE /api/v1/producttypes/{productTypeId}
* DELETE /api/v1/Vendors/{vendorId}
* DELETE /api/v1/Vendors/{vendorId}/products/{productId}
#### GET
* GET /api/v1/products/{contactId}/products
* GET /api/v1/contacts/{contactId}
* GET /api/v1/offices/{officeId}
* GET /api/v1/producttypes/{productTypeId}
* GET /api/v1/Vendors/{vendorId}
* GET /api/v1/contacts
* GET /api/v1/offices
* GET /api/v1/products
* GET /api/v1/products/{productTypeId}/contacts
* GET /api/v1/products/{productTypeId}/vendors
* GET /api/v1/Vendors
* GET /api/v1/Vendors/{vendorId}/products
#### POST
* POST /api/v1/products/{contactId}/products
* POST /api/v1/contacts
* POST /api/v1/offices
* POST /api/v1/Vendors
* POST /api/v1/Vendors/{vendorId}/products
* POST /api/v1/producttypes
#### PUT
* PUT /api/v1/contacts/{contactId}
* PUT /api/v1/offices/{officeId}
* PUT /api/v1/producttypes/{productTypeId}
* PUT /api/v1/Vendors/{vendorId}

