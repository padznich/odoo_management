from odoo_connect import client


def show_all_modules():

    proxy = client.model('ir.module.module')
    proxy.update_list()

    for k, v in client.modules('').items():

        print(k.capitalize())

        for i_module in v:
            print("\t {}".format(i_module))

if __name__ == "__main__":

    show_all_modules()
