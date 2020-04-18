## API Documentation  

**Dataset**: National time series, statewise stats and test counts  
**Crowdsourced by**: [COVID19INDIA](https://www.covid19india.org)  
**API Link**: [https://api.covid19india.org/data.json](https://api.covid19india.org/data.json)  

### JSON Hierarchy
```bash
└─  (object)
   ├─ "cases_time_series" (array)
   │  └─  (object)
   │     ├─ "dailyconfirmed" (string)
   │     ├─ "dailydeceased" (string)
   │     ├─ "dailyrecovered" (string)
   │     ├─ "date" (string)
   │     ├─ "totalconfirmed" (string)
   │     ├─ "totaldeceased" (string)
   │     └─ "totalrecovered" (string)
   ├─ "statewise" (array)
   │  └─  (object)
   │     ├─ "active" (string)
   │     ├─ "confirmed" (string)
   │     ├─ "deaths" (string)
   │     ├─ "deltaconfirmed" (string)
   │     ├─ "deltadeaths" (string)
   │     ├─ "deltarecovered" (string)
   │     ├─ "lastupdatedtime" (string)
   │     ├─ "recovered" (string)
   │     ├─ "state" (string)
   │     ├─ "statecode" (string)
   │     └─ "statenotes" (string)
   └─ "tested" (array)
      └─  (object)
         ├─ "positivecasesfromsamplesreported" (string)
         ├─ "samplereportedtoday" (string)
         ├─ "source" (string)
         ├─ "testsconductedbyprivatelabs" (string)
         ├─ "totalindividualstested" (string)
         ├─ "totalpositivecases" (string)
         ├─ "totalsamplestested" (string)
         └─ "updatetimestamp" (string)

```


### JSON Field details
| Field | Data type | Details |
| ----- | --------- | ------- |
| `cases_time_series` |  `array` | - |
| `dailyconfirmed` |  `string` | - |
| `dailydeceased` |  `string` | - |
| `dailyrecovered` |  `string` | - |
| `date` |  `string` | - |
| `totalconfirmed` |  `string` | - |
| `totaldeceased` |  `string` | - |
| `totalrecovered` |  `string` | - |
| `statewise` |  `array` | - |
| `active` |  `string` | - |
| `confirmed` |  `string` | - |
| `deaths` |  `string` | - |
| `deltaconfirmed` |  `string` | - |
| `deltadeaths` |  `string` | - |
| `deltarecovered` |  `string` | - |
| `lastupdatedtime` |  `string` | - |
| `recovered` |  `string` | - |
| `state` |  `string` | - |
| `statecode` |  `string` | - |
| `statenotes` |  `string` | - |
| `tested` |  `array` | - |
| `positivecasesfromsamplesreported` |  `string` | - |
| `samplereportedtoday` |  `string` | - |
| `source` |  `string` | - |
| `testsconductedbyprivatelabs` |  `string` | - |
| `totalindividualstested` |  `string` | - |
| `totalpositivecases` |  `string` | - |
| `totalsamplestested` |  `string` | - |
| `updatetimestamp` |  `string` | - |

