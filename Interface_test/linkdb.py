from xmlrpc import client

server_url = 'http://localhost:8069'
db_name = 'odoo_01'
username = 'odoo_01'
password = 'odoo_01'

common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
user_id = common.authenticate(db_name, username, password, {})

if user_id:
    print("Success: User id is", user_id)
else:
    print("Failed: wrong credentials")

models =  client.ServerProxy('%s/xmlrpc/2/object' % server_url)
if user_id:
    #验证账户在模型里面是否有create的权限
    has_access = models.execute_kw(db_name, user_id, password,
                                   'todo.task', 'check_access_rights',
                                   ['create'], {'raise_exception': False})
    print('Has create access on todotask:', has_access)
else:
    print('Wrong credentials')
