# Air Quality API

This is a RESTful API for querying and analyzing air quality data (PM2.5 levels).

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd air_quality_api
   
## Install dependencies:
 ```bash
    pip install -r requirements.txt

```

 ```bash
  uvicorn app.main:app --reload
```

 ```bash
docker build -t air_quality_api .
docker run -d -p 8000:8000 air_quality_api
```

##  API Endpoints
```bash
GET /data: Retrieve all available data.
GET /data/{id}: Fetch a specific data entry by ID.
POST /data: Add a new air quality data entry.
PUT /data/{id}: Update an existing data entry.
DELETE /data/{id}: Remove a data entry.
GET /data/filter: Filter data by latitude and/or longitude.
GET /data/stats: Get statistics of PM2.5 levels.


