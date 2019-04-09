import requests
import sys
def get_weather():
    city = sys.argv[1]
    try: 
        api_address = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=9f162c4a7576a32569f4374bd5fdff7b'
        json_data = requests.get(api_address).json()
        '''print ("It's {} in {}, with a temperature of {}, pressure {} and humidity {}.".format(json_data['weather'][0]['description'],\
                                                                                     city.capitalize(), json_data['main']['temp'],\
                                                                                     json_data['main']['pressure'],\
                                                                                     json_data['main']['humidity']))'''
        send_data=[city,json_data['weather'][0]['description'],json_data['main']['temp'],json_data['main']['pressure'],json_data['main']['humidity']]
        send_data=list(map(str,send_data))
        send_data='&'.join(send_data)
        print(send_data)
    except:
        print("error")
get_weather()
sys.stdout.flush()
