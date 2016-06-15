from odoo_connect import client

for model in sorted(client.models()):

    print model
