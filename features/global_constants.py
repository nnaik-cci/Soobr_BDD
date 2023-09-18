import random

username_admin_qa = "neha.naik"
password_admin_qa = "Eqw6OVJL2TBk40PZmAaS"
economic_entity_name = "Creative Capsule"
header_economic_entity = "Economic entity"

username_admin_stage = "neha.naik"
password_admin_stage = "m1SOMaIqhD0PnGMFWVQa"

validation_login_url = "Error! Default url route should be log in"

# create data
randGen = random.SystemRandom()
for x in range(0, 10):
    Ran_no = 10 + randGen.randint(0, 499)
new_ee_name = "Auto_Test" + str(Ran_no)
new_ee_label = "label_auto1"

cleaning_areas_url = "https://soobr-cockpit-staging.testing.soobr.ch/cockpit/economic-entity/132/map/cleaning-areas" \
                     "/cleaning-area"
tour_activities_url="https://soobr-cockpit-staging.testing.soobr.ch/cockpit/economic-entity/132/map/cleaning-areas" \
                    "/cleaning-tour-planning"

validation_incorrect_url="Error! Incorrect page opened!"
