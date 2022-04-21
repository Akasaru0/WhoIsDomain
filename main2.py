from ast import arg
import whois
import argparse
import csv
#____    __    ____  __    __    ______      __       _______.   _______   ______   .___  ___.      ___       __  .__   __. 
#\   \  /  \  /   / |  |  |  |  /  __  \    |  |     /       |  |       \ /  __  \  |   \/   |     /   \     |  | |  \ |  | 
# \   \/    \/   /  |  |__|  | |  |  |  |   |  |    |   (----`  |  .--.  |  |  |  | |  \  /  |    /  ^  \    |  | |   \|  | 
#  \            /   |   __   | |  |  |  |   |  |     \   \      |  |  |  |  |  |  | |  |\/|  |   /  /_\  \   |  | |  . `  | 
#   \    /\    /    |  |  |  | |  `--'  |   |  | .----)   |     |  '--'  |  `--'  | |  |  |  |  /  _____  \  |  | |  |\   | 
#    \__/  \__/     |__|  |__|  \______/    |__| |_______/      |_______/ \______/  |__|  |__| /__/     \__\ |__| |__| \__| 
#Author : Audric Lorthios

def promptInformation(domains, information):
    for domain in domains.split("|"):
        print('[x] Query the TLDs for information about the domain : '+domain)
        resp = whois.whois(domain)
        print('[x] Query received')
        print('[x] Query Information :')
        for info in information.split("|"):
            print('     ~> '+str(info)+' :'+str(resp[info]))

def extract2csv(domains,information,output):
    with open(output+'.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile,delimiter='/')
        #Header of the CSV file
        header = []
        for info in information.split("|"):
            header.append(info)
        writer.writerow(header)

        for domain in domains.split("|"):
            if args.verbose <=1 :
                print('[x] Query the TLDs for information about the domain : '+domain)
            resp = whois.whois(domain)
            line = []
            #Content of the CSV
            for info in information.split("|"):
                line.append(resp[info])
            writer.writerow(line)
    if args.verbose <=1 :
        print("Wrinting finished")


if __name__ == '__main__':
    #Gestion des arguments
    parser = argparse.ArgumentParser(description='Get Information About a Domain Name')
    parser.add_argument('-d','--domain',dest='domain',help='The domain name to be checked. You can add more domains with the seperator \'|\'',required=True)
    parser.add_argument('-o','--output-file',dest="output",help='Output File Name. If not specify the result will just be printed')
    parser.add_argument('-i','--informaiton',dest='information',default="creation_date|registrar|city",help='Information about the domain. You can add more information with the seperator \'|\'')
    args = parser.parse_args()
    
    domain_name = args.domain
    information = args.information  
    if str(args.output) == "None":
        promptInformation(domain_name,information)
    else:
        extract2csv(domain_name,information,args.output)