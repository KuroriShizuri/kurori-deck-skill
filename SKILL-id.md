---
name: rajen-deck-skill
version: 1.0.0
description: |
  Membangun deck proposal bisnis yang didukung analisis data, dengan cara
  yang dipakai pada Final Assignment GCI World 2026: draf bahasa Indonesia
  dulu, lalu humanizer, angka diverifikasi terhadap notebook yang dieksekusi,
  satu file HTML per slide, dan render PDF dengan pipeline yang bisa
  diulang. Maksimal 15 slide; setiap angka membawa sitasi di slide tempat
  angka itu muncul.
license: MIT
compatibility: claude-code codex muse opencode
---

# Rajen Deck Skill

Membangun deck proposal bisnis yang singkat dari analisis data, dengan
sumber untuk setiap angka. Skill ini merekam cara kerja yang dipakai pada
Final Assignment GCI World 2026 (churn telekomunikasi Company A, November
2026): deck PDF 15 slide berbahasa Inggris, dibangun dari draf Indonesia.
Setiap angka dicek ke notebook analisis yang dieksekusi dan membawa sitasi
di slide tempat angka itu muncul. Paket yang sudah jadi diserahkan ke
penulisnya; file PDF deck itu sendiri tidak disertakan di sini. Yang
disertakan adalah metodenya, aturannya, toolchain-nya, dan teks deck
sebagai contoh kerja (`examples/`).

## Kapan dipakai

Pakai skill ini saat user meminta deck presentasi yang argumentasinya
harus didukung data: tugas akhir mata kuliah, proposal churn atau
retensi, atau deck eksekutif apa pun yang rekomendasinya didukung model.
Cocok saat deck harus pendek (maksimal 15 slide), setiap angka harus
membawa sumber, dan teksnya tidak boleh terbaca seperti keluaran AI yang
generik.

## Kapan tidak dipakai

Jangan pakai untuk deck kreatif bebas, set slide kuliah, atau deck yang
tidak didukung data. Langkah verifikasi di skill ini mengasumsikan ada
notebook analisis (atau padanannya) yang menghasilkan angka-angka di
slide. Kalau tidak ada notebook atau output analisis padanannya, langkah
angka tidak berlaku. Lewati Langkah 3 dan cek notebook di Langkah 8,
jalankan langkah sisanya, dan katakan terus terang bahwa angkanya tidak
terverifikasi terhadap analisis yang dieksekusi.

## Aturan keras

Aturan-aturan ini tidak boleh dilanggar. Deck aslinya lolos cek build dan
cek angka (Langkah 8 dan 9) karena mengikuti aturan ini.

1. **Maksimal 15 slide, termasuk slide judul dan slide referensi.**
   Hitung semua slide. Pada tugas GCI, penilai mengabaikan slide yang
   melewati batas, jadi slide tambahan sama saja dengan tidak ada.
   Pastikan batas dan konsekuensinya untuk setiap tugas baru (Langkah 1).
2. **Minimal satu model ML atau statistik, dengan nama, metrik evaluasi,
   dan skor ditulis eksplisit di teks slide.** Grafik saja tidak cukup.
   Bandingkan beberapa model kalau bisa.
3. **Kutipan langsung di bawah 40% dari teks deck, sebagai patokan.**
   Tulis argumen dengan kalimat sendiri.
4. **Setiap angka di slide membawa sumbernya di slide yang sama.**
   Footnote kecil (minimal 13 px) berisi organisasi, judul dokumen, dan
   tanggal. Tidak ada angka tanpa sumber, tanpa pengecualian.
5. **Data pasar dipakai hanya setelah sumbernya terbukti bisa dibuka dan
   dicari.** Buka sendiri halamannya dan temukan angkanya di halaman itu
   sebelum angka itu masuk slide. Kalau sumbernya tidak bisa dibuka,
   jangan pakai angkanya.
6. **Skor model harus cocok dengan notebook yang dieksekusi.** Notebook
   yang dieksekusi dan diserahkan adalah otoritasnya, bukan run lokal dan
   bukan teks tutorial. Lihat `references/number-verification.md`.
7. **Transkrip chat AI tidak pernah dipublikasikan.** Kalau tugas meminta
   pengungkapan pemakaian AI, cantumkan URL sesinya saja. Jangan pernah
   melampirkan atau menempel transkrip. Kasus GCI mencantumkan URL sesi
   Kiro, yang hanya bisa dibuka setelah login dan tidak membuat transkrip
   menjadi publik.
8. **Tanpa em-dash dan tanpa en-dash di teks slide, tanpa emoji, tanpa
   gaya penulisan AI.** Checker menolak kedua dash di mana saja, jadi
   tulis rentang angka seperti 270-300 dengan tanda hubung biasa. Kata
   yang dilarang: delve, furthermore, moreover, leverage, leveraging,
   cutting-edge, robust, seamless, pivotal, utilize, dan gradient. Nama
   model dikecualikan dari larangan kata: larangan itu menyangkut gaya
   bahasa, bukan nama model seperti Gradient Boosting. Jangan pakai tanda
   hubung berspasi sebagai dash. Lihat `references/humanizer-rules.md`.
9. **Angka tidak pernah dikarang, dibulatkan menjadi klaim baru, atau
   disalin dari ingatan.** Kalau angka tidak ada di lembar angka
   terverifikasi (bagian `SHEET` di `check_numbers_final.py`, lihat
   Langkah 8), angka itu tidak masuk slide. Di draf, tulis TBD atau buang
   klaimnya, jangan ditebak. Tidak boleh ada TBD tersisa di deck yang
   diserahkan.
10. **Slide terakhir adalah daftar referensi lengkap dengan URL.** Daftar
    yang sama ditempel ke kolom References di platform pengumpulan, tanpa
    diubah.

## Alur kerja

### Langkah 1. Baca aturan tugas dari dokumen resminya

Baca langsung README dan file tutorial tugasnya, dari disk. Jangan
mengandalkan ringkasan browser atau jawaban chat soal format. Kasus GCI
menunjukkan alasannya: laporan browser awal mengarang syarat 16:9, latar
putih, presentasi kelompok, dan deadline Google Classroom. Semuanya tidak
ada di dokumen resmi. (Deck final tetap memakai kanvas 16:9 dan latar
putih, sebagai pilihan desain, bukan sebagai syarat.) Aturan yang benar:
PDF, maksimal 15 slide, pengumpulan lewat Omnicampus, deadline 28
November 2026 11:30 UTC, nama file `[AccountName].pdf` dan
`[AccountName].ipynb`. Untuk tugas yang baru, pastikan aturan yang benar
sebelum menulis apa pun. Catat aturan itu di file aturan baru yang
diformat seperti `references/deck-rules.md`, dan lakukan sebelum build
dimulai.

### Langkah 2. Rencanakan deck sebelum analisis selesai, tapi jangan kunci judul slide dulu

Buat rencana 15 slide yang mencakup hook, problem, insight, solution,
cost, conclusions, dan references. Rencana GCI, slide per slide, ada di
`references/deck-rules.md`. Kalau deck yang baru butuh slide lebih
sedikit, angka 15 adalah batas atas, bukan target. Beri tiap slide satu
gagasan dan tiap slide hasil satu exhibit. Judul proposal tetap hipotesis
kerja sampai analisis menghasilkan angka.

### Langkah 3. Jalankan analisis, lalu tulis judul slide dari angkanya

Judul adalah kalimat kesimpulan lengkap yang membawa angka, maksimal dua
baris. Contoh dari contoh kerja: "Churn jumps from 37.4% for handsets
aged 270-300 days to 60.3% for handsets aged 300-330 days, a gap of 22.9
percentage points." Jangan pernah menulis judul sebelum angka yang
mendasarinya ada. Masukkan setiap angka yang dipakai di judul ke lembar
angka terverifikasi, termasuk angka turunan seperti selisih 22,9 poin.

Bandingkan model pada split train/test yang sama dan laporkan akurasi,
AUC, precision, dan recall. Cantumkan margin of error di samping skor
jika split-nya cukup besar untuk dihitung. Uji feature engineering dan
laporkan hasilnya walaupun tidak membantu. Pada kasus GCI feature
engineering tidak membantu (akurasi cross-validasi 0,6224 dengan fitur
baru melawan 0,6239 tanpa fitur baru), jadi fiturnya dibuang dan hal itu
dinyatakan di slide.

### Langkah 4. Tetapkan framing pasar dan kalimat batasnya

Bila perusahaan dalam kasus bersifat anonim, katakan di slide, dan
katakan pasar nyata mana yang dipakai hanya sebagai acuan. Tulis kalimat
batas lebih awal dan ulangi di tempat pembaca bisa salah mengira pasar
acuan sebagai perusahaan itu sendiri. Contoh: "Company A is anonymous.
Indonesia is only a reference market, and the model results are not
claimed to represent Indonesian customers." Verifikasi tiap sumber pasar
dengan membukanya sendiri (aturan 5 di atas) sebelum angka pasar masuk
deck.

### Langkah 5. Tulis draf teks deck dalam bahasa Indonesia dulu

Tulis seluruh teks slide dalam bahasa Indonesia (`content-id.md` pada
contoh kerja). Satu bagian per slide: Title, Composition, Exhibit,
Content, Footnote. File `examples/content-id.md` menunjukkan format tiap
bagian. Tulis angka dengan notasi yang diharapkan
`scripts/check_numbers_final.py`, supaya angka Indonesia dan Inggris
cocok persis. Jaga urutan slide tetap identik di kedua bahasa.

### Langkah 6. Jalankan humanizer bahasa Indonesia

Terapkan aturan `humanizer-indonesia` pada draf Indonesia. Pakai skill
yang sudah terpasang jika tersedia. Ringkasan aturannya ada di
`references/humanizer-rules.md`. Pass ini membuang tanda-tanda AI dan
bahasa terjemahan (kalke, yaitu calque) tanpa mengubah angka, sitasi,
atau rujukan silang apa pun. Jalankan skrip metrik skill itu jika
tersedia, dan perbaiki yang ditandai. Pengukuran draf Indonesia pada kasus GCI: rerata panjang kalimat
14,4 kata, simpangan baku 8,8, 0 em/en dash. Humanizer menghasilkan draf untuk disunting manusia, jadi sunting
hasilnya dengan tangan setelahnya.

### Langkah 7. Terjemahkan ke Inggris, lalu jalankan humanizer Inggris

Terjemahkan draf Indonesia ke Inggris (`content-en.md`). Lalu terapkan
aturan `academic-humanizer` hanya pada prosa Inggris. Pakai skill yang
sudah terpasang jika tersedia. Jangan pernah menerapkan humanizer pada
judul, angka, nama model, sitasi, atau rumus. Judul adalah kalimat
lengkap yang membawa angka, jadi tulis ulang judul yang lemah dengan
tangan, jangan jalankan lewat humanizer.

Dua pelajaran dari build GCI, keduanya ditemukan lewat review independen:

- Pertahankan hedge epistemik seperti "to the best of our knowledge"
  saat kalimat membuat klaim kebaruan.
- Jangan biarkan perbaikan gaya mengubah besaran samar menjadi klaim
  spesifik yang eksklusif. Perbaikan yang menyebut setting tertentu
  ("only on ...") adalah klaim empiris baru. Cek ke tabel hasil sebelum
  mempertahankannya.

Lihat `references/humanizer-rules.md`.

### Langkah 8. Verifikasi semua angka dengan checker

Salin `scripts/check_numbers_final.py` ke root proyek deck. Ganti lembar
terverifikasinya (bagian `SHEET`) dengan angka deck yang baru, yang
diambil dari notebook yang dieksekusi. Jalankan. Checker memeriksa tiga
hal:

1. Angka identik antara teks Indonesia dan Inggris, slide per slide.
2. Setiap angka ada di lembar terverifikasi, sebagai nilai, nilai kali
   100, atau nilai bagi 100.
3. Larangan gaya berlaku: tanpa angka yang dilarang (seperti yang
   didefinisikan di skrip), tanpa em/en dash, tanpa emoji, tanpa kata
   yang dilarang, tanpa tanda hubung berspasi.

Hasilnya harus nol masalah.

Lalu jalankan pengecekan notebook lawan deck dengan
`scripts/check_notebook_vs_deck.py` (sesuaikan path dan daftar `CHECKS`
dengan deck yang baru; versi GCI adalah contoh kerja). Pada build GCI
hasilnya 51 PASS dan 9 FAIL. Setelah ditinjau, kesembilan FAIL masuk
kategori yang dinilai tidak bermasalah: nilai yang hanya ada di notebook,
selisih aritmetika turunan, dan nilai rank yang memang ditampilkan
sebagai rank. Lihat `references/number-verification.md`.

### Langkah 9. Build deck

Tulis satu file HTML mandiri per slide, ditambah `deck.css` dan
`deck.json` (manifest yang menentukan urutan slide). Lalu jalankan
pipeline:

1. Buat grafik dari angka terverifikasi dengan Python dan matplotlib.
   `scripts/build_charts_v2.py` adalah contoh kerja.
2. Tanam font dan inline gambar dengan `scripts/build_deck.py`.
3. Gabungkan slide dengan `scripts/assemble_deck.mjs` (jalankan dengan
   Bun).
4. Render ke PDF dan audit dengan `scripts/render_audit.mjs` (Playwright
   dengan headless Chromium; jalankan dengan `--gate`).
5. Validasi dengan `scripts/validate_pdf.sh`.

Lalu cek PDF:

- Jalankan `pdfinfo`. Untuk deck GCI: 15 halaman (maksimal 15 secara
  umum) pada 960 kali 540 pt. Ukuran ini sama dengan kanvas 1280 kali
  720 px pada 96 px per inci.
- Jalankan `pdffonts`. Setiap font yang terdaftar harus Source Sans 3
  (Regular atau Bold) dan menunjukkan `yes` di kolom `emb`.
- Baca setiap PNG hasil render (di `.src/validate/`). Cari overflow,
  angka yang berbeda dari teks Inggris, dan slide data yang kehilangan
  footnote sumber.

Argumen perintah, pipeline lengkap, dan gate-nya ada di
`references/toolchain.md`.

### Langkah 10. Serahkan paketnya

Serahkan PDF, notebook, dan daftar referensi lewat platform mata kuliah.
Daftar referensi di slide terakhir dan daftar yang ditempel ke kolom
References platform harus daftar yang sama. Kalau tugas meminta
pengungkapan pemakaian AI, daftar itu memuat URL sesi AI. Jangan pernah
melampirkan transkrip chat AI. Ganti nama `deck.pdf` mengikuti aturan
nama file platform. Pada kasus GCI filenya adalah `[AccountName].pdf`
dan `[AccountName].ipynb`, dengan nama akun Rajendriya.

## Tata letak file proyek deck

```
deck/
  content-id.md            draf Indonesia, satu bagian per slide
  content-en.md            teks Inggris final, urutan slide sama
  check_numbers_final.py   checker angka dan gaya (sesuaikan SHEET)
  .src/
    slides/                satu HTML per slide, deck.css, deck.json
    media/                 grafik (PNG), foto, font, build_charts_v2.py
    index.html             dokumen gabungan (dihasilkan)
    validate/              PNG per halaman dari PDF final (dihasilkan)
  deck.pdf                 output akhir
```

## Design token

- Navy `#14467C` adalah warna struktur.
- Putih adalah latar.
- Emas lembut `#E8B84A` adalah satu-satunya aksen.
- Slate teal `#2F6F6E` adalah warna sekunder yang dipakai hemat. Pakai
  hanya jika box memang perlu. Jangan pernah memakai teks teal di atas
  latar navy.
- Font: hanya Source Sans 3, Regular dan Bold.
- Kanvas: 1280 kali 720 px.
- Ukuran minimum: teks isi 20 px, tabel 18 px, sitasi 13 px.
- Foto diwarnai ulang menjadi duotone navy. Cover memakai tab duotone
  kecil, bukan foto full-bleed.

Token lengkap, angka kontras, delapan aturan aksen, dan daftar periksa
untuk menghindari tampilan generik ada di `references/design-tokens.md`.

## Dependensi

- `academic-humanizer` (humanizer Inggris; MIT; AIScientists-Dev;
  v0.3.3): enam layer, audit dulu baru tulis ulang, angka dan sitasi
  dipertahankan, tidak pernah mengarang bukti. Sumber:
  https://github.com/AIScientists-Dev/academic-humanizer. Ringkasannya di
  `references/humanizer-rules.md`.
- `humanizer-indonesia` (humanizer Indonesia; v1.7.2): draf, audit, lalu
  revisi akhir. Membuang tanda AI dan bahasa terjemahan. Ringkasannya di
  `references/humanizer-rules.md`.
- Panduan presentasi dari skill `documents` (satu file HTML per slide,
  ditambah `deck.css` dan `deck.json`, dirakit dengan cara yang sama setiap
  kali): pola tata letak yang diikuti skill ini.
- Skrip di `scripts/`: `assemble_deck.mjs`, `render_audit.mjs`,
  `validate_pdf.sh`, `build_charts_v2.py`, `check_numbers_final.py`,
  `check_notebook_vs_deck.py`, `build_deck.py`. Lihat
  `references/toolchain.md` untuk peran tiap skrip dan asalnya.
- Tool yang dibutuhkan perintah Langkah 9: Python dengan matplotlib,
  Bun, Playwright dengan headless Chromium, `pdfinfo` dan `pdffonts`
  (dari poppler-utils), dan file font Source Sans 3. Versinya tidak
  dicatat di skill ini.

## Roadmap: BELUM diadopsi, bukan bagian dari skill ini

Framework pitch deck seperti H-P-S-I-T-C, SCR Framework, Pyramid
Principle, One slide One message, metode BLUF, Data Slide Formula,
pendekatan Storyboard, dan tes "So what?" dicatat di
`references/roadmap.md` sebagai kandidat perbaikan berikutnya. Framework
itu BELUM diadopsi di sini. Jangan ajarkan sebagai aturan skill ini
sampai penulis skill dan orang yang memakai skill melakukan brainstorming
dan mengadopsinya di versi baru.

## File referensi

| File | Isinya |
|---|---|
| `references/deck-rules.md` | Aturan tugas dan rencana 15 slide |
| `references/number-verification.md` | Disiplin angka, checker, kasus nyata |
| `references/design-tokens.md` | Warna, font, ukuran, aturan foto dan aksen |
| `references/toolchain.md` | Pipeline build, skrip, gate, batas PPTX |
| `references/humanizer-rules.md` | Kedua skill humanizer, ringkas, dengan peringatan |
| `references/worked-example.md` | Deck churn Company A, angka dan peta slide |
| `references/roadmap.md` | Framework pitch deck yang dipertimbangkan, belum diadopsi |
| `examples/content-en.md` | Teks deck Inggris final (contoh kerja) |
| `examples/content-id.md` | Teks draf Indonesia (contoh kerja) |
| `scripts/` | Skrip toolchain, disalin apa adanya |
