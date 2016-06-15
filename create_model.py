from odoo_connect import client


def create_model():

    model_proxy = client.model('ir.model')
    field_proxy = client.model('ir.model.fields')

    values = {
        'model': 'x_contact',
        'name': 'Contact',
        'state': 'manual',
    }

    # With this instruction, you are going to create the model
    # in the database without one line of python code.
    model = model_proxy.create(values)

    values = {
        'name': 'x_firstname',
        'ttype': 'char',
        'size': 64,
        'field_description': 'Firstname',
        'model_id': model.id,
        'model': model.model,
        'domain': '[]',
    }
    field = field_proxy.create(values)

#####################
contact_proxy = client.model('x_contact')
contact_proxy.create({'x_firstname': 'Stephane'})

for contact in contact_proxy.browse([]):
    print(contact.x_firstname)