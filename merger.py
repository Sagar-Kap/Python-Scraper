import pandas as pd

notino = pd.read_csv("notino.csv").astype(object)
technomarket = pd.read_csv("technomarket.csv").astype(object)
zora = pd.read_csv("Zora.csv").astype(object)
technopolis = pd.read_csv("technopolis.csv").astype(object)
emag = pd.read_csv("emag.csv").astype(object)



a = pd.concat([notino.set_index('Model'),technomarket.set_index('Model'), zora.set_index('Model'), 
	technopolis.set_index('Model'), emag.set_index("Model")], axis=1)

a = a.fillna(0)

a.columns = ('Notino', 'Technomarket', 'Zora', "Technopolis", "Emag")
b =a.reset_index()
print(b)
b.to_csv("Merged_Products.csv", index = False)

