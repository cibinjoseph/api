#!/usr/bin/python3
""" A python code to generate documentation for the JSON API links """
""" Usage: Add the link to the variable called api """
""" Author: Cibin joseph https://github.com/cibinjoseph"""

import requests
import json
import json2tree as j2t

# Dict in the format <filename>: <url>
api = {'data.md': 'https://api.covid19india.org/data.json', \
       'state_district_wise.md': 'https://api.covid19india.org/state_district_wise.json', \
       'v2_state_district_wise.md': 'https://api.covid19india.org/v2/state_district_wise.json', \
       'raw_data1.md': 'https://api.covid19india.org/raw_data1.json', \
       'raw_data2.md': 'https://api.covid19india.org/raw_data2.json', \
       'raw_data3.md': 'https://api.covid19india.org/raw_data3.json', \
       'states_daily.md': 'https://api.covid19india.org/states_daily.json', \
       'deaths_recoveries.md': 'https://api.covid19india.org/deaths_recoveries.json', \
       'resources.md': 'https://api.covid19india.org/resources/resources.json', \
       'raw_data.md': 'https://api.covid19india.org/raw_data.json', \
       'state_test_data.md': 'https://api.covid19india.org/state_test_data.json'}

header = '## API Documentation  \n\n' + \
        '**Dataset**:  \n' + \
        '**Crowdsourced by**: [COVID19INDIA](https://www.covid19india.org)  '

for item in api:
    filename = item
    link = api[item]
    try:
        jsonData = requests.get(link).json()
        print('Stats retrieval: SUCCESS')
        tree = j2t.json2tree(jsonData)
        table = j2t.json2table(jsonData)

        # Pretty print to file with .md extension
        with open(filename, 'w') as mdfile:
            print(header, file=mdfile)
            print('**API Link**: [' + link + '](' + link + ')  \n', file=mdfile)
            print('### JSON Hierarchy', file=mdfile)
            print('```bash', file=mdfile)
            print(tree, file=mdfile)
            print('```', file=mdfile)
            print('\n', file=mdfile)
            print('### JSON Field details', file=mdfile)
            print(table, file=mdfile)

        # Print status
        print('Generated template for file: ' + filename)

    except:
        print('Stats retrieval: FAILED')
        print('No internet connection or invalid link')
        raise ConnectionError
