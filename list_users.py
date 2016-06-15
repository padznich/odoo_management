from odoo_connect import client


def show_users():

    proxy = client.model('res.users')
    # No need to use the model.search method, the model.browse method accepts a domain
    users = proxy.browse([])

    for user in users:
        print("{user.id} {user.name}".format(user=user))

if __name__ == "__main__":

    show_users()
