import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
from groq import Groq


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

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
if st.button("Question"):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Ask your question"}]
    )
    st.write(response.choices[0].message.content)
