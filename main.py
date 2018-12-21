from bs4 import BeautifulSoup
import urllib3.request
import certifi
import sys

if __name__ == "__main__":

    i = 0
    http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())

    source = BeautifulSoup(http.request("GET", sys.argv[1]).data, "html.parser")

    for image in source.findAll("span", {"class":"mdCMN09Image"}):
        style = image["style"]
        url = style[style.find("(")+1:style.find(")")]
        print("Downloading sticker " + str(i+1))
        content = http.request("GET", url)
        f = open(str(i+1)+".png", "wb")
        f.write(content.data)
        f.close
        
        i+=1

