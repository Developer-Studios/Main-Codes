#instructions below
#enter a website for ex:www.google.com
#then it return ip address of that website
#IP (Internet Protocol) Address is an address of your network hardware.

from socket import *
host=input()
try:
    addr=gethostbyname(host)
    print("IP Address of website is"+" "+addr)
except gaierror:
    print("The website doesn't exist")
p=gethostname()
q=gethostbyname(p)
print("Your pc name is "+p)
print("Your ip address is "+q)
