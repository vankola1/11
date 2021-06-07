from pyad import pyad
from pyad import adquery


def get_user_by_login(acc, search_base=None, options={}):
    ad_query = adquery.ADQuery()
    ad_query.execute_query(where_clause=("sAMAccountName = '%s'" % acc),
                           base_dn=search_base,
                           type="GC",
                           options=options)
    return pyad.from_dn(ad_query.get_single_result()['distinguishedName'])

def test():
    return 1

def main():
    user = pyad.from_cn("Комогорова Mарина Владимировна")
    print(user.get_attribute("sAMAccountName"))
    print(user.get_attribute("userPrincipalName"))

    q = get_user_by_login('kmarina')
    print(q)

    folder = pyad.adcontainer.ADContainer.from_dn('OU=PBI,OU=Services Groups,OU=SpecialAccounts,DC=komos,DC=local')
    print(folder)
    groups = folder.get_children()
    print(groups)
    for g in groups:
        print(g)
    print('123')


if __name__ == '__main__':
    main()

# group = pyad.from_cn("PBI_KG_Creatio_Br")
# print(group)

# group.add_members([user])

# for u in group.get_members():
#    print(u.cn)
