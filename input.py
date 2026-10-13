hesaru = input("Dayaviṭṭu nimma hesarannu namūdisi: ")
print("Namaskāra, " + hesaru +  "!")

hudugana_hesaru = input("Dayaviṭṭu hudugana hesarannu namūdisi: ")

hudugana_age = input("Dayaviṭṭu hudugana vayassannu namūdisi: ")

hudugiya_hesaru = input("Dayaviṭṭu hudugiya hesarannu namūdisi: ")

hudugiya_age = input("Dayaviṭṭu hudugiya vayassannu namūdisi: ")

age_difference = abs(int(hudugana_age) - int(hudugiya_age))


print("Age difference between " + hudugana_hesaru + " and " + hudugiya_hesaru + " is " + str(age_difference))
print(f"Age difference between {hudugana_hesaru} and {hudugiya_hesaru} is {age_difference}")