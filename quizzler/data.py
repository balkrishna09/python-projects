import requests
amount =1
paramter = {
    'amount': 10,
    'type': 'boolean'
}

# URl with direct parameter
#response = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')

# URL by giving parameter manually
response = requests.get(url='https://opentdb.com/api.php', params=paramter)
data = response.json()
question_data = data['results']