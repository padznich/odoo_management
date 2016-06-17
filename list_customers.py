from odoo_connect import client


def show_users():

    proxy = client.model('res.partner')
    users = proxy.browse([])

    limit = 30
    d = 0
    for user in users:
        if d == limit:
            break
        print(u"{user.name}___{user.email}__{user.phone}".format(user=user))
        d += 1

if __name__ == "__main__":

    show_users()
