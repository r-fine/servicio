## How to install:
#### 1. Install [Python3.9](https://www.python.org/downloads/release/python-3913/) on your computer
#### 2. [Download](https://github.com/r-fine/tasker.git) or clone the repository 
```
git clone https://github.com/r-fine/servicio.git
```
#### 3. Open project folder on vscode
#### 4. Open terminal
#### 4. Make a virtual environment
```
python3 -m venv venv
```
#### 5. Activate virtual environment
For Linux and macOS:
```
source ./venv/bin/activate
```
For Windows:
```
venv/Scripts/activate
```
#### 6. Install requirements file
```
pip install -r requirements.txt
```
#### 7. Migrate database and create superuser
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
#### 8. Run the server
```
python manage.py runserver
```
#### 9. Go to localhost:8000 or 127.0.0.1:8000 on your browser
