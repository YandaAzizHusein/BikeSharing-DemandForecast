# Bike Sharing Dataset - README

## 1. Deskripsi Dataset
Bike Sharing Dataset adalah kumpulan data yang berisi informasi tentang penggunaan sistem penyewaan sepeda **Capital Bikeshare** di Washington, D.C. Data ini dikumpulkan selama tahun 2011 hingga 2012, mencatat jumlah sepeda yang disewa setiap jam dan setiap hari, serta faktor-faktor yang mempengaruhinya.

## 2. Struktur Dataset
Dataset ini terdiri dari beberapa file utama:

- **hour.csv**: Berisi data penyewaan sepeda per jam (**17.379 record**).
- **day.csv**: Berisi data penyewaan sepeda per hari (**731 record**).
- **Readme.txt**: Berisi deskripsi dan dokumentasi dataset.

Setiap file memiliki variabel utama berikut:

### **Variabel dalam Dataset**

#### **Informasi Waktu**
- `dteday` → Tanggal pencatatan data.
- `season` → Musim:
  - `1`: Musim Semi
  - `2`: Musim Panas
  - `3`: Musim Gugur
  - `4`: Musim Dingin
- `yr` → Tahun:
  - `0`: 2011
  - `1`: 2012
- `mnth` → Bulan (1-12).
- `hr` → Jam dalam sehari (0-23) **(hanya dalam hour.csv)**.
- `weekday` → Hari dalam seminggu (0: Minggu, 1: Senin, dst.).
- `workingday` → Hari kerja atau bukan:
  - `1`: Hari kerja
  - `0`: Akhir pekan/hari libur
- `holiday` → Status hari libur:
  - `1`: Hari libur
  - `0`: Bukan hari libur

#### **Kondisi Cuaca**
- `weathersit` → Kondisi cuaca:
  - `1`: Cerah, sedikit berawan
  - `2`: Berkabut, mendung
  - `3`: Hujan ringan/salju ringan
  - `4`: Hujan lebat/petir/salju lebat
- `temp` → Suhu yang dinormalisasi (dibagi 41 sebagai nilai maksimum).
- `atemp` → Suhu yang dirasakan (dibagi 50 sebagai nilai maksimum).
- `hum` → Kelembaban udara (dibagi 100 sebagai nilai maksimum).
- `windspeed` → Kecepatan angin (dibagi 67 sebagai nilai maksimum).

#### **Informasi Penyewaan Sepeda**
- `casual` → Jumlah penyewa yang bukan pelanggan tetap.
- `registered` → Jumlah penyewa yang merupakan pelanggan tetap.
- `cnt` → Total jumlah sepeda yang disewa (casual + registered).

## 3. Setup & Menjalankan Dashboard
a. Buat & Aktifkan Environment (Anaconda)
```
conda create --name bike-ds python=3.9
conda activate bike-ds
```
b. Install Dependencies
```
pip install -r requirements.txt
```
c. Menjalankan Dashboard
```
cd dashboard
streamlit run dashboard.py
```
d. Link Menuju dashbord pada cloud
[https://dashboard-capitalbikeshare-a319ybf503.streamlit.app/]

## 4. Struktur Direktori Proyek
Struktur direktori dalam proyek ini adalah sebagai berikut:

```
submission
├───dashboard
|   └───dashboard.py
├───data
|   ├───day.csv
|   ├───hour.csv
|   └───dan-lainnya.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt
```

- **dashboard/** → Folder ini berisi skrip dan data yang digunakan untuk membuat dashboard.
  - `main_data.csv` → Data yang digunakan dalam dashboard.
  - `dashboard.py` → Skrip Python untuk menjalankan dashboard.

- **data/** → Folder ini menyimpan dataset utama.
  - `day.csv` → Data penyewaan sepeda per hari.
  - `hour.csv` → Data penyewaan sepeda per jam.
  - `dan-lainnya.csv` → File tambahan lainnya yang digunakan dalam analisis.

- `notebook.ipynb` → Notebook Jupyter yang berisi eksplorasi dan analisis data.

- `README.md` → Dokumentasi proyek yang menjelaskan dataset, analisis, dan cara menjalankan proyek.

- `requirements.txt` → Daftar dependensi atau pustaka Python yang diperlukan untuk menjalankan proyek.

- `url.txt` → File teks yang kemungkinan berisi sumber atau tautan terkait proyek.

## 5. Sumber Data
- **Data Penyewaan Sepeda**: [Capital Bikeshare](http://capitalbikeshare.com/system-data)

## 6. Lisensi
> Fanaee-T, Hadi, and Gama, Joao, "Event labeling combining ensemble detectors and background knowledge", Progress in Artificial Intelligence (2013), Springer Berlin Heidelberg.

