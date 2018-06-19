### Requirements

* docker-compose or an activated python virtualenv with docker-compose installed.

Docker-compose installation in the local environment, Follow the link with the instructions about how to install docker compose:
```bash
https://docs.docker.com/compose/install/#install-compose
```
The second option is create an virtualenv installation/activation example:
```bash
pip install virtualenv
virtualenv scheduling_api
source scheduling_api/bin/activate
pip install -U docker-compose
```

#### After installation of all the above requirements:

### Installing the project

Clone the repository and install it:

```bash 
git clone https://github.com/julianoalmeida/challenge_api.git
```

Go to `sources root` directory:

You now need to sync your database for the first time and create an initial user and set a password for that user.
And run the following command:

```bash
docker-compose run app python manage.py migrate
docker-compose run app python manage.py createsuperuser --email admin@admin --username admin

```

### WARNING: Before running the tests it's necessary to start the application

Starting the application:

```bash
docker-compose up
```
Before running the tests, you need to open another terminal in application root directory and execute de command below:

```bash
docker-compose run app python manage.py test api -v 2
```

### After the execution of all the above commands, your scheduling api is prepared to be used.

To access the application just follow the url:
```bash
http://127.0.0.1:8000/api/
```

### WARNING: By default it's necessary to create an patient and procedures before use the scheduling endpoint

To access the patient, procedure or scheduling endpoint follow the url:
```bash
http://127.0.0.1:8000/api/patient/
http://127.0.0.1:8000/api/procedure/
http://127.0.0.1:8000/api/scheduling/
```
