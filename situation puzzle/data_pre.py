import json

with open('sp.json') as user_file:
    file_contents = user_file.read()

sp_data = json.loads(file_contents)



data = json.dumps(sp_data, indent=1)
with open("sp_data.json", 'w', newline='\n') as f:
    f.write(data)




