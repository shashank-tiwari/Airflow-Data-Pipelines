This repo is to capture the steps for Airflow installation, setup and creating some simple data pipelines based on udemy tutorial by Marc.

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

### Configure Local Executor 
To execute multiple tasks in parallel where a task becomes a sub process in a single machine.

1. Install Postgres for metastore
```sh
# To refresh your packages in your virtual env
sudo apt update
# To install Postgres
sudo apt install postgresql
```

2. Connect to postgres and set password for postgres user
```sh
sudo -u postgres psql
ALTER USER postgres PASSWORD 'postgres';
```

3. Install airflow postgres package
```sh
pip install 'apache-airflow[postgres]'
```

4. Edit airflow.cfg file for using postgres as Metastore and set LocalExecutor
```sh
sql_alchemy_conn = postgresql+psycopg2://postgres:postgres@localhost/postgres
executor = LocalExecutor

#Check if you are able to reach postgres database -
airflow db check
```

5. Stop airflow webserver and scheduler

6. Initiate Apache Airflow Metastore    
```sh
airflow db init
```

7. Re-create admin account
```sh
airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org
```
8. Start the web server and scheduler
```sh
airflow webserver
airflow scheduler
```
> Go to localhost:8080 and verify 

### Airflow User Data Pipeline

![dag](png/user_processing.PNG)
> Structure of the Airflow User Data Pipeline

### Airflow Parallel DAG Pipeline

![dag](png/parallel_dag.PNG)

### Airflow DAG Example for Task Groups

![dag](png/example_taskgroups.PNG)

### Airflow DAG Example for XCOM and Branching

![dag](png/xcom_dag.PNG)

### Airflow Elastic Search Plugin Example 
As part of this example, followings are covered - 
1. Created ElasticHook to connect to Elastic search and add a doc to index
2. Created PgToEsOperator to get data from postgres and add it to Elastic search
3. Created a dag to print elastic search info and get connections from postgres and add it to elastic search

![dag](png/elasticsearch_dag.PNG)
