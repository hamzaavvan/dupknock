import os
import sys

ext = 'txt'
dname = sys.argv[1]

if len(sys.argv) ==2:
	ext = sys.argv[2]

subdomains=[]

# List all subdirectories using scandir()
def main(basepath, temp=[], ext='txt'):
    exts = ext.split(',')

    with os.scandir(basepath) as entries:
        for entry in entries:
            temppath = basepath

            if entry.is_dir():
                temppath = temppath+'/'+entry.name
                main(temppath, temp)
            else:
                if entry.name.split('.')[-1] not in exts: continue

                temppath = temppath+'/'+entry.name
                print("[+] Reading "+entry.name)

                with open(temppath) as f:
                    for subdomain in f:
                        if subdomain in temp: continue

                        if len(subdomain) >0:
                            temp.append(subdomain)



main(dname, subdomains, ext)

fh = open('./finals.txt', 'w+')
print("[-] Writing to final.txt")
for d in subdomains:
    fh.write(d)

fh.close()
