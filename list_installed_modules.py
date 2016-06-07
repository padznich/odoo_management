import erppeek


client = erppeek.Client('http://localhost:8069', 'odoo_with_pad', 'pad@mail.ru', 'padznich')

proxy = client.model('ir.module.module')
installed_modules = proxy.browse([('state', '=', 'installed')])

print("Installed modules are:")

for module in installed_modules:

    print("\t {}".format(module))


def show_all_modules():

    for k, v in client.modules('').items():

        print(k.capitalize())

        for i_module in v:
            print("\t {}".format(i_module))
