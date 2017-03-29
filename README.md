# PySQL
Simple API service for a MySQL database (Python 2.7).

## Installation

##### Linux

Install required packages (assuming root):
```
apt-get update
apt-get install python2.7
apt-get install mysql-server
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
<Change "port" value to the port you use for MySQL>
<Change "user" value to whatever username you prefer (root by default)>
<Change "pass" value to the password for that username within MySQL (admin by default)>
```

Run PySQL:
```
cd ./path/to/PySQL
python pysql.py
```
