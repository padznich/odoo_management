from odoo_connect import client


def install_module(module_to_install='base_import_module'):

    if module_to_install in client.modules('')['uninstalled']:

        print("Checked module in uninstalled")

        client.install(module_to_install)

        if module_to_install in client.modules('')['installed']:

            print("Module \"{}\" successfully installed".format(module_to_install))

    proxy = client.model('ir.module.module')
    proxy.update_list()

if __name__ == "__main__":

    install_module()
