import netCDF4 as nc
import numpy as np

dir = "C:/Users/smrTu/OneDrive/Documents/GithubC/CDIF/integrationPublic/exampleMetadata/WDCC_NetCDF/"
filename = "sftlf_fx_AWI-CM-1-1-MR_ssp370_r1i1p1f1_gn.nc"
#dir = "C:/Users/smrTu/OneDrive/Documents/GithubC/CDIF/integrationPublic/ExampleData/"
#dir = "C:/Users/smrTu/Downloads/"
#filename = '20231120_002_1mg_Murchison_Smithsonian.cdf'
#filename = "hur_Amon_UKESM1-0-LL_1pctCO2-cdr_r1i1p1f2_gn_255001-263912.nc"
ds = nc.Dataset(dir + filename, 'r')

# print("variables: ", ds.variables)
print("variables keys", ds.variables.keys)

for dim in ds.dimensions.values():
 print("dimension: ", dim)

print('...............')

for var in ds.variables.values():
    print("variable: ", var)
    print('.....')

print("###############################")
print("keys and values in dataset")
for akey in ds.__dict__.keys():
    if ds.__dict__[akey]:
        print(f'{akey}: {ds.__dict__[akey]}')
    else:
        print(f'{akey}, no value')