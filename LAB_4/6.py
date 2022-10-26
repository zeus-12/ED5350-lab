metro_cities = {"Mumbai", "Chennai", "New Delhi", "Pune", "Bangalore"," Hyderabad"}
coastal_cities = { "Surat", "Vizag", "Chennai", "Panaji", "Mumbai", "Cochin"}

# metro and coastal
print(metro_cities & coastal_cities)

# metro or coastal but not both
print(metro_cities ^ coastal_cities)
