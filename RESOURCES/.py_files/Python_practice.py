print("Hello World")
num_candiates = 3
winning_percentage = 73.81
candiate_name = "Diane"
won_election = True
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
print(counties[0])
len(counties)
print(counties[0:2])
print(counties[:2])
print(counties[1:])
counties.append("El Paso")
print(counties)
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(-1)
print(counties)
counties[2] = "El Paso"
print(counties)
counties.insert(1, "El Paso")
counties.remove("Arapahoe")
print(counties)
counties[1] = "El Paso"
print(counties)
counties.pop(2)
print(counties)
counties[1] = "Jefferson"
print(counties)
counties.insert(2, "Denver")
print(counties)
counties.append("Arapahoe")
print(counties)
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
print(len(counties_tuple))
print(counties_tuple[1])
counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})
print(voting_data)
voting_data.insert(1, {"county": "El Paso", "registered_voters": 461149})
print(voting_data)
voting_data.remove({"county": "Arapahoe", "registered_voters": 422829})
print(voting_data)
voting_data[1] = {"county": "Jefferson", "registered_voters": 432438}
voting_data[2] = {"county": "Denver", "registered_voters": 463353}
print(voting_data)
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
print(voting_data)

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print("{} county has {} registered voters.".format(county, voters))

voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353},
               {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes/ total_votes * 100}% of the total votes.")

