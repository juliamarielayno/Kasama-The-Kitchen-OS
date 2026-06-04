import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import google.generativeai as genai


if os.path.exists("filenametest1.csv"):
    df = pd.read_csv("filenametest1.csv")

else:
    df = pd.DataFrame(columns=['date', 'event', 'headcount', 'budget', 'cost', 'food'])

newrow = pd.DataFrame([{"date": "8/25/26",
                       "event": "GBM #1",
                       "headcount": 100,
                       "budget": 75,
                        "cost": 64.17,
                       "food": "taho cups"},
                      {"date": "9/1/26",
                       "event": "Mango Mixer",
                       "headcount": 60,
                       "budget": 75,
                        "cost": 45.74,
                       "food": "Mango Ice Candy"}])

df["cost"] = df["cost"].astype(float)


df = pd.concat([df, newrow], ignore_index= True)

df.to_csv("filenametest1.csv", index = False)

fig, ax = plt.subplots()

ax.set_title('Cost Per Event Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Cost ($)')

ax.plot(df['date'],df['cost'])
st.pyplot(fig)

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("your prompt here")

st.write(response.text)

