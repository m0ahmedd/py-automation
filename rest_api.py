
################################
##### JSON dumps:
# import json
# 
# people = [
#   {
#     "name": "Sabrina Green",
#     "username": "sgreen",
#     "phone": {
#       "office": "802-867-5309",
#       "cell": "802-867-5310"
#     },
#     "department": "IT Infrastructure",
#     "role": "Systems Administrator"
#   },
#   {
#     "name": "Eli Jones",
#     "username": "ejones",
#     "phone": {
#       "office": "684-348-1127"
#     },
#     "department": "IT Infrastructure",
#     "role": "IT Specialist"
#   }
# ]
# people_json = json.dumps(people)
# print(people_json)
# o/p --> [{"name": "Sabrina Green", "username": "sgreen", "phone": {"office": "802-867-5309", "cell": "802-867-5310"}, "department": "IT Infrastructure", "role": "Systems Administrator"}, {"name": "Eli Jones", "username": "ejones", "phone": {"office": "684-348-1127"}, "department": "IT Infrastructure", "role": "IT Specialist"}]

##################################
##### REST POST :
# p = {"description": "white kitten",
#      "name": "Snowball",
#      "age_months": 6}
# response = requests.post("https://example.com/path/to/api", data=p)

##################################
#! /usr/bin/env python3
import os
import requests
import json


files_path = "./feedback"
url = "http://35.230.22.255/feedback"
# Get list of files included in the directory
feedback_list = []
onlyfiles = [f for f in os.listdir(files_path) if os.path.isfile(os.path.join(files_path,f))]
for f in onlyfiles:
    with open(os.path.join(files_path,f)) as feedback:
        for current_line_no, line in enumerate(feedback, start=1):
            if current_line_no == 1:
                title = line.strip()
            elif current_line_no == 2:
                name = line.strip()
            elif current_line_no == 3:
                date = line.strip()
            elif current_line_no == 4:
                feedback_content = line.strip()
        review = {
            "title": str(title),
            "name": name,
            "date": date,
            "feedback": feedback_content
        }
        
        feedback_json = json.dumps(review)
        response = requests.post(url, data=feedback_json)
        
        # # Print the data being sent for debugging
        # print("Sending review in json:", feedback_json)
        
        # Print response status code for debugging
        print(response.status_code)
        
        # # Print response content for debugging
        # print(f"Response content: {response.content.decode()}")
        
        # print(response.json())

        # print(review)
        # feedback_list.append(review)

# Turn feedback_list into a json usin json.dumps()
# feedback_json = json.dumps(feedback_list)
# print (feedback_json)

# POST feedback_json to the API
# response = requests.post("http://34.66.141.170/feedback", data=feedback_json)
# print(response.status_code)

