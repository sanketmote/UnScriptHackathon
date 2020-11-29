# mercuri

## UnScript Rookie’s Hackathon 2020

<h3>COVID19 Hospital Management System</h3>

Created a COVID-19 patients management
and tracking web application for a Hospital.

Should you choose to work on the existing pushed DB,

username = admin

password = admin

### specification

1. The user/admin will enter the Name, Address, Current  Symptoms, Contact Details, Health Details and other details of the patient and will assign a bed to the respective patient
2. Only the management can insert and modify the patient data and health status of the patient. Also, created a dashboard for hospital management where they can see the status of the recovered, admitted ,deceased patients and bed availability.
3. Interface to insert and modify patient’s medical data in hospital database including symptoms of patient showed at the time of admission
4. Interface to search of a particular patient
5. symptom checker covid 19 chatbot

# Get the code

```$ git clone https://github.com/sanketmote/mercuri.git```

```$ cd mercuri```



# Install related modules 

```$ pip install asgiref```

```$ pip install autopep8```

```$ pip install Django```

```$ pip install pycodestyle```

```$ pip install pytz```

```$ pip install sqlparse```

```$ pip install Unipath```

```$ pip install dj-database-url```

```$ pip install python-decouple```

```$ pip install gunicorn```

```$ pip install whitenoise```




# Create tables

```$ python manage.py makemigrations```

```$ python manage.py sqlmigrate```
```$ python manage.py migrate```

# Start the application (development mode)


```$ python manage.py runserver ```      # default port 8000

# Start the app - custom port

```$ # python manage.py runserver 0.0.0.0:<your_port> ```

```$ # Access the web app in browser: http://127.0.0.1:8000/ ```
