# QRkot_spreadseets

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

5. Run!
```uvicorn app.main:app --reload```