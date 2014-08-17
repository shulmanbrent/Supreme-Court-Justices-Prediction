import os

for year in range(1955,2014):
    newpath = os.path.join(os.getcwd(), year)
    if not os.path.exists(newpath): os.makedirs(newpath)