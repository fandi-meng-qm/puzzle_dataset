import json

with open('riddle.json') as user_file:
    file_contents = user_file.read()

riddle_data = json.loads(file_contents)
# print(jeopardy_data)


data = json.dumps(riddle_data, indent=1)
with open("riddle_data.json", 'w', newline='\n') as f:
    f.write(data)




