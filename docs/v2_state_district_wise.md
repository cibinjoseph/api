## API Documentation  

**Dataset**: State-district-wise V2  
**Crowdsourced by**: [COVID19INDIA](https://www.covid19india.org)  
**API Link**: [https://api.covid19india.org/v2/state_district_wise.json](https://api.covid19india.org/v2/state_district_wise.json)  

### JSON Hierarchy
```bash
└─  (array)
   └─  (object)
      ├─ "state" (string)
      └─ "districtData" (array)
         └─  (object)
            ├─ "district" (string)
            ├─ "confirmed" (number)
            ├─ "lastupdatedtime" (string)
            └─ "delta" (object)
               └─ "confirmed" (number)

```


### JSON Field details
| Field | Data type | Details |
| ----- | --------- | ------- |
| `state` |  `string` | - |
| `districtData` |  `array` | - |
| `district` |  `string` | - |
| `confirmed` |  `number` | - |
| `lastupdatedtime` |  `string` | - |
| `delta` |  `object` | - |
| `confirmed` |  `number` | - |

