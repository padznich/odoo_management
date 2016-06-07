import erppeek


client = erppeek.Client('http://localhost:8069', 'odoo_with_pad', 'pad@mail.ru', 'padznich')

proxy = client.model('ir.module.module')
installed_modules = proxy.browse([('state', '=', 'installed')])

print("Installed modules are:")

for module in installed_modules:

    print("\t {}".format(module))
