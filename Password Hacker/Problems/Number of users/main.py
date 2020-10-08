# write your code here
with open("users.json") as json_file:
    dict_from_json = json.load(json_file)
    users_list = dict_from_json['users']
    print(len(users_list))
