#!/usr/bin/env python
#_*_ coding: utf8 _*_

import dns.resolver

import argparse
import time
import os

parser = argparse.ArgumentParser(description="Obtener información mediante DNS")
parser.add_argument('-w','--web',help="Indica una web")
parser = parser.parse_args()


def main():
    if parser.web:
        print("Posibles errores:  1.Quita el 'https://www.' al final de la web. ejemplo: example.com")
        print("                   2.Comprueba si la web esta bien escrita")
        time.sleep(5)
        print("    3")
        time.sleep(1)
        print("  2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        os.system('cls')

        print()
        n = "Host Address IPv4"
        try:
            a = dns.resolver.resolve(parser.web,"A")
            for x in a:
                print(f"Host Address IPv4: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Host Address IPv6"
        try:
            a = dns.resolver.resolve(parser.web,"AAAA")
            for x in a:
                print(f"Host Address IPv6: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Authoritative name server"
        try:    
            a = dns.resolver.resolve(parser.web,"NS")
            for x in a:
                print(f"Authoritative name server: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Mail destination"
        try:
            a = dns.resolver.resolve(parser.web,"MD")
            for x in a:
                print(f"Mail destination: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Mail forwarder"
        try:                            
            a = dns.resolver.resolve(parser.web,"MF")
            for x in a:
                print(f"Mail forwarder: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Canonical name for an alias"
        try:                            
            a = dns.resolver.resolve(parser.web,"CNAME")
            for x in a:
                print(f"Canonical name for an alias: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Start of a zone of authority"
        try:                            
            a = dns.resolver.resolve(parser.web,"SOA")
            for x in a:
                print(f"Start of a zone of authority: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Mailbox domain name"
        try:                            
            a = dns.resolver.resolve(parser.web,"MB")
            for x in a:
                print(f"Mailbox domain name: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Mail group member"
        try:                            
            a = dns.resolver.resolve(parser.web,"MG")
            for x in a:
                print(f"Mail group member: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Mail rename domain name"
        try:                            
            a = dns.resolver.resolve(parser.web,"MR")
            for x in a:
                print(f"Mail rename domain name: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Null RR"
        try:                            
            a = dns.resolver.resolve(parser.web,"NULL")
            for x in a:
                print(f"Null RR: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Well known service description"
        try:                            
            a = dns.resolver.resolve(parser.web,"WKS")
            for x in a:
                print(f"Well known service description: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Domain name pointer"
        try:                            
            a = dns.resolver.resolve(parser.web,"PTR")
            for x in a:
                print(f"Domain name pointer: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Host information"
        try:                            
            a = dns.resolver.resolve(parser.web,"HINFO")
            for x in a:
                print(f"Host information: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Domain name pointer"
        try:                            
            a = dns.resolver.resolve(parser.web,"PTR")
            for x in a:
                print(f"Domain name pointer: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Mailbox or mail list information"
        try:                            
            a = dns.resolver.resolve(parser.web,"MINFO")
            for x in a:
                print(f"Mailbox or mail list information: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")
    
        print()
        n = "Mail exchange"
        try:                            
            a = dns.resolver.resolve(parser.web,"MX")
            for x in a:
                print(f"Mail exchange: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Text strings"
        try:                            
            a = dns.resolver.resolve(parser.web,"TXT")
            for x in a:
                print(f"Text strings: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")
        
        print()
        n = "Transfer of an entire zone"
        try:                            
            a = dns.resolver.resolve(parser.web,"AXFR")
            for x in a:
                print(f"Transfer of an entire zone: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Mailbox-related records"
        try:                            
            a = dns.resolver.resolve(parser.web,"MAILB")
            for x in a:
                print(f"Mailbox-related records: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")

        print()
        n = "Mail agent RR"
        try:                            
            a = dns.resolver.resolve(parser.web,"MAILA")
            for x in a:
                print(f"Mail agent RR: {x}")

        except:
            print(f"ERROR: No se ha podido obtener la consulta '{n}' :c")



    else:
        print("Escoje una web :v")
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo..")
        exit()