import streamlit as st
import json
import requests
import matplotlib.pyplot as plt



st.title("Weather app 🌤️")
st.subheader('Enter a city name to see the current weather or forecast')

api_key='76686c1d03fd400780a100945251503'


option = st.radio('Choose an option', ['Current Weather', 'Forecast'])



if option == "Current Weather":
    city = st.text_input('Enter the city name:')
    if st.button("Display"):
        p = {
            'appid': api_key,
            'q': city

        }

        base_url = f'http://api.weatherapi.com/v1/current.json?key=76686c1d03fd400780a100945251503&q={city}&aqi=no'
        # print(base_url)

        response = requests.get(base_url, params=p)

        data = response.json()
        # st.write(data)
        var = data['current']['condition']['icon']
        var = "https:" + var
        st.image(var, width=100)

        st.subheader(f'☁️The weather info of {city}☁️ :')
        st.subheader(f'⏲️The date and time is, {data['location']['localtime']}⏲️')
        st.write(f"🌡️Temp in celcius: {data['current']['temp_c']}C🌡️")
        st.write(f"🌡️Temp in farenheit: {data['current']['temp_f']}F🌡️")
        st.write(f"💧Humdity: {data['current']['humidity']}💧")
        st.write(f'The weather feels like {data["current"]["condition"]["text"]}')
        st.write(f'🍃The wind speed is {data["current"]["wind_kph"]} kph🍃')
        st.write(f'☁️The U.V index is {data["current"]["uv"]}☁️')

    else:
        print("Pls Enter A City!!")
        st.warning('please enter a valid city name')
if option == "Forecast":
    city = st.text_input('Enter the city name:')
    days = st.number_input('Enter the no. of days:', min_value = 0)
    base_url = f"http://api.weatherapi.com/v1/forecast.json?key=39fcd22d8dfe4504bdd124819241109&q={city}&days={days}&a"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()

        days = data['forecast']['forecastday']
        t = days[0]['hour']
        time_list = []
        temp_list = []
        for i in t:
            # print(i)
            time_list.append(i['time'])
            temp_list.append(i['temp_c'])
        fig = plt.figure(figsize=(10, 5))
        plt.plot( time_list, temp_list, marker='o')
        plt.xticks(rotation=90)
        plt.grid()
        plt.xlabel('Time')
        plt.ylabel('Temperature')
        plt.title(f'Temperature forecast for city {city}')
        if st.button('Display'):
            st.pyplot(fig)

