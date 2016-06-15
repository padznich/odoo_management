import erppeek

db_name = 'db_t'
# db_name = 'odoo_db'
user_email = 'pad@mail.by'
password = 'odoo'


client = erppeek.Client('http://localhost:8069', db_name, user_email, password)