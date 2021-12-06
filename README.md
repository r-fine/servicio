# How to install:
### 1. Install [Python](https://www.python.org/downloads/) on your computer
### 2. [Download](https://github.com/r-fine/servicio.git) or clone the repository 
```
git clone https://github.com/r-fine/servisio.git
```
### 3. Open project folder on vscode
### 4. Open terminal
### 4. Make a virtual environment
For Linux and macOS
```
python3 -m venv venv
```
For Windows:
```
py -m venv venv
```
### 5. Activate virtual environment
For Linux and macOS:
```
source /venv/bin/activate
```
For Windows:
```
./Scripts/activate
```
### 6. Install requirements file
```
pip install -r requirements.txt
```
### 7. Migrate database and create superuser
For Linux and macOS:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
For Windows:
```
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
```
### 8. Run the server
For Linux and macOS:
```
python3 manage.py runserver
```
For Windows:
```
py manage.py runserver
```
### 9. Go to localhost:8000 or 127.0.0.1:8000 on your browser
