# Make sure that Postgresql installed

db_name='stock_tools_db'
username='admin'
password='12345678'

sudo -u postgres psql -U postgres -c "DROP DATABASE IF EXISTS ${db_name};"
sudo -u postgres psql -c "CREATE DATABASE ${db_name};"
sudo -u postgres psql -c "DROP USER IF EXISTS ${username};"
sudo -u postgres psql -c "CREATE USER ${username} PASSWORD '${password}';"