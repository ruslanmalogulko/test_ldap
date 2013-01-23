import ldap

server = 'ldap://172.22.64.41:389'
username = r'' #dc.dc\name
password= ''
base_dn='ou=Technical,dc=nc,dc=local'

l = ldap.initialize(server)
l.protocol_version = 3
try :
	l.simple_bind_s(username,password)
	searchFilter = "cn=*"
	retrieveAttributes = ['cn']
	results = l.search_s(base_dn,ldap.SCOPE_SUBTREE,searchFilter, retrieveAttributes)
	print results
except ldap.LDAPError:
	print "Sorry"
#print s
