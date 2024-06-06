dicti = {
  "name": "magc",
  "age": "da",
  "year": "sanad",
}
print(dicti)

#list
list = ["muuse","cali","yaxye","ahmed"]
print(list)

#change list to set()
list_set = set(list)

print(list_set)


# add set()
list_set.add("mulki")
print(list_set)


# two set() update
girls = {"mulki","caisha","ikran","aniso"}
boys ={"Ahmed","abdi","ali","moha","mulki"}

girls.update(boys)
print(girls)

# remove set()
girls.remove("ikran")
print(girls)

#union
girls = {"mulki","caisha","ikran","aniso"}
boys ={"Ahmed","abdi","ali","moha","mulki"}
total = girls.union(boys)
print(total)


