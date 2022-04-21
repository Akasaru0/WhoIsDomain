import whois
import argparse
import json
import csv

def promptInformation(domains, information):
    for domain in domains.split("|"):
        print('[x] Query the TLDs for information about the domain : '+domain)
        resp = whois.whois(domain)
        print('[x] Query received')
        print('[x] Query Information :')
        for info in information.split("|"):
            print('     ~> '+info+' :'+resp[info])

def extract2csv(domains,information,output):
    with open(output+'.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter='/')
        #Header of the CSV file
        header = []
        for info in information.split("|"):
            header.append(info)
        writer.writerow(header)

        for domain in domains.split("|"):
            print('[x] Query the TLDs for information about the domain : '+domain)
            resp = whois.whois(domain)
            line = []
            #Content of the CSV
            for info in information.split("|"):
                line.append(resp[info])
            writer.writerow(line)
    print("Wrinting finished")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get Information About a Domain Name')
    parser.add_argument('-d','--domain',dest='domain',help='The domain name to be checked. You can add more domains with the seperator \'|\'',required=True)
    parser.add_argument('-o','--output-file',dest="output",help='Output File Name. If not specify the result will just be printed')
    parser.add_argument('-i','--informaiton',dest='information',help='Information about the domain. You can add more information with the seperator \'|\'')
    args = parser.parse_args()
    
    domain_name = str(args.domain)
    information = str(args.information)

    if args.information == "None":
        information = "creation_date|registrar|city"
    
    if type(args.output) == NoneType:
        promptInformation(domain_name,information)
    else:
        extract2csv(domain_name,information,args.output)