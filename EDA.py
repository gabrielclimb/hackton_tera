import pandas as pd
carac = pd.read_csv("caracteristics.csv", encoding="latin-1")
holi = pd.read_csv("holidays.csv", encoding="latin-1")
places = pd.read_csv("places.csv", encoding="latin-1")
users = pd.read_csv("users.csv", encoding="latin-1")
veh = pd.read_csv("vehicles.csv", encoding="latin-1")

places.lartpc = places.lartpc.fillna(0)

places.larrout.isnull().mean()

places.larrout = places.larrout.fillna(0)