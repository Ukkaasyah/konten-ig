# Konten Instagram @mahad.aly.luqmanulhakim

Lembaga: **Ma'had Aly Luqmanul Hakim**. Di slide dan caption, cukup tulis "Ma'had Aly Luqmanul Hakim".
JANGAN tulis "disusun oleh Ukkaasyah Abdurrahman" di konten akun ini.

## Alur kerja
1. Pengguna memberi tema atau menyetujui usulan tema.
2. Buat carousel JPG 4:5 (1080×1350) plus caption. Kirim ke pengguna untuk dicek.
3. Setelah disetujui: commit gambar ke `mahad/posts/YYYY-MM-DD-slug/`, push ke `main`.
4. Jadwalkan lewat Metricool, brand Ma'had (blogId: BELUM ADA, akun belum disambungkan ke Metricool),
   zona waktu Asia/Jakarta, network `instagram`, type `POST`,
   media = `https://raw.githubusercontent.com/Ukkaasyah/konten-ig/main/mahad/posts/<slug>/<nn>.jpg`.
5. Jadwal: 1x sehari, selang-seling AQIDAH dan KAIDAH FIKIH. Jam tayang: BELUM DITENTUKAN.
6. Unggah ke Metricool sebagai draf dulu; jadikan terjadwal hanya setelah pengguna bilang oke.

## Aset
- `aset/logo.jpg`: logo Ma'had Aly Luqmanul Hakim (taruh kecil di pojok kiri bawah setiap slide, seperti contoh).
- `aset/qris-navy.jpg`: slide penutup donasi untuk seri AQIDAH.
- `aset/qris-gold.jpg`: slide penutup donasi untuk seri KAIDAH FIKIH.
- `contoh/`: contoh sampul dari pengguna (acuan gaya) dan fihris 36 kaidah Al-Muskah Al-Kautsariyah.
- Font: pakai `../fonts/` (Amiri untuk Arab, Lora untuk judul, Inter untuk isi).

## Gaya visual (dari contoh pengguna)
- Bingkai garis tipis emas ganda di tepi slide.
- Label kecil berspasi lebar di atas judul (mis. "KAJIAN AQIDAH", "KAIDAH FIKIH SYAFI'IYAH").
- Judul besar serif tebal huruf kapital, lalu sub-judul serif italic; garis pendek di bawahnya; satu kalimat hook.
- Teks Arab (kutipan inti) di kanan bawah sampul, nama ulama/kitab dengan huruf kapital berspasi; "GESER →" di kanan bawah.
- Warna:
  - Navy Ma'had #2A4B5C (sampul AQIDAH), teks krem, aksen emas.
  - Emas Ma'had #B08E4E (sampul KAIDAH FIKIH), judul navy, sub-judul krem.
  - Warna khusus hanya untuk sampul. JANGAN pakai hijau.

## Aturan umum (semua konten)
1. Bermanhaj salaf.
2. Rujukan: Al-Qur'an dan Sunnah.
3. Narasi untuk Instagram carousel.
4. Mudah dimengerti, terstruktur, bahasa yang baik. Harus terasa ditulis manusia, bukan "gaya AI".
5. Ukuran 4:5.
6. Selalu sertakan dalil dari Al-Qur'an atau hadits.
7. Sertakan pendapat ulama: teks Arab, arti, dan rujukan.
8. Rujukan diambil dari Turath (تراث) lewat konektor Turath.
9. Fokus: AQIDAH dan KAIDAH FIKIH.
10. Nukilan kitab: tampilkan halaman kitab (teks halaman dari Turath, dirender seperti halaman kitab, dengan nama kitab/juz/halaman),
    beri tanda stabilo pada bagian yang dinukil, lalu terjemahkan.
11. Judul: hook berbahasa ilmiah atau bergaya santri.
12. Slide terakhir SELALU berisi ajakan mendukung program lewat donasi QRIS (pakai `aset/qris-navy.jpg` atau `aset/qris-gold.jpg`).

## Aturan AQIDAH
- Selalu bawakan nukilan dari generasi salaf (3 abad pertama) dan ulama Syafi'iyah yang berakidah salaf / ashhabul hadits.
- Sertakan dalil naqli, dalil aqli, dan analogi.
- Rujukan yang bisa dipakai: Al-Mausu'ah Al-Muyassarah fil Adyan wal Madzahib (WAMY), Dirasat fil Ahwa' wal Firaq (Dr. Nashir Al-'Aql),
  Ibnu Taimiyah; untuk orientalisme: karya Dr. Musthafa As-Siba'i dan Dr. Musthafa Al-A'zhami.
- Warna sampul: navy #2A4B5C.

## Aturan KAIDAH FIKIH
- Fokus kaidah fikih Syafi'i: Al-Asybah wan Nazha'ir (As-Suyuthi), Al-Mantsur fil Qawa'id (Az-Zarkasyi), dan semisalnya.
  Urutan kaidah bisa mengikuti fihris Al-Muskah Al-Kautsariyah (`contoh/fihris-*`).
- Selalu sertakan: dalil, maksud kaidah, penerapan kaidah, pengecualian, dan syarat kaidah.
- Maksimal 10 slide (termasuk slide QRIS). Dalil cukup 1 slide. Penerapan kaidah minimal 5 kasus.
- Warna sampul: emas #B08E4E.
