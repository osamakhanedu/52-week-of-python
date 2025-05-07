from pprint import pprint

# dictionary 

device = {
    "name": "sbx-n9",
    "vendor": "cisco",
    'model': "Modle", 
    "os": "nxos",
    "version": "9.3",
    "ip": "10.1.11"
}

# print 
print("=== Simple === ")
print(device)
print(device['model'])


# pp 
print("=== prety pring === ")
pprint(device)

# use loop to format 
pprint("print using loop ")
for key,value in device.items():
    print(f"{key:>16s} : {value}")

