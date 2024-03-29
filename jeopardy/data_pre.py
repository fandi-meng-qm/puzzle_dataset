import json

with open('jeopardy.json') as user_file:
    file_contents = user_file.read()

jeopardy_data = json.loads(file_contents)
# print(jeopardy_data)

for i in range(100):
    del jeopardy_data[i]['Show Number'], jeopardy_data[i]['Air Date'], jeopardy_data[i]['Round'], \
        jeopardy_data[i]['Category'], jeopardy_data[i]['Value']

print(jeopardy_data)

data = json.dumps(jeopardy_data, indent=1)
with open("jeopardy_data.json", 'w', newline='\n') as f:
    f.write(data)