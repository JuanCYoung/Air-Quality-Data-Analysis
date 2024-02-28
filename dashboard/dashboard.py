import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#read dataset
data_df = pd.read_csv("dashboard/main_data.csv")

#Fungsi 
def max_pm25_2015(data_df):
    max_pm_2015 = data_df[data_df["year"] == 2015].groupby(by=["station"]).agg({
        "PM2.5" : "max"
    })
    
    return max_pm_2015

def perkembangan(data_df):
    tingkat_perkembangan = data_df[data_df["station"]=="Aotizhongxin"].groupby(by=["year"]).agg({
    "PM2.5":"mean",
    "PM10":"mean"
})
    return tingkat_perkembangan

data_max_pm_2150 = max_pm25_2015(data_df)
tingkat_perkembangan = perkembangan(data_df)


#Header
st.header('Air Quality Dashboard Dicoding :sparkles:')

#Tingkat PM2.5 tahun 2015
st.subheader('Highest and Lowest PM2.5 in 2015 China')

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
 
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="PM2.5",y="station", data=data_max_pm_2150.sort_values(by="PM2.5", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Tingkat PM2.5 Rate", fontsize=25)
ax[0].set_title("Station with Highest PM2.5", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)
 
sns.barplot(x="PM2.5",y="station", data=data_max_pm_2150.sort_values(by="PM2.5", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Tingkat PM2.5 Rate", fontsize=25)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Station with Lowest PM2.5", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)
 
st.pyplot(fig)

# Perkembangan Pm2.5 dan Pm10
st.subheader("The development of PM2.5 and PM10 each year.")
fig_pm2_5 = plt.figure(figsize=(10, 5))
plt.plot(
    tingkat_perkembangan.index,
    tingkat_perkembangan["PM2.5"],
    marker='o', 
    linewidth=2,
    color="#72BCD4"
)
plt.title("Graph Perkembangan PM2.5 (Tahun)", loc="center", fontsize=20)
plt.xlabel("Tahun", fontsize=12)  
plt.ylabel("Rata-rata PM2.5", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xticks(ticks=tingkat_perkembangan.index, labels=[str(int(year)) for year in tingkat_perkembangan.index], fontsize=10)

# Menampilkan plot PM2.5 di Streamlit
st.pyplot(fig_pm2_5)

fig_pm10 = plt.figure(figsize=(10, 5))
plt.plot(
    tingkat_perkembangan.index,
    tingkat_perkembangan["PM10"],
    marker='o', 
    linewidth=2,
    color="#72BCD4"
)
plt.title("Graph Perkembangan PM10 (Tahun)", loc="center", fontsize=20)
plt.xlabel("Tahun", fontsize=12)  
plt.ylabel("Rata-rata PM10", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xticks(ticks=tingkat_perkembangan.index, labels=[str(int(year)) for year in tingkat_perkembangan.index], fontsize=10)

# Menampilkan plot PM10 di Streamlit
st.pyplot(fig_pm10)


#Korelasi
st.subheader('Corelation Between NO2 dan SO2')

fig_corr = plt.figure(figsize=(10, 6))
for year in data_df['year'].unique():
    year_data = data_df[data_df['year'] == year]
    plt.scatter(year_data['NO2'], year_data['SO2'], label=year, alpha=0.5)

plt.xlabel('NO2')
plt.ylabel('SO2')
plt.title('Korelasi antara NO2 dan SO2')
plt.legend()

# Menampilkan plot korelasi di Streamlit
st.pyplot(fig_corr)

