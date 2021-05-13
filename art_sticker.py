import csv
def imageProvider(userstring, category):
    category_values = {
            "human" : "set5",
            "kitten" : "set4",
            "monster" : "set2",
            "robots" : "set3",
            "peaky_robos" : "set1"} 
    users_value = ""
    if category == "":
        request_string = f"https://robohash.org/{userstring}"
    else :
        users_value = category_values[f"{category}"]
        request_string = f"https://robohash.org/{userstring}?set={users_value}"
    with open("./records/image_art_provider.csv", "a") as provider:
        image_info = csv.writer(provider)
        image_info.writerow([userstring,users_value])
    return request_string
    