
import pyad.adquery
import pyad.adsearch
import pyad.adobject
import pyad.adcomputer
import pyad.adcontainer
import pyad.adgroup
import pyad.aduser
import pyad.addomain
import pyad.pyad


from pyad import pyadutils, adgroup


class ADGroup(pyad.ADObject):



def create(cls, name, container_object, security_enabled=True, scope='GLOBAL', optional_attributes={}):
    return container_object.create_group(name=name,
                                         security_enabled=security_enabled,
                                         scope=scope,
                                         optional_attributes=optional_attributes)
def add_members(self, members):
    members = map(lambda member: member.dn, pyadutils.generate_list(members))
    return self.append_to_attribute('member', members)
print()


pyad.adgroup. ADGroup(distinguished_name=None,adsi_ldap_com_object=none)






