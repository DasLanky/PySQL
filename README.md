# PySQL
Simple API service for a MySQL database (Python 2.7).

## Installation

##### Linux

Install required packages (assuming root):
```
apt-get update
apt-get install python2.7
apt-get install mysql-server
apt-get install python-mysql.connector
apt-get install python-openssl
```

Clone the repository:
```
cd ./path/to/projects/folder
git clone https://github.com/DasLanky/PySQL.git
```

## Running PySQL Server

##### Linux

Assuming that you can configure the MySQL server.

Configure PySQL:
```
cd ./path/to/PySQL
vi pysql.properties
<Change "server_port" value to the port you use for listening>
<Change "user" value to whatever username you prefer (root by default)>
<Change "pass" value to the password for that username within MySQL (admin by default)>
<Change "dbname" to the database to manipulate>
<Change other parameters as necessary>
```

Generate a certificate for PySQL SSL (only if client uses SSL):
```
python mk_simple_certs.py
```

Run PySQL:
```
cd ./path/to/PySQL
python pysql.py
```
