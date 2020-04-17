## API Documentation

**Dataset**: State-district-wise V2  
**Link**: [https://api.covid19india.org/v2/state_district_wise.json](https://api.covid19india.org/v2/state_district_wise.json)  
**Crowdsourced by**: [COVID19INDIA](https://www.covid19india.org)  

### JSON Hierarchy
```bash
└─ (array)
   └─ (object)
      ├─ "state" (string)
      └─ "districtData" (array)
         └─ "(object)"
            ├─ "district" (string)
            ├─ "confirmed" (number)
            ├─ "lastupdatedtime" (string)
            └─ "delta" (object)
               └─ "confirmed" (number)
```


### JSON Field details
| Field | Data type | Notes |
| --- | --- | --- |
| `state` | `string` | - |
| `districtData` | `array` | - |
| `district` | `string` | - |
| `confirmed` | `number` | - |
| `lastupdatedtime` | `string` | - |
| `delta` | `object` | - |
| `confirmed` | `number` | - |
