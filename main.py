import argparse

parser = argparse.ArgumentParser(description='Get Information About a Domain Name')
parser.add_argument('-d','--domain',help='The domain name to be checked',required=True)
parser.add_argument('-o','--ouput-file',help='Ouput File Name. If not specify the result will just be printed')

args = parser.parse_args()
domain_name = args.domain

from whoisapi import *
import json

client = Client(api_key='at_ws24xwuGq75oCQYMZXD7Egc1B3qcU',outputFormat='JSON')
# Get parsed whois record as a model instance.
print('[x] Query WhoisAPIXML for the domain :'+domain_name)
whois = json.loads(client.raw_data(domain_name))
print('[x] Query received')
# Get particular field of the whois record
print('[x] Query Information :')
print('     ~> Creation Date :'+whois["WhoisRecord"]["createdDate"])
print('     ~> Name of the Registrant : '+whois["WhoisRecord"]["registrant"]["name"])
print('     ~> Organization : '+whois["WhoisRecord"]["administrativeContact"]["organization"])