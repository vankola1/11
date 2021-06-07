import pyad.adquery
q = pyad.adquery.ADQuery()

q.execute_query(
    attributes = ["distinguishedName", "description"],
    where_clause = "objectClass = '*'",
    base_dn = "OU=users, DC=domain, DC=com"
)

for row in q.get_results():
    print row["distinguishedName"]