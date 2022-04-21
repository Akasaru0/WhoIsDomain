#import argparse

#parser = argparse.ArgumentParser(description='Get Information About a Domain Name')
#parser.add_argument('-d','--domain',help='The domain name to be checked',required=True)
#parser.add_argument('-o','--ouput-file',help='Ouput File Name. If not specify the result will just be printed')

from whoisapi import *
import json

client = Client(api_key='at_ws24xwuGq75oCQYMZXD7Egc1B3qcU',outputFormat='JSON')
# Get parsed whois record as a model instance.
domain_name = 'tryhackme.com'
print('[x] Query WhoisAPIXML for the domain :'+domain_name)
whois = json.loads(client.raw_data(domain_name))
print(whois)
print(type(whois))
print('[x] Query received')
# Get particular field of the whois record
print('[x] Query Information :')
print('     ~> Creation Date :'+whois["WhoisRecord"]["createDate"])
print('     ~> Name of the Registrant : '+whois["WhoisRecord"]["registrant"]["name"])
print('     ~> Organization : '+whois["WhoisRecord"]["administrativeContact"]["organization"])
#print(whois)


#print(whois.created_date_raw+" / "+whois.domain_name+" / "+whois.registrant.organization)

# Get raw API response
#resp_str = client.raw_data('whoisxmlapi.com')
#print(resp_str["WhoisRecord"]["registrant"]["organization"])