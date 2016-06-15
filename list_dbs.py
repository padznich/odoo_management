from odoo_connect import client


def show_dbs():


    for database in client.db.list():
       print('database: %r' % (database,))

if __name__ == "__main__":

    show_dbs()
