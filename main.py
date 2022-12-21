from replit import db
import os

# Store my name in the replit db
# db['name'] = 'Dave'

print(db['name'])

keys = db.keys()

print(keys)

for key in db:
  print(db[key])

myApiKey = os.environ['apiKey']
print(myApiKey)



