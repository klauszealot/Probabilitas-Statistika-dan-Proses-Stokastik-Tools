# Alat Probabilitas, Statistika, dan Proses Stokastik

Aplikasi Desktop GUI komprehensif untuk menyelesaikan persoalan matematika dalam mata kuliah Probabilitas, Statistika, dan Proses Stokastik. Alat ini dibangun menggunakan **Python**, **Tkinter**, **SciPy**, dan **NumPy**.

## 🚀 Fitur Utama

- **Antarmuka Tab Intuitif:** Modul dikategorikan berdasarkan materi (Probabilitas, Distribusi, Sampling, Hipotesis, ANOVA).
- **Parameter Input Dinamis:** Masukkan variabel seperti $n, r, p, \mu, \sigma$ dengan mudah.
- **Eksekusi Instan:** Mendukung tombol "Enter" pada keyboard untuk konfirmasi kalkulasi cepat.
- **Layout Bento UI:** Tampilan bersih dan modern dengan baris input horizontal.
- **Penanganan Error yang Kuat:** Memvalidasi domain matematika, mencegah aplikasi tertutup paksa akibat pembagian nol atau input tidak valid.

## 📊 Rumus yang Diimplementasikan

### 1. Probabilitas & Kombinatorika
- Peluang Dasar: $P(A) = n/N$
- Aturan Penjumlahan (Saling Lepas & Umum)
- Peluang Bersyarat: $P(B|A)$
- Teorema Bayes (Analisis 2-Titik)
- Permutasi ($nP_r$) & Kombinasi ($nC_r$)
- Nilai Harapan $E(X)$ & Varians $\sigma^2$ (Variabel Acak Diskrit)

### 2. Distribusi Probabilitas
- Binomial: $b(x; n, p)$ (PMF, Rata-rata, Varians)
- Poisson: $p(x; \mu)$
- Fungsi Densitas Normal (PDF)
- Transformasi Z-Score: $Z = (X - \mu)/\sigma$

### 3. Distribusi Sampling
- Standar Error Rata-rata (Populasi Terbatas & Tak Terbatas)
- Standar Error Proporsi (Populasi Terbatas & Tak Terbatas)

### 4. Estimasi Parameter & Uji Hipotesis
- Selang Kepercayaan Rata-rata ($n \ge 30$ & $n < 30$)
- Estimasi Proporsi & Margin of Error
- Uji-Z & Uji-t Satu Sampel
- Uji-Z Dua Sampel (Beda Rata-rata)
- Uji-Z Satu Sampel & Dua Sampel untuk Proporsi

### 5. Analisis Varians (ANOVA)
- ANOVA Satu Arah (Kalkulasi Statistik-F)
- ANOVA Dua Arah (Statistik-F untuk Perlakuan & Blok)

## 💻 Cara Menjalankan

Anda dapat menjalankan aplikasi ini melalui dua cara:

### A. Menggunakan File Executable (.exe)
Jika Anda sudah memiliki file `.exe` hasil konversi:
1. Cari file bernama `Probabilitas, Statistika, dan Proses Stokastik Tools.exe`.
2. Klik dua kali pada file tersebut.
3. Tunggu beberapa saat hingga jendela aplikasi muncul (tidak memerlukan instalasi Python di komputer target).

### B. Menjalankan dari Kode Sumber (Python)
Pastikan Anda telah menginstal Python 3.10 ke atas.
1. Instal dependensi yang diperlukan:
   ```bash
   pip install scipy numpy
   ```
2. Clone repositori ini:
   ```bash
   git clone https://github.com/klauszealot/Probabilitas-Statistika-dan-Proses-Stokastik-Tools.git
   ```
3. Jalankan aplikasi:
   ```bash
   python main.py
   ```

## 📄 Lisensi
Proyek ini dibuat untuk tujuan edukasi. Silakan gunakan dan modifikasi untuk keperluan belajar!

---
*Dibuat oleh [klauszealot](https://github.com/klauszealot)*
