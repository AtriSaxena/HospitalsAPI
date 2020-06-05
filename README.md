# HospitalsAPI

[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)


Django REST API for getting list of Hospitals.


This is hosted on heroku server.

## Data
The data is taken from the [Indian Government website](https://data.gov.in).

Fields of this data are: 
- id
- State
- City
- Name
- category
- Medicine
- Address
- website
- specialization

## Usage

This API is created to find the hospital based on state, city and category of hospital and can also find hospital based on id. 

1. Hospital with city name

```GET https://indian-hospital.herokuapp.com/api/v1/hospitals/?city=Lucknow```

```
[
    {
        "id": 995,
        "state": "Uttar Pradesh",
        "city": "Lucknow",
        "name": "Eye-Q Super Speciality Eye Hospitals, Aliganj",
        "category": "Private",
        "medicine": "Allopathic",
        "address": "B-60, Sector-B, Aliganj, Lucknow, Uttar Pradesh, Phone- (0522) 4024306, 4101710, 2330739",
        "website": "226020",
        "specilization": "NA"
    },
]

```

2. Hospitals with city and category(Private/Public)

```GET https://indian-hospital.herokuapp.com/api/v1/hospitals/?city=Delhi&category=Private```

```

[
    {
        "id": 216,
        "state": "Delhi",
        "city": "Delhi",
        "name": "Kiran Eye Centre",
        "category": "Private",
        "medicine": "Allopathic",
        "address": "C-211, Jhilmil Colony, Delhi, Phone-(011) 64603093, 09871063297",
        "website": "110095",
        "specilization": "NA"
    },
]
```
3. Hospitals with city, category and state

```GET https://indian-hospital.herokuapp.com/api/v1/hospitals/?city=Delhi&category=Private&state=Delhi```

```
[
    {
        "id": 216,
        "state": "Delhi",
        "city": "Delhi",
        "name": "Kiran Eye Centre",
        "category": "Private",
        "medicine": "Allopathic",
        "address": "C-211, Jhilmil Colony, Delhi, Phone-(011) 64603093, 09871063297",
        "website": "110095",
        "specilization": "NA"
    },
]
```

4. Hospital by id

```GET https://indian-hospital.herokuapp.com/api/v1/hospitals/1/```

```
{
    "id": 1,
    "state": "Andaman and Nicobar Islands",
    "city": "Port Blair",
    "name": "G B Pant Hospital, Port Blair",
    "category": "Public",
    "medicine": "Allopathic",
    "address": "GB Pant Road, City Centre, Port Blair, Andaman and Nicobar Islands, Phone- (03192) 233665, 246058, 233455, 230858",
    "website": "744103",
    "specilization": "NA"
}
```

