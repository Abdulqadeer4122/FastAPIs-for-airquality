# Air Quality Data RESTful API

This project is a RESTful API built using FastAPI that provides access to global annual PM2.5 air pollution levels. The API allows users to query, filter, and perform basic analytics on air quality data.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete air quality data entries.
- **Filtering**: Filter data based on latitude and longitude.
- **Statistics**: Retrieve basic statistics (count, average, min, max) for PM2.5 levels.
- **Documentation**: Automatic interactive API documentation via FastAPI.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [License](#license)

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Abdulqadeer4122/air-quality-api.git
   cd air-quality-api
```

## Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
##Install dependencies:
```bash 
pip install -r requirements.txt
```
##Run the application:

```bash
uvicorn app.main:app --reload --port 8001
```
##Usage
Once the server is running, you can access the API documentation at:
```bash
http://127.0.0.1:8001/docs
```
###You can use tools like Postman or curl to test the API endpoints.

##API Endpoints
```bash
Method	Endpoint	Description
GET	/data	Retrieve all available data
GET	/data/{id}	Fetch a specific data entry by ID
POST	/data	Add a new data entry
PUT	/data/{id}	Update an existing data entry
DELETE	/data/{id}	Delete a data entry
GET	/data/filter?lat={lat}&long={long}	Filter data based on latitude and longitude
GET	/data/stats	Provide basic statistics on PM2.5 levels
```
##License
This project is licensed under the MIT License - see the LICENSE file for details.
##Contributing
Contributions are welcome! Please create a pull request or open an issue for any enhancements or bug fixes.
##Contact
For any inquiries, feel free to reach out via abdul.qadeer4122@gmail.com.
