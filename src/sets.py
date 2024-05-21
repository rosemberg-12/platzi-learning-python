# SET
countries = {"col", "pe", "ar"}

countries.update({"usa", "pe", "bol"})

print(countries)


# SET Union

countries_a = {"col", "pe", "ar"}
countries_b = {"usa", "pe", "bol"}

countries_union = countries_a.union(countries_b)
print(countries_union)
print(countries_a | countries_b)

countries_intersection = countries_a.intersection(countries_b)
print(countries_intersection)
print(countries_a & countries_b)

countries_difference = countries_a.difference(countries_b)
print(countries_difference)
print(countries_a - countries_b)

countries_symetric_difference = countries_a.symmetric_difference(countries_b)
print(countries_symetric_difference)
print(countries_a ^ countries_b)
