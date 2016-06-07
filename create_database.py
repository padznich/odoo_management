import erppeek

DATABASE = "odoo_with_create_test3"
SERVER = "http://localhost:8069"
ADMIN_PASSWORD = "admin"

client = erppeek.Client(server=SERVER)

if DATABASE not in client.db.list():

    print("The DB does not exist yet, creating.....")
    client.create_database(ADMIN_PASSWORD, DATABASE)

    if DATABASE in client.db.list():
        print("\"{}\" successfully added.".format(DATABASE))

else:

    print("The DB \"" + DATABASE + "\" already exist.")
