import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Judul Dashboard
st.title("Dashboard Peminjaman Sepeda")

# Load Data
#st.write("## 📅 Data Per Hari")
file_path_day = r"C:\Users\HP\Downloads\yanda\day.csv"
df_OriginalDay = pd.read_csv(file_path_day)
#st.dataframe(df_OriginalDay)

#st.write("## ⏳ Data Per Jam")
file_path_hour = r"C:\Users\HP\Downloads\yanda\hour.csv"
df_OriginalHour = pd.read_csv(file_path_hour)
#st.dataframe(df_OriginalHour)

#st.write("## 📌 Statistik Dasar")
#st.write(df_OriginalDay[['cnt', 'temp', 'hum', 'windspeed']].describe())

# Konversi tanggal ke format numerik untuk analisis tren
df_OriginalHour['dteday'] = pd.to_datetime(df_OriginalHour['dteday'])
df_OriginalHour['dteday_float'] = df_OriginalHour['dteday'].apply(lambda x: x.year + (x.day_of_year / (366 if x.is_leap_year else 365)))
df_numHour = df_OriginalHour.drop(columns=['dteday'])

df_OriginalDay['dteday'] = pd.to_datetime(df_OriginalDay['dteday'])
df_OriginalDay['dteday_float'] = df_OriginalDay['dteday'].apply(lambda x: x.year + (x.day_of_year / (366 if x.is_leap_year else 365)))
df_numDay = df_OriginalDay.drop(columns=['dteday'])

# Analisis Penyewaan Sepeda Berdasarkan Kondisi Cuaca
st.write("## 🌤️ Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
df_weather = df_numHour.groupby("weathersit")[['cnt', 'registered', 'casual']].mean()
weather_labels = {1: "Cerah/Sedikit Berawan", 2: "Berkabut + Berawan", 3: "Hujan Ringan/Petir", 4: "Hujan Deras/Salju Lebat"}
df_weather.index = df_weather.index.map(weather_labels)

fig, ax = plt.subplots(figsize=(10, 6))
df_weather.plot(kind="bar", colormap="Set2", ax=ax, rot=0, grid=True)
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
ax.set_xlabel("Kategori Cuaca")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.legend(["Total", "Casual", "Registered"])
ax.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig)

# Analisis Penyewaan Sepeda Berdasarkan Musim
st.write("## 🍂 Penyewaan Sepeda Berdasarkan Musim")
df_season = df_numDay.groupby("season")[['cnt', 'registered', 'casual']].mean().round()
season_labels = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
df_season.index = df_season.index.map(season_labels)
selected_seasons = st.multiselect("Pilih Musim:", df_season.index, default=df_season.index)
df_filtered_season = df_season.loc[selected_seasons]

fig, ax = plt.subplots(figsize=(10, 6))
df_filtered_season.plot(kind="bar", colormap="Set2", ax=ax, rot=0, grid=True)
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.legend(["Total", "Casual", "Registered"])
st.pyplot(fig)

# Analisis Penyewaan Sepeda Berdasarkan Hari dalam Seminggu
st.write("## 📊 Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
df_weekday = df_numDay.groupby("weekday")[['cnt', 'registered', 'casual']].mean().round()
days_labels = {0: "Minggu", 1: "Senin", 2: "Selasa", 3: "Rabu", 4: "Kamis", 5: "Jumat", 6: "Sabtu"}
df_weekday.index = df_weekday.index.map(days_labels)
df_weekday = df_weekday.loc[["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]]
selected_days = st.multiselect("Pilih Hari untuk Ditampilkan", df_weekday.index, default=df_weekday.index)
df_selected_days = df_weekday.loc[selected_days]

fig, ax = plt.subplots(figsize=(10, 6))
df_selected_days.plot(kind="bar", colormap="Set2", rot=0, grid=True, ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
ax.set_xlabel("Hari")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.legend(["Total", "Casual", "Registered"])
st.pyplot(fig)

# Analisis Penyewaan Sepeda Berdasarkan Jam
st.write("## ⏰ Penyewaan Sepeda Berdasarkan Jam")
df_hour = df_numHour.groupby("hr")[['cnt', 'registered', 'casual']].mean().round()

fig, ax = plt.subplots(figsize=(10, 6))
df_hour.plot(kind="bar", colormap="Set2", rot=0, grid=True, ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.legend(["Total", "Casual", "Registered"])
st.pyplot(fig)

# Analisis Penyewaan Sepeda Berdasarkan Hari Kerja vs Libur
st.write("## 🏢 vs 🎉 Penyewaan Sepeda pada Hari Kerja vs Libur")
df_working = df_numHour[df_numHour["workingday"] == 1].groupby("hr")[['cnt', 'registered', 'casual']].mean()
df_nonworking = df_numHour[df_numHour["workingday"] == 0].groupby("hr")[['cnt', 'registered', 'casual']].mean()

# Plot Hari Kerja
fig_work, ax_work = plt.subplots(figsize=(7, 6))
sns.lineplot(x=df_working.index, y=df_working["cnt"], label="Total", color="blue", marker="o", ax=ax_work)
sns.lineplot(x=df_working.index, y=df_working["registered"], label="Registered", color="green", marker="o", ax=ax_work)
sns.lineplot(x=df_working.index, y=df_working["casual"], label="Casual", color="red", marker="o", ax=ax_work)
ax_work.set_title("Hari Kerja")
ax_work.set_xlabel("Jam")
ax_work.set_ylabel("Penyewaan Sepeda")
ax_work.set_xticks(df_working.index)
ax_work.grid(True)
st.pyplot(fig_work)

# Plot Hari Libur
fig_nonwork, ax_nonwork = plt.subplots(figsize=(7, 6))
sns.lineplot(x=df_nonworking.index, y=df_nonworking["cnt"], label="Total", color="blue", marker="o", ax=ax_nonwork)
sns.lineplot(x=df_nonworking.index, y=df_nonworking["registered"], label="Registered", color="green", marker="o", ax=ax_nonwork)
sns.lineplot(x=df_nonworking.index, y=df_nonworking["casual"], label="Casual", color="red", marker="o", ax=ax_nonwork)
ax_nonwork.set_title("Hari Libur")
ax_nonwork.set_xlabel("Jam")
ax_nonwork.set_ylabel("Penyewaan Sepeda")
ax_nonwork.set_xticks(df_nonworking.index)
ax_nonwork.grid(True)
st.pyplot(fig_nonwork)
