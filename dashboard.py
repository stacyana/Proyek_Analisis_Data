import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('all_data.csv')

# Membuat dataframe untuk PM25_Station
PM25_Station = df.groupby('station')['PM25'].mean()

# Membuat dataframe untuk Temp_Station
Temp_Station = df.groupby('station')['TEMP'].mean()

# Membuat dataframe untuk Rain_station
Rain_station = df.groupby('station')['RAIN'].mean()

# Membuat dashboard
st.title('Dashboard Kualitas Udara')
st.header('Kriteria PM25_Station')
st.write('Stasiun mana yang memiliki rata-rata nilai pm2.5 tertinggi?')
stasiun_tertinggi_PM25 = PM25_Station.idxmax()
st.write(f'Stasiun {stasiun_tertinggi_PM25} memiliki rata-rata nilai pm2.5 tertinggi sebesar {PM25_Station.max()}')
st.bar_chart(PM25_Station)
st.write('kesimpulan pertanyaan pertama : stasiun mana yang memiliki rata-rata nilai pm2.5 tertinggi? dapat dilihat dari hasil visualisasi data bahwa stasiun yang memiliki rata-rata nilai PM2.5 tertinggi adalah Dongsi, dengan nilai sekitar 84.9 dibanding dengan Stasiun-stasiun lainnya memiliki nilai yang lebih rendah, dengan beberapa di antaranya berada di kisaran 70. oleh karna itu kulitas udara yang paling buruk di antara stasiun lainnya adalah stasiun Dongsi. Dan yang paling baik kualitas udara nya adalah stasiun Dingling yang memiliki nilai rata-rata PM2.5 paling rendah. hal ini sangat penting untuk diketahui, dikarenakan bahwa Konsentrasi partikel PM2.5 yang tinggi dalam udara dapat memiliki dampak buruk bagi kesehatan manusia. Paparan jangka panjang terhadap partikel PM2.5 dapat menyebabkan berbagai masalah kesehatan, termasuk gangguan pernapasan, iritasi mata, meningkatkan risiko penyakit jantung dan paru-paru, dan penyakit lainnya.Oleh karena itu, penting untuk memantau dan mengendalikan konsentrasi partikel PM2.5 dalam udara, terutama pada kondisi cuaca yang dapat meningkatkan konsentrasi tersebut, seperti saat suhu rendah.')

st.header('Kriteria Temp_Station')
st.write('Stasiun mana yang memiliki rata-rata temperatur suhu terendah?')
stasiun_terendah_Temp = Temp_Station.idxmin()
st.write(f'Stasiun {stasiun_terendah_Temp} memiliki rata-rata temperatur suhu terendah sebesar {Temp_Station.min()}')
st.bar_chart(Temp_Station)
st.write('kesimpulan pertanyaan ke dua : stasiun mana yang memiliki rata-rata temperatur suhu terendah? dari hasil visualisasi gambar menunjukan temperatur suhu pada tiap stasiun yang menunjukkan bahwa nilai rata-rata temperatur paling rendah berada di stasiun Huairou dengan rata-rata 12.24 celcius yang dimana ini berhbungan dengan kualitas PM2.5, dikarenakan Pada umumnya, pada suhu rendah, konsentrasi partikel PM2.5 dalam udara cenderung meningkat. Hal ini disebabkan oleh aktivitas pembakaran yang lebih intensif untuk pemanasan dan kegiatan lainnya pada saat suhu dingin. Selain itu, kondisi dispersi udara yang buruk pada suhu rendah juga dapat menyebabkan partikel PM2.5 lebih lama bertahan di udara dan tidak tersebar dengan baik, sehingga meningkatkan konsentrasinya.')

st.header('Kriteria Rain_station')
st.write('Stasiun mana yang paling sering mengalami hujan?')
stasiun_tertinggi_Rain = Rain_station.idxmax()
st.write(f'Stasiun {stasiun_tertinggi_Rain} memiliki rata-rata curah hujan tertinggi sebesar {Rain_station.max()}')
st.bar_chart(Rain_station)
st.write('kesimpulan pertanyaan ke tiga : statiun mana yang paling sering mengalami hujan? dari hasil visualisasi gambar dapat dismpulkan bahwa station yang paling sering mengalami hujan adalah stasiun wangliu dengan rata-rata 0.07 dengan nilai tertinggi dibandingkan dengan station lainnya.Hal ini menandakan daerah ini yang paling sering mengalami hujan dibandingkan dengan daerah-daerah stasiun lainya. hal ini juga berhubungan dengan kualitas PM2.5 pada suatu daerah dikarenakan dengan curah hujan yang tinggi dapat membantu meminimalisir konsentrasi partikel PM2.5 dalam udara. Curah hujan dapat berperan sebagai "pembersih" udara alami dengan mengikat partikel-partikel PM2.5 dalam udara dan membawanya ke tanah. Sehingga, ketika hujan turun, partikel-partikel tersebut akan terendapkan dan udara menjadi lebih bersih.')