capital = { "France" : "Paris",
            "Germany": "Berlin"
}
travel_log = {
    "France": ["paris", "Lile", "Dijan"],
    "Germany": ["Berlin", "Munich", "Stuttgart"]
}
print(travel_log["France"] [1])


nested_list = ["a", "b", ["c", "d"]]
print(nested_list[2][1])
travel_log = {
    "france":{
        "cities_visited" :["paris", "Lile", "Dijon"],
        "total_visits": 12
    },

    "Germany": {
        "cities_visited": ["Berlin", "Munich", "stuttgart"],
        "total_visits": 8
    },
}
print (travel_log["Germany"] ["cities_visited"] [2])