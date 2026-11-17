# Konten Instagram @ukkaasyah.abdurrahman

> Repo ini juga dipakai untuk akun pondok @mahad.aly.luqmanulhakim. Aturannya terpisah di `mahad/CLAUDE.md`,
> dan aturan di file ini TIDAK berlaku untuk konten Ma'had.

Penyusun: Ukkaasyah Abdurrahman · Instagram: @ukkaasyah.abdurrahman

## Alur kerja
1. Pengguna memberi tema/bahan (atau menyetujui usulan tema).
2. Buat carousel JPG 4:5 (1080×1350), maksimal 10 slide, plus caption. Kirim ke pengguna untuk dicek.
3. Setelah disetujui: commit gambar ke folder `posts/YYYY-MM-DD-slug/` di repo ini, push ke `main`.
4. Jadwalkan lewat Metricool (blogId `8115480`, zona waktu Asia/Jakarta, network `instagram`, type `POST`),
   media = `https://raw.githubusercontent.com/Ukkaasyah/konten-ig/main/<path>.jpg` (urutan = urutan slide).
5. Jadwal: 1x sehari pukul 16.00 WIB, ganti tema tiap hari (selang-seling fikih Syafi'i dan tazkiyah/adab).
6. Sebelum terbit, unggah ke Metricool sebagai draf dulu; ubah jadi terjadwal hanya setelah pengguna bilang oke.
7. Pengguna ingin setiap postingan "sembunyikan jumlah suka". API Metricool/Instagram tidak menyediakan opsi ini, jadi pengguna menyalakannya manual di aplikasi Instagram setelah postingan terbit (titik tiga > Sembunyikan jumlah suka).

## Rencana: ajakan unduh aplikasi Haidku (BELUM aktif)
- Setelah pembayaran Mayar aktif (perkiraan pengguna: 18–19 Nov 2026), setiap carousel ditutup dengan slide ajakan mendapatkan aplikasi Haidku, "link ada di bio"; caption juga ditutup dengan ajakan yang sama.
- Slide ajakan dihitung dalam batas maksimal 10 slide.
- Jangan cantumkan harga di materi promosi.
- Jangan pasang sebelum pengguna mengonfirmasi Mayar sudah aktif.
- Template slide ajakan: `tools/haidku_cta.py OUT.jpg NO TOTAL` (warna merek Haidku, ungu-plum; diadaptasi dari poster promosi pengguna).

## Font
- Teks Arab: Amiri (file dari pengguna ada di `fonts/`, salin ke ~/.fonts lalu `fc-cache -f`).
- Judul Latin: Lora Bold (dipilih pengguna; `fonts/`); isi: Inter (sudah ada di sistem).
- Contoh skrip render (Playwright, 1080×1350, auto-fit): `tools/jamak_hujan_render.py`.

## Gaya bahasa (semua konten)
Harus terasa ditulis manusia, bukan "gaya AI". Hindari pola klise AI.

## Rules FIKIH (madzhab Syafi'i)
1. Bermanhaj salaf.
2. Rujukan: Al-Qur'an dan Sunnah.
3. Narasi untuk Instagram carousel.
4. Mudah dimengerti, terstruktur, bahasa yang baik.
5. Ukuran 4:5.
6. Selalu sertakan dalil Al-Qur'an atau hadits.
7. Sertakan pendapat ulama madzhab Syafi'i (teks Arab, arti, rujukan).
8. Rujukan dari Turath (تراث) lewat konektor Turath.
9. Fokus kitab: Ibnu Hajar Al-Haitami, Ar-Ramli, Zakariya Al-Anshari, Al-Khatib Asy-Syirbini, An-Nawawi, Ad-Damiri, Hasyiyah Al-Jamal, Hasyiyah Al-Bujairimi, dll.
10. Sertakan khilaf antara Ibnu Hajar, Ar-Ramli, Asy-Syirbini, Zakariya Al-Anshari, dan ashhabul hawasyi jika ada.
11–12. Nama & akun di atas.
13. Nukilan kitab: tampilkan halaman kitab (teks halaman dari Turath, dirender seperti halaman kitab, dengan nama kitab/juz/halaman) dan beri tanda stabilo pada bagian yang dinukil, lalu terjemahkan.
14. Judul: hook bergaya ilmiah atau gaya bahasa santri.
15. Warna sampul: selalu hijau tua (#1E3A2B).
16. Maksimal 10 slide.

## Rules TAZKIYAH / ADAB
1. Bermanhaj salaf.
2. Rujukan: Al-Qur'an dan Sunnah.
3. Narasi untuk Instagram carousel.
4. Mudah dimengerti, terstruktur, bahasa yang baik.
5. Ukuran 4:5.
6. Selalu sertakan dalil Al-Qur'an atau hadits.
7. Sertakan perkataan ulama ahlus sunnah (teks Arab, arti, rujukan).
8. Rujukan dari Turath (تراث).
9. Format JPG siap posting.
10. Maksimal 10 slide.
11. Warna sampul sesuai palet pengguna (hanya sampul). JANGAN pakai hijau untuk konten non-fikih.

## Palet warna (dari pengguna)
- Fikih Syafi'i — Hijau hutan #1E3A2B (sampul fikih)
- Tazkiyah / akhlak — Navy malam #1B2340 (sampul tazkiyah)
- Postingan selingan — Krem kertas #F3EBDD (juga latar slide isi)
- Aksen semua seri — Emas #D4A84B
