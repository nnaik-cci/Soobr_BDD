import random


uername_admin = "neha.naik"
password_admin = "Eqw6OVJL2TBk40PZmAaS"
economic_entity_name = "Creative Capsule"
header_economic_entity = "Economic entity"

validation_login_url = "Error! Default url route should be log in"

# create data
randGen = random.SystemRandom()
for x in range(0,10):
    Ran_no = 10 + randGen.randint(0,499)
new_ee_name = "Auto_Test"+str(Ran_no)
new_ee_label = "label_auto1"

