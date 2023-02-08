# import requests
# import json


# def send_sms(number, message):
#     url = ' https://www.fast2sms.com/dev/bulkV2'
#     params = {
#         'authorization': '0odscIY3ianW9zUwBTLFblg2HuD7j48OtEJChV6rZMxvmeXkAf8mKDrOCdEbugInXSPN1wyZoevVTlaF',
#         'sender_id': 'FSTSMS',
#         'message': message,
#         'language': 'english',
#         'route': 'p',
#         'numbers': number
#     }
#     response = requests.get(url, params=params)
#     dic = response.json()
#     print(dic)



# send_sms("7905179730","this is youtube message")  
