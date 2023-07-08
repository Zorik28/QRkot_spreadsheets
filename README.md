# QRkot_spreadsheets

### Description
The application for the Charitable Foundation for Supporting Kittens.
The QRKot Foundation can have multiple projects. Each project has a name, 
description and amount to be raised. After the required amount is collected, 
the project is closed.

Donations to projects are received according to the First In, First Out principle:
all donations go to the project opened earlier than others; when this project collects
the required amount and closes, donations begin to flow into the next project.

### Technologies
- Python           3.9.6
- Flask            2.0.2
- Flask-SQLAlchemy 2.5.1
- Flask-WTF        1.0.0


### Project run on local server
1. Install the virtual environment:
```py -m venv venv```    
   Activate: 
```. venv/Scripts/activate```

2. Upgrade pip version:
```py -m pip install --upgrade pip```    
   Install dependencies from requirements.txt:
```pip install -r requirements.txt```

3. Apply the migrations:
```alembic upgrade head``` 

5. Run the app!
```uvicorn app.main:app --reload```


### Example
**Create a new short link:**    
_POST .../api/id_ 
``` 
    {
        "url": "https://github.com/Zorik28/yacut/blob/master/README.md"
    }
```

**Response:**
```
    {
        "short_link": "http://127.0.0.1:5000/NuTJNQ",
        "url": "https://github.com/Zorik28/yacut/blob/master/README.md"
    }
```


### Author
Karapetian Zorik   
Russian Federation, St. Petersburg, Kupchino.