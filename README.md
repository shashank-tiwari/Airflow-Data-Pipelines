### Installation & Quick Start 

1. Create a python virtual environment to have an isolated environment for this exercise
```sh
python3 -m venv sandbox
```
2. Activate the venv - sandbox as below -  
```sh
source sandbox/bin/activate
```
3. Install Apache Airflow   
```sh
pip install wheel
pip3 install apache-airflow==2.0.0 --constraint <constraints-file.txt>
```
> In this case, we are installing Airflow 2.0.0 version. 
> **Wheel** is a built-package format, and offers the advantage of not recompiling your software during every install.
 
4. Initiate Apache Airflow Metastore    
```sh
airflow db init
```
> By default, Airflow uses **SQLite**, which is intended for development purposes only.

5. Create an admin account
```sh
airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org
```
6. Start the web server, default port is 8080 and start the scheduler in new terminal or run webserver with `-D` option to run it as a daemon
```sh
airflow webserver
airflow scheduler
```
> Go to localhost:8080 in the browser and use the admin account you just created to login.

### Airflow User Data Pipeline
Steps for Airflow installation, setup and creating a simple data pipeline based on udemy tutorial by Marc.

![dag](png/user_processing.PNG)
> Structure of the Airflow DAG