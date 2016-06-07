import erppeek


module_to_install = 'sale'

client = erppeek.Client('http://localhost:8069', 'odoo_with_pad', 'pad@mail.ru', 'padznich')

if module_to_install in client.modules('')['uninstalled']:

    print("Checked module in uninstalled")

    client.install(module_to_install)

    if module_to_install in client.modules('')['installed']:

        print("Module \"{}\" successfully installed".format(module_to_install))
