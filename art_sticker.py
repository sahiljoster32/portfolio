import requests

def imageProvider(userstring, category):
    category_values = {
            "human" : "set5",
            "kitten" : "set4",
            "monster" : "set2",
            "robots" : "set3",
            "peaky_robos" : "set1"}
    users_value = category_values[f"{category}"]
    if category == None:
        request_string = f"https://robohash.org/{userstring}"
    else :
        request_string = f"https://robohash.org/{userstring}?set={users_value}"
    response_image = requests.get(request_string)
    final_image = response_image.content
    with open("./static/assets/images/current.jpg" , "wb") as askedimage:
        askedimage.write(final_image)