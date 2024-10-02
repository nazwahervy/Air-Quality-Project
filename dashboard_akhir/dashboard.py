import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style for plots
sns.set(style='darkgrid')

# Load data
combined_df = pd.read_csv('all_data.xls')

# Convert date column to datetime
combined_df['date'] = pd.to_datetime(combined_df['date'])

# Sidebar for filters
st.sidebar.title("Filter Data")
# Date range filter
start_date, end_date = st.sidebar.date_input(
    "Pilih Rentang Waktu",
    value=[combined_df['date'].min(), combined_df['date'].max()],
    min_value=combined_df['date'].min(),
    max_value=combined_df['date'].max()
)
# Filter by location
locations = combined_df['Location'].unique()
selected_location = st.sidebar.multiselect('Pilih Lokasi', locations, default=locations)

# Filter by variable
variables = ['WSPM', 'TEMP']  # You can add more variables if needed
selected_variable = st.sidebar.selectbox('Pilih Variabel', options=variables)

# Apply filters to data
filtered_df = combined_df[(combined_df['date'] >= pd.Timestamp(start_date)) & 
                          (combined_df['date'] <= pd.Timestamp(end_date)) & 
                          (combined_df['Location'].isin(selected_location))]

# Main title
st.title('Dashboard Pemantauan Cuaca dan Kualitas Udara')

# Grafik 1: Perubahan Harian Variabel Terpilih (WSPM atau TEMP)
st.subheader(f'Perubahan Harian {selected_variable} di Setiap Stasiun Pemantauan')
daily_data = filtered_df.groupby(['date', 'Location'])[selected_variable].mean().unstack()
plt.figure(figsize=(12, 6))
daily_data.plot(ax=plt.gca())
plt.title(f'Perubahan Harian {selected_variable}')
plt.xlabel('Tanggal')
plt.ylabel(selected_variable)
plt.legend(title='Stasiun Pemantauan', loc='upper left')
st.pyplot(plt)

# Grafik 2: Korelasi antara Kecepatan Angin (WSPM) dan Suhu (TEMP)
if 'WSPM' in filtered_df.columns and 'TEMP' in filtered_df.columns:
    st.subheader('Korelasi antara Kecepatan Angin (WSPM) dan Suhu (TEMP)')
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=filtered_df, x='TEMP', y='WSPM', hue='Location')
    plt.title('Korelasi antara Kecepatan Angin dan Suhu')
    plt.xlabel('Suhu (°C)')
    plt.ylabel('Kecepatan Angin (WSPM)')
    st.pyplot(plt)

# Grafik 3: Boxplot Variabel Terpilih
st.subheader(f'Variasi Harian {selected_variable} di Setiap Stasiun Pemantauan')
plt.figure(figsize=(12, 6))
sns.boxplot(data=filtered_df, x='Location', y=selected_variable)
plt.title(f'Variasi Harian {selected_variable}')
plt.xlabel('Stasiun Pemantauan')
plt.ylabel(selected_variable)
plt.xticks(rotation=90)
st.pyplot(plt)