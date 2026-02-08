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

# simple print  print
print("===== Simple =====")
print(device)
print(device['model'])
print()


# pp 
print("===== pretty print =====")
pprint(device)
print()

# use loop to format 
print("===== custom print using f string  ==== ")
for key,value in device.items():
    print(f"{key:>16s} : {value}")

