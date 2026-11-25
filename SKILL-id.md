---
name: kurori-deck-skill
version: 2.0.0
description: |
  Membangun deck proposal bisnis yang didukung analisis data, dengan cara
  yang dipakai pada deck contoh kerja: memilih metode lewat router, draf
  bahasa Indonesia dulu, lalu humanizer, angka diverifikasi terhadap
  notebook yang dieksekusi, satu file HTML per slide, dan render PDF dengan
  pipeline yang bisa diulang. Sweet spot 15 slide; setiap angka membawa
  sitasi di slide tempat angka itu muncul. Termasuk mode case-competition
  untuk deck yang dinilai dingin, tanpa presenter.
license: MIT
compatibility: claude-code codex muse opencode
---

# Kurori Deck Skill

Membangun deck proposal bisnis yang singkat dari analisis data, dengan
sumber untuk setiap angka. Skill ini merekam cara kerja yang dipakai pada
deck contoh kerja: deck churn telekomunikasi Company A (November 2026,
15 slide, berbahasa Inggris, dibangun dari draf Indonesia) dan deck
case-competition MieLestari (November 2026, 43 slide, berbahasa Indonesia,
dinilai 9 untuk kelayakan menang oleh reviewer eksternal). Setiap angka
dicek ke analisis yang dieksekusi dan membawa sitasi di slide tempat angka
itu muncul. Paket yang sudah jadi diserahkan ke penulisnya; file PDF deck
itu sendiri tidak disertakan di sini. Yang disertakan adalah metodenya,
aturannya, toolchain-nya, dan teks deck sebagai contoh kerja
(`examples/`, `references/worked-example.md`,
`references/case-competition-mode.md`).

## Yang berubah di v2.0.0

Versi 1 merekam satu alur kerja tetap untuk satu tugas. Versi 2 menambah
apa yang dibuktikan tiga program uji setelah v1 rilis:

- **Router metode.** Sembilan metode (4 alur, 5 lapisan pendukung),
  diranking per brief pada lima dimensi, dengan walk-down saat user
  menolak pilihan teratas. Lihat "Router metode".
- **Jumlah slide sebagai sweet spot.** Angka 15 adalah target, bukan
  floor keras dan bukan cap universal. Cap 15 hanya berlaku bila tugas
  membatasinya. Deck utama case-competition berisi 10-12 slide ditambah
  appendix yang tidak dihitung. Lihat "Jumlah slide".
- **Pustaka palet.** 51 palet bernama di `references/palette-library.md`
  dengan pemilih visual (`references/palette-picker-2026-11-24.html`).
  Agent menalar palet dari data, audiens, dan konteks, lalu mengusulkan
  3-4 opsi dengan satu baris alasan per opsi. User mengunci satu. Lihat
  "Palet".
- **Alur kerja 15 langkah dengan Spesifikasi Beku.** Brief dikonvergensikan
  dulu (gate langkah 7), keputusan dibekukan jadi Spesifikasi Beku
  (langkah 10), build menyusul, dan loop validasi-refine punya aturan
  berhenti. Humanizer adalah item checklist di langkah 11, bukan ingatan.
  Lihat "Alur kerja".
- **Mode Case-Competition.** Mode dua lapis untuk deck yang dinilai dingin,
  tanpa presenter: deck utama narasi 10-12 slide ditambah appendix padat,
  satu analisis per slide. Spesifikasi lengkap di
  `references/case-competition-mode.md`.
- **Aturan desain.** 19 aturan visual empiris dari uji Company A
  (aturan 1-14), reel "10 Niche Design Hacks" (aturan 15-18), dan uji
  MieLestari (aturan 19), termasuk aturan simetri. Lihat "Aturan desain".
- **Disiplin verifikasi.** File angka kanonik sebagai satu-satunya sumber
  kebenaran, satu checker per versi, dan halaman hasil render dibaca
  dengan mata, bukan hanya dicek overflow. Lihat "Disiplin verifikasi".

Metode v1 tetap utuh di dalam alur kerja v2: sepuluh aturan keras tetap
berlaku (aturan 1 direvisi seperti di atas), draf Indonesia dulu dengan
dua pass humanizer tetap menjadi pipeline bahasa, dan checker angka tetap
harus melaporkan nol masalah sebelum build. Tidak ada yang dihapus dari
v1; v2 menambah pilihan dan satu mode kedua di sekelilingnya. Catatan
lengkap ada di `CHANGELOG.md`.

## Kapan dipakai

Pakai skill ini saat user meminta deck presentasi yang argumentasinya
harus didukung data: tugas akhir mata kuliah, proposal churn atau
retensi, pitch deck, entri case-competition, atau deck eksekutif apa pun
yang rekomendasinya didukung model. Cocok saat deck harus padat, setiap
angka harus membawa sumber, dan teksnya tidak boleh terbaca seperti
keluaran AI yang generik.

Bila deck akan dinilai dingin, tanpa presenter (business case, case
competition, atau deck apa pun yang diserahkan sebagai dokumen), pakai
Mode Case-Competition. Bila user menyebut pitch deck, router memilih
H-P-S-I-T-C lebih dulu.

## Kapan tidak dipakai

Jangan pakai untuk deck kreatif bebas, set slide kuliah, atau deck yang
tidak didukung data. Langkah verifikasi di skill ini mengasumsikan ada
notebook analisis (atau padanannya) yang menghasilkan angka-angka di
slide. Kalau tidak ada notebook atau output analisis padanannya, langkah
angka tidak berlaku. Lewati cek notebook di alur kerja, jalankan langkah
sisanya, dan katakan terus terang bahwa angkanya tidak terverifikasi
terhadap analisis yang dieksekusi.

## Aturan keras

Aturan-aturan ini tidak boleh dilanggar. Deck aslinya lolos cek build dan
cek angka karena mengikuti aturan ini, dan deck MieLestari mempertahankan
skor 9 karena mengikuti aturan ini juga.

1. **Jumlah slide mengikuti tugas; 15 adalah sweet spot, bukan floor
   keras.** Pastikan batas yang benar untuk setiap tugas baru (Alur
   kerja langkah 1). Bila tugas membatasi deck sampai 15 slide, angka 15
   adalah cap keras dan semua slide dihitung, termasuk judul dan
   referensi. Bila tugas tidak membatasi, targetkan 15 dan serahkan ke
   agent untuk memutuskan lebih banyak atau lebih sedikit dari temuan;
   gate "so what?" dan one-slide-one-message yang membatasi
   pembengkakan, bukan angka. Di Mode Case-Competition, deck utama berisi
   10-12 slide dan appendix tidak dihitung.
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
   melampirkan atau menempel transkrip. Contoh kerja mencantumkan URL sesi
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
   terverifikasi (bagian `SHEET` di `check_numbers_final.py`, lihat Alur
   kerja langkah 12), angka itu tidak masuk slide. Di draf, tulis TBD
   atau buang klaimnya, jangan ditebak. Tidak boleh ada TBD tersisa di
   deck yang diserahkan.
10. **Slide terakhir adalah daftar referensi lengkap dengan URL.** Daftar
    yang sama ditempel ke kolom References di platform pengumpulan, tanpa
    diubah.

## Router metode

Jangan memilih metode karena kebiasaan. Routing per brief.

### Mekanisme

1. **User tidak memberi prompt metode.** Agent menalar dari konteks,
   tujuan, dan data, meranking kesembilan metode, menampilkan daftar
   peringkat dengan satu baris alasan per metode, dan membangun di atas
   #1.
2. **User memberi metode.** Ikuti, dan sampaikan di brief kenapa metode
   lain bisa lebih bagus. Saran saja, kecuali metode itu bertabrakan
   dengan batas keras (jumlah slide, tujuan deck, atau aturan skill);
   kalau begitu, tandai sebagai KONFLIK dan tanyakan sebelum membangun.
3. **Walk-down.** User menolak #1, agent pindah ke #2, lalu #3, sampai
   daftar habis. Kalau habis, dengarkan ulang: user mau seperti apa,
   dari referensi atau imajinasinya.

### Lima dimensi ranking

Ranking memakai lima dimensi ini saja. Jangan tambah dimensi keenam.
Preferensi user sebelumnya bukan dimensi terpisah; catat sebagai bukti
pendukung di dimensi 1 (kesesuaian tujuan) dan dimensi 5 (kesesuaian
style). Dimensi terpisah akan menghitung ganda dan mengunci kebiasaan,
padahal user bisa mau alur berbeda untuk jenis deck berbeda.

1. **Kesesuaian tujuan.** Menginformasikan, membujuk, memutuskan, atau
   melaporkan.
2. **Kesesuaian audiens.** Eksekutif mau kesimpulan dulu; investor mau
   cerita; akademisi mau metode dulu.
3. **Ketersediaan data.** Alur data-story butuh hasil model;
   H-P-S-I-T-C butuh masalah dan solusi yang jelas.
4. **Jumlah slide.** Sweet spot 15; H-P-S-I-T-C itu panjang, SCR itu
   pendek.
5. **Kesesuaian style.** Professional sebagai default; pitch hanya kalau
   user bilang pitch.

### Pool: sembilan metode

Empat alur bisa menstruktur satu deck penuh. Lima lapisan pendukung
selalu menyala, dalam urutan prioritas, dan bukan alternatif walk-down.

**Alur:**

1. **Pyramid.** Kesimpulan dulu, ditopang pohon argumen berjenjang.
2. **H-P-S-I-T-C.** Alur pitch utuh: Hook, Problem, Solution, Impact,
   Traction, Call to action.
3. **SCR.** Situation, Complication, Resolution; alur pendek berbasis
   masalah. SCR juga bersarang di dalam H-P-S-I-T-C: fase Problem pada
   template H-P-S-I-T-C mengikuti struktur SCR. Pool mencantumkan SCR
   sekali; template H-P-S-I-T-C merujuknya.
4. **Data-story.** Masalah, Data, Model, Hasil, Rekomendasi. Alur dari
   deck Company A user sendiri; sudah terbukti bekerja di tangannya.

**Lapisan pendukung (selalu menyala):**

5. **BLUF.** Kesimpulan dulu di setiap level; judul slide adalah kalimat
   kesimpulan. Ini sudah menjadi praktik judul di v1. BLUF adalah prinsip
   yang selalu menyala; Pyramid adalah alur. Keduanya hidup, di level
   berbeda.
6. **One slide one message.** Satu slide, satu pesan.
7. **Data Slide Formula.** Template slide data: temuan, so what, bukti.
   Berlaku hanya untuk slide yang poin utamanya satu temuan data (pada
   uji Company A: slide 5, 6, 7, 8). Slide hook, definisi masalah,
   proses, dan keputusan memakai struktur lain.
8. **Tes "so what?".** Gate per slide; slide tanpa jawaban dipotong atau
   digabung. Skill yang menilai saat membangun; user mengonfirmasi di
   preview HTML.
9. **Storyboard.** Satu baris per slide (pesan ditambah visual) sebelum
   slide apa pun dibangun; duduk di research step.

### Urutan kandidat per jenis deck

Urutan ini adalah prior. Router tetap meranking ulang per kasus; urutan
di bawah hanya titik awal, bukan vonis.

- **Professional / data: Data-story > SCR > Pyramid > H-P-S-I-T-C.**
  Terbukti lewat uji Company A: Data-story #1, SCR #2, Pyramid #3,
  H-P-S-I-T-C #4. H-P-S-I-T-C terakhir karena alur pitch tidak cocok
  untuk deck data dan keputusan.
- **Pitch: H-P-S-I-T-C > Pyramid > Data-story > SCR.** Terkonfirmasi
  lewat uji pitch KopiRumah (24 Nov 2026): H-P-S-I-T-C #1, SCR yang
  bersarang di slide Masalah berfungsi.
- **Case competition (business case, dinilai sebagai dokumen): Pyramid >
  SCR > Data-story > H-P-S-I-T-C.** Prior dengan bukti pendukung: deck
  uji MieLestari memakai Pyramid lebih dulu dan mendapat skor 9 untuk
  kelayakan menang. Metode-metode itu tidak diranking satu lawan satu
  di uji itu, jadi urutan ini tetap prior, bukan ranking terkonfirmasi.
  Mode lengkap di `references/case-competition-mode.md`.
- **Akademik: Data-story > Pyramid > SCR > H-P-S-I-T-C.** Bukti: deck
  Company A user sendiri memakai Data-story (Masalah, Data, Model,
  Hasil, Rekomendasi) dan berhasil; Pyramid kedua karena tiap bagian
  dibuka kesimpulan.

### Aturan saat user memberi metode

- **Eksplisit** ("pakai Pyramid"): ikuti; saran bersifat advisory,
  metode yang diminta menang kecuali user pindah.
- **Implisit** ("buatkan pitch deck", yang menyiratkan H-P-S-I-T-C):
  dihitung sebagai diberi tapi lemah; ikuti, sambil sarankan.
- **Konflik keras vs saran lunak.** Bila metode yang diminta bertabrakan
  dengan batas keras (jumlah slide, tujuan deck, atau aturan skill),
  tandai sebagai KONFLIK dan tanyakan sebelum membangun. Jangan hanya
  menyarankan.
- **Metode di luar pool, atau tidak dikenal:** minta definisi singkat,
  atau perlakukan masukan itu sebagai referensi atau imajinasi (jalur
  "daftar habis"). Jangan pura-pura paham.

### Mekanika walk-down

- Daftar diranking SEKALI per brief; penolakan bergerak turun sesuai
  urutan.
- Pindah #1 ke #2 berarti brief diturunkan ulang (storyboard dan urutan
  slide berubah mengikuti alur), bukan sekadar ganti label.
- Bila user mengubah brief (data, audiens, atau tujuan baru), ranking
  dibuat ulang dari nol.
- Bila daftar habis, ambil jalur referensi atau imajinasi user (deck
  atau gambar acuan menjadi research step).

### Dua mode: general dan focused

- **Mode general:** router yang memilih metode, seperti di atas.
- **Mode focused:** user yang memberi metode. Alurnya sama, tapi langkah
  thinking pertama memakai metode yang diberikan user (ikuti dan
  sarankan), bukan router.

## Jumlah slide

Agent mengira-ngira jumlah slide dan menawarkannya di brief, sebelum
membangun.

- **Slide struktural:** sekitar 5 (judul, masalah dan konteks, metode,
  rekomendasi, referensi).
- **Slide temuan:** satu slide per temuan atau interpretasi kunci dari
  data (satu chart ditambah "so what" per slide); temuan yang kompleks
  dan multi-faset mendapat 2 slide.
- **Sweet spot 15.** Targetkan 15 slide. Lebih banyak atau lebih sedikit
  adalah keputusan agent dari kebutuhan deck (pitch deck 10-12 slide itu
  wajar) bila user tidak meminta jumlah tertentu. Bila user meminta
  jumlah, ikuti permintaannya. Tidak ada lagi floor keras 15.
  Pembengkakan dibatasi gate "so what?" dan one-slide-one-message, bukan
  angka.
- **Cap 15 hanya bila tugas membatasi.** Pada tugas Company A, penilai
  mengabaikan slide yang melewati batas, jadi slide tambahan sama saja
  dengan tidak ada. Pastikan batas dan konsekuensinya untuk setiap tugas
  baru (Alur kerja langkah 1).
- **Mode Case-Competition:** deck utama 10-12 slide; slide appendix
  tidak dihitung ke jumlah slide.

Uji Company A membuktikan estimasi ini: 15 slide diestimasi, 15 dibangun.

## Palet

Jangan pernah bertanya ke user "paletnya apa" sebagai teks mentah.
Jangan pernah memakai satu palet yang sama untuk semua deck.

1. **Pustaka adalah sumbernya.** `references/palette-library.md` memuat
   51 palet bernama: 22 dari reels referensi, 13 kombinasi draf yang
   lolos review eksternal, 16 ditambahkan review itu. Rasio kontras
   dicek dengan rumus WCAG. Palet yang sudah dipakai di satu deck dicatat
   supaya deck berikutnya tidak mengulang tanpa sengaja.
2. **Agent menalar dulu.** Menalar palet dari data, audiens, dan konteks
   deck (deck data atau keuangan yang serius mengambil palet professional
   yang kalem; deck pitch atau investor mengambil palet pitch yang berani;
   deck akademik mengambil palet akademik yang kalem), lalu mengusulkan
   3-4 opsi yang cocok dengan satu baris alasan per opsi.
3. **Selalu visual.** Setiap usulan palet disertai pemilih visual
   (`references/palette-picker-2026-11-24.html`, satu file berisi ke-51
   palet: nama, warna, label cocok). Jangan pernah bertanya soal palet
   hanya lewat teks.
4. **User mengunci satu.** Kunci user yang menang. Bila user menjawab
   "bebas" atau tidak memilih, agent memakai opsi #1-nya sendiri dan
   mencatatnya di brief.
5. **Hanya hex terverifikasi yang menjadi token build.** Hex bertanda ~
   di pemilih adalah perkiraan untuk preview saja, bukan token build.
   Verifikasi hex dari frame resolusi penuh sebelum dipakai sebagai token.
   Token default di "Design token" di bawah hanya fallback bila user
   tidak memilih dan tidak ada acuan.
6. **Pustaka ini hidup.** Tiap referensi baru dari user ditambahkan
   sebagai palet bernama. Ekstraksi palet otomatis penuh dari gambar
   acuan BELUM diadopsi (lihat "Yang masih belum diadopsi"); mekanisme
   yang terbukti adalah "tampilkan 3-4 opsi dari pustaka, user kunci".

## Alur kerja

Lima belas langkah. Konvergen dulu (rencana disepakati), baru build, lalu
refine. Gate user ada di tempat yang tepat. Diagram alir lengkap ada di
`references/alur-kerja-v2-flowchart-2026-11-24.html` (dan `.pdf`).

### Langkah 1. Prompt

User memberi prompt: permintaan deck, materi, data, referensi (deck atau
gambar). Brief untuk deck uji WAJIB menyertakan daftar referensi: brief
yang tidak menyertakannya membuat agent melaporkan "gap" palsu.

### Langkah 2. Agent membaca materi dan prompt

Research step: baca materi, verifikasi sumber (harus bisa dibuka dan
dicari), ekstrak palet dari gambar acuan. Output: sumber terverifikasi,
palet, pemetaan awal. Baca README dan file tutorial tugas langsung dari
disk. Jangan mengandalkan ringkasan browser atau jawaban chat soal format.
Contoh kerja menunjukkan alasannya: laporan browser awal mengarang syarat
16:9, latar putih, presentasi kelompok, dan deadline Google Classroom.
Semuanya tidak ada di dokumen resmi. (Deck final tetap memakai kanvas
16:9 dan latar putih, sebagai pilihan desain, bukan sebagai syarat.)
Untuk tugas yang baru, pastikan aturan yang benar sebelum menulis apa
pun, termasuk jumlah slide dan apa yang terjadi bila melewati batas.
Catat aturan itu di file aturan baru yang diformat seperti
`references/deck-rules.md`, dan lakukan sebelum build dimulai.

### Langkah 3. Agent thinking

Router: ranking 9 metode pada 5 dimensi, estimasi jumlah slide
(struktural sekitar 5 ditambah 1 per temuan kunci; sweet spot 15), dan
draf storyboard (satu baris per slide: pesan ditambah visual).

### Langkah 4. Prototyping, rencana

Susun prototipe rencana, yaitu brief: metode #1 dengan alasannya,
estimasi slide, storyboard, palet, density. Ada dua prototyping di alur
ini dan keduanya beda jenis: prototipe #1 adalah prototipe rencana (brief
ini); prototipe #2 adalah prototipe deck (preview HTML di langkah 9).

### Langkah 5. Tanyakan ke user apa yang agent butuhkan

Agent bertanya 3-5 pertanyaan selera: hal yang masih belum jelas dari
materi atau prompt. Satu pertanyaan standar, ditanyakan bersama pertanyaan
selera: "bolehkah agent cari gambar atau aset di internet?" Jawaban
dicatat di brief (langkah 6-7) dan dibekukan di Spesifikasi Beku (langkah
10), supaya build (langkah 11) tidak perlu bertanya lagi. Bila user
menjawab "hanya materi saya" dan materinya tidak ada gambar yang bisa
dipakai, tandai sebagai GAP di brief; jangan diam-diam membangun deck
kosong. Default bila user tidak menjawab: BOLEH, tapi hanya dari daftar
sumber gratis berlisensi yang terverifikasi, bukan gambar AI-generated
(user lebih suka foto asli, bukan AI). Brief selalu menampilkan rencana
aset, jadi user bisa veto di gate langkah 7. Setiap gambar dan aset
membawa sumbernya (di slide atau di referensi); pakai hanya sumber yang
terbukti bisa dibuka dan dicari.

### Langkah 6. Agent thinking

Olah jawaban user, revisi brief.

### Langkah 7. Minta konfirmasi, atau beri rekomendasi (GATE)

Agent meminta konfirmasi brief, atau memberi rekomendasi; user setuju
atau mengubah. Tanyakan SEMUA detail yang kurang itu sekaligus, dalam
satu pesan konfirmasi (tentang apa, buat siapa, tujuan, data yang hilang),
bukan satu-satu bergiliran, supaya user langsung menangani semuanya
dalam sekali jawab. **Konfirmasi tetap dilakukan walau materi sudah
cukup:** selalu tampilkan konfirmasi sekaligus sebelum build, berisi
yang dipahami agent dari materi (tentang apa, buat siapa, tujuan)
ditambah usulan palet 3-4 opsi dengan pemilih visual, supaya user bisa
mengoreksi dan mengunci semuanya dalam sekali jawab. Ini adalah gate
persetujuan brief. Tidak ada build sebelum brief dan palet dikonfirmasi.
Bila user menjawab "bebas" atau "lanjut", agent memakai penalarannya
sendiri dan mencatatnya di brief. Di Mode Case-Competition, konfirmasi
mencakup cakupan deck utama dan appendix sekaligus.

### Langkah 8. LOOP: thinking dan feedback user

Ulangi langkah 6-7 sampai brief converge. Output: brief final.

### Langkah 9. Prototyping, deck

Bangun preview HTML deck lengkap. Preview adalah gate iterasi: user
meninjau seluruh deck di browser sebelum apa pun dirender ke PDF.

### Langkah 10. Get condition: Spesifikasi Beku

Kumpulkan semua keputusan yang sudah disepakati (metode, jumlah slide,
palet, konten, izin aset, density) sebagai spesifikasi final sebelum
build. Tulis sebagai checklist. Setelah beku, build mengikutinya;
perubahan setelah beku membuka ulang langkah 7, bukan mengedit build
diam-diam. Checklist humanizer (langkah 11) adalah item di Spesifikasi
Beku.

### Langkah 11. Take action: build

Build: satu file HTML per slide, ditambah chart. Tulis teks dalam
bahasa Indonesia dulu, lalu jalankan pipeline bahasa sebagai CHECKLIST,
dengan urutan ini: teks Indonesia, pass `humanizer-indonesia`, terjemah
ke Inggris, pass `academic-humanizer` hanya pada prosa Inggris. Langkah
ini mudah terlewat; ia adalah item checklist di Spesifikasi Beku, bukan
ingatan. Lalu assemble. Lihat "Pipeline bahasa" di bawah dan
`references/humanizer-rules.md`.

### Langkah 12. Validasi agent: data dan tampilan

Validasi data (angka cocok dengan notebook atau sumber) dan tampilan
(token desain, layout, tidak overflow). Output: daftar temuan. Dua
pelajaran validasi, keduanya dari build nyata:

- **Validasi file dari agent yang diuji.** Blok kode panjang yang
  ditranskripsi dari tampilan halaman bisa tercampur baris draf (blok
  Thought yang terlipat). Minta kirim ulang per potongan (chunked);
  koreksi agent tentang filenya sendiri yang berwenang; verifikasi
  visual wajib sebelum klaim selesai.
- **Baca halaman hasil render, bukan hanya cek overflow.** Cek overflow
  yang hanya menandai elemen yang melewati tepi slide tidak menangkap
  konten yang terpotong bar dalam. Di build MieLestari, slide S2 v9
  terpotong 16 px oleh insight bar dan lolos cek 113/113. Baca halaman
  hasil render, terutama slide yang isinya bertambah di ronde itu.

### Langkah 13. Refine

Perbaiki temuan validasi.

### Langkah 14. LOOP: validasi dan refine (GATE)

Ulangi langkah 12-13 sampai cek data lolos DAN user menyetujui preview.
Bila mentok, eskalasi ke user; jangan mengulang sendiri. Aturan
berhenti: berhenti saat cek data lolos dan user menyetujui preview.

### Langkah 15. Serahkan ke user

Serahkan paket final: PDF ditambah sumber deck. Versi PPTX bisa dibuat
dari slide hasil render, tapi hanya sebagai deck berbasis gambar: satu
PNG hasil render per slide, dengan judul slide sebagai speaker notes.
Teksnya tidak bisa diedit. Itu keterbatasan, bukan fitur. Jalur PPTX
teks-editable BELUM diadopsi (lihat "Yang masih belum diadopsi"). PDF
adalah deliverable utama.

### Pipeline bahasa (langkah 11, rinci)

1. Tulis draf teks deck dalam bahasa Indonesia dulu (`content-id.md`
   pada contoh kerja). Satu bagian per slide: Title, Composition,
   Exhibit, Content, Footnote. File `examples/content-id.md`
   menunjukkan format tiap bagian. Tulis angka dengan notasi yang
   diharapkan `scripts/check_numbers_final.py`, supaya angka Indonesia
   dan Inggris cocok persis. Jaga urutan slide tetap identik di kedua
   bahasa.
2. Jalankan humanizer bahasa Indonesia. Terapkan aturan
   `humanizer-indonesia` pada draf Indonesia. Pakai skill yang sudah
   terpasang jika tersedia. Ringkasan aturannya ada di
   `references/humanizer-rules.md`. Pass ini membuang tanda-tanda AI dan
   bahasa terjemahan (kalke, yaitu calque) tanpa mengubah angka, sitasi,
   atau rujukan silang apa pun. Jalankan skrip metrik skill itu jika
   tersedia, dan perbaiki yang ditandai. Pengukuran draf Indonesia pada
   contoh kerja: rerata panjang kalimat 14,4 kata, simpangan baku 8,8,
   0 em/en dash. Humanizer menghasilkan draf untuk disunting manusia,
   jadi sunting hasilnya dengan tangan setelahnya.
3. Terjemahkan ke Inggris, lalu jalankan humanizer Inggris. Terjemahkan
   draf Indonesia ke Inggris (`content-en.md`). Lalu terapkan aturan
   `academic-humanizer` hanya pada prosa Inggris. Pakai skill yang sudah
   terpasang jika tersedia. Jangan pernah menerapkan humanizer pada
   judul, angka, nama model, sitasi, atau rumus. Judul adalah kalimat
   lengkap yang membawa angka, jadi tulis ulang judul yang lemah dengan
   tangan, jangan jalankan lewat humanizer.

Dua pelajaran dari build aslinya, keduanya ditemukan lewat review
independen:

- Pertahankan hedge epistemik seperti "to the best of our knowledge"
  saat kalimat membuat klaim kebaruan.
- Jangan biarkan perbaikan gaya mengubah besaran samar menjadi klaim
  spesifik yang eksklusif. Perbaikan yang menyebut setting tertentu
  ("only on ...") adalah klaim empiris baru. Cek ke tabel hasil sebelum
  mempertahankannya.

Lihat `references/humanizer-rules.md`.

### Analisis sebelum build

Spesifikasi Beku membekukan metode, jumlah slide, palet, dan rencana
konten. Analisis berjalan setelah beku dan sebelum teks ditulis di
langkah 11. Judul tetap hipotesis kerja sampai analisis menghasilkan
angka.

- **Jalankan analisis, lalu tulis judul slide dari angkanya.** Judul
  adalah kalimat kesimpulan lengkap yang membawa angka, maksimal dua
  baris. Contoh dari contoh kerja: "Churn jumps from 37.4% for handsets
  aged 270-300 days to 60.3% for handsets aged 300-330 days, a gap of
  22.9 percentage points." Jangan pernah menulis judul sebelum angka yang
  mendasarinya ada. Masukkan setiap angka yang dipakai di judul ke lembar
  angka terverifikasi, termasuk angka turunan seperti selisih 22,9 poin.
  Bandingkan model pada split train/test yang sama dan laporkan akurasi,
  AUC, precision, dan recall. Cantumkan margin of error di samping skor
  jika split-nya cukup besar untuk dihitung. Uji feature engineering dan
  laporkan hasilnya walaupun tidak membantu. Pada contoh kerja, feature
  engineering tidak membantu (akurasi cross-validasi 0,6224 dengan fitur
  baru melawan 0,6239 tanpa fitur baru), jadi fiturnya dibuang dan hal itu
  dinyatakan di slide.
- **Tetapkan framing pasar dan kalimat batasnya.** Bila perusahaan dalam
  kasus bersifat anonim, katakan di slide, dan katakan pasar nyata mana
  yang dipakai hanya sebagai acuan. Tulis kalimat batas lebih awal dan
  ulangi di tempat pembaca bisa salah mengira pasar acuan sebagai
  perusahaan itu sendiri. Contoh: "Company A is anonymous. Indonesia is
  only a reference market, and the model results are not claimed to
  represent Indonesian customers." Verifikasi tiap sumber pasar dengan
  membukanya sendiri (aturan keras 5) sebelum angka pasar masuk deck.

### Disiplin verifikasi

- **Satu file angka kanonik adalah satu-satunya sumber kebenaran.**
  Simpan setiap angka yang tampil di deck dalam satu file kanonik (JSON
  pada build MieLestari), yang dihitung dari model atau notebook yang
  dieksekusi. Deck hanya menampilkan; ia tidak pernah mengarang angka
  dengan tangan. Versi baru deck mendapat file kanonik baru; file lama
  disimpan.
- **Satu checker per versi.** Sesuaikan `scripts/check_numbers_final.py`
  dengan deck yang baru dengan mengganti lembar terverifikasinya (bagian
  `SHEET`) dengan angka deck yang baru, yang diambil dari notebook yang
  dieksekusi. Jalankan. Checker memeriksa tiga hal: angka identik antara
  teks Indonesia dan Inggris, slide per slide; setiap angka ada di lembar
  terverifikasi, sebagai nilai, nilai kali 100, atau nilai bagi 100;
  larangan gaya berlaku (tanpa angka yang dilarang seperti yang
  didefinisikan di skrip, tanpa em/en dash, tanpa emoji, tanpa kata yang
  dilarang, tanpa tanda hubung berspasi). Hasilnya harus nol masalah.
  Lalu jalankan pengecekan notebook lawan deck dengan
  `scripts/check_notebook_vs_deck.py` (sesuaikan path dan daftar `CHECKS`
  dengan deck yang baru). Pada build aslinya hasilnya 51 PASS dan 9 FAIL.
  Setelah ditinjau, kesembilan FAIL masuk kategori yang dinilai tidak
  bermasalah: nilai yang hanya ada di notebook, selisih aritmetika
  turunan, dan nilai rank yang memang ditampilkan sebagai rank. Lihat
  `references/number-verification.md`. Catat kategori yang tidak
  bermasalah itu secara tertulis. FAIL tanpa alasan tertulis adalah
  cacat terbuka.
- **Perbaiki teksnya, bukan checkernya.** Bila cek gagal, ubah teks deck
  atau modelnya, jangan pernah ceknya.
- **Asersi geometri di checker.** Checker juga harus mengasersi geometri
  layout: tepi bawah setiap elemen minimal 8 px di atas atas insight bar,
  di setiap slide. Build MieLestari v9 lolos 113/113 cek sementara satu
  slide terpotong 16 px oleh insight bar-nya, karena cek hanya menandai
  elemen yang melewati tepi slide.
- **Baca halaman hasil render.** Setelah render, baca setiap gambar
  halaman dengan mata. Cari overflow, angka yang berbeda dari teks
  Inggris, dan slide data yang kehilangan footnote sumber. Jangan
  serahkan deck dengan overflow.

### Build deck

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

- Jalankan `pdfinfo`. Untuk deck contoh kerja: 15 halaman pada 960 kali
  540 pt. Ukuran ini sama dengan kanvas 1280 kali 720 px pada 96 px per
  inci.
- Jalankan `pdffonts`. Setiap font yang terdaftar harus Source Sans 3
  (Regular atau Bold) dan menunjukkan `yes` di kolom `emb`.
- Baca setiap PNG hasil render (di `.src/validate/`). Cari overflow,
  angka yang berbeda dari teks Inggris, dan slide data yang kehilangan
  footnote sumber.

Argumen perintah, pipeline lengkap, dan gate-nya ada di
`references/toolchain.md`. Jebakan print CSS, dipelajari di uji pitch
KopiRumah: matikan zoom JS di print CSS (`.frame{zoom:1!important}`,
`@page{size:1280px 720px}`); selalu periksa UKURAN slide di halaman PDF
hasil render, bukan hanya jumlah halaman. Lima jebakan build HTML/CSS
lain dari deck uji (flex `<br>`, stretch, flex-shrink, lebar font
fallback, unit marker SVG) ada di `references/toolchain.md`.

### Serahkan paketnya

Serahkan PDF, notebook, dan daftar referensi lewat platform mata kuliah.
Daftar referensi di slide terakhir dan daftar yang ditempel ke kolom
References platform harus daftar yang sama. Kalau tugas meminta
pengungkapan pemakaian AI, daftar itu memuat URL sesi AI. Jangan pernah
melampirkan transkrip chat AI. Ganti nama `deck.pdf` mengikuti aturan
nama file platform. Pada contoh kerja, filenya adalah `[AccountName].pdf`
dan `[AccountName].ipynb`, dengan nama akun Rajendriya.

## Mode Case-Competition

Pakai mode ini bila deck adalah business case yang dinilai dingin, tanpa
presenter. Spesifikasi lengkap ada di `references/case-competition-mode.md`;
bentuknya:

- **Dua lapis dalam satu file.** Deck utama (narasi, 10-12 slide, density
  pitch: satu klaim per slide, maksimal 6 baris, satu grafik per slide,
  slide 1 adalah cover dan jawaban ada di slide 2) ditambah appendix
  (density dokumen, satu analisis per slide, berdiri sendiri, sumber DI
  slide). Satu slide pembatas ("Lampiran / Appendix") berdiri di antara
  keduanya. Slide appendix tidak dihitung ke jumlah slide.
- **Jawaban dulu.** Rekomendasi dan angka kunci ada di slide 2, bukan di
  akhir. Tiap slide utama dibuka kicker pertanyaan ("| Q: ...") dan judul
  kalimat yang membawa angka.
- **Tulang punggung yang bisa dilacak.** Kesenjangan, akar masalah, lengan
  solusi, KPI, dan baris keuangan memakai satu rantai ID yang sama di
  seluruh deck, supaya juri bisa menelusuri satu angka dari rekomendasi
  sampai ke asumsinya tanpa bertanya.
- **Kerangka bernama sebagai rubrik.** MAUT, Monte Carlo, tornado,
  break-even, FMEA, Gate 0 dengan kill criteria. Juri bisa mencentang
  "rigor analitik" tanpa berpikir.
- **Tunjukkan kerja.** Asumsi di depan, kalibrasi, sensitivitas, skenario
  downside, dan batas yang diakui. Probabilitas 100% tanpa input yang
  terlihat justru menurunkan kredibilitas, jadi tampilkan distribusinya.
- **Ada yang bisa disentuh juri.** Kode QR atau tautan ke model yang
  bekerja (spreadsheet, repo), bukan janji.
- **Tutup dengan keputusan yang diminta.** Slide implementasi memuat
  keputusan yang diminta, tahapan dengan kriteria berhenti, dan metrik
  pemicu.
- **Langit-langit kejujuran.** Kasus fiktif tanpa data primer mentok di
  skor kelayakan menang 9. Jangan pernah menjanjikan 10. Asumsi dilabeli,
  batas dinyatakan sebagai Fase 2, angka tidak pernah dikarang.

Contoh kerjanya adalah deck MieLestari (v10 FINAL, 43 slide, skor 9).
Lihat `references/case-competition-mode.md`.

## Aturan desain

Sembilan belas aturan empiris, dari uji Company A (aturan 1-14), reel
"10 Niche Design Hacks" (aturan 15-18), dan uji MieLestari (aturan 19).
Bila aturan dan tampilan yang bagus bertabrakan, tampilan yang menang;
catat perubahannya.

1. **Berani pada skala tipografi dan box.** Judul 36 px dua baris (klaim
   tebal ditambah lanjutan ringan 26 px); angka kunci jadi display figure
   48 px di judul; angka hero 104-200 px. Output router yang aman dan
   konservatif adalah cacat, bukan fitur. Skill harus mendorong hierarki
   berani sebagai bagian dari build.
2. **Exhibit harus mengisi tinggi slide.** Exhibit satu elemen yang tipis
   akan melayang di ruang kosong. Perbesar dan pusatkan vertikal sampai
   mengisi slide.
3. **Judul adalah elemen display, bukan blok teks.** Angka kunci
   diekstrak dari judul dan diperbesar sebagai display figure.
4. **Display figure harus SEIRAMA.** Sewarna dan sesuara dengan judul
   (navy, tanpa text-shadow atau kontur); hierarki hanya dari ukuran
   ditambah weight. Kombinasi warna kontras ditambah kontur terbaca
   "maksa beda sendiri".
5. **Angka display tidak boleh terjebak di dalam tanda kurung kecil.**
6. **Penempatan informasi kreatif.** Diagonal atau berjenjang (tangga
   menaik, kartu berjenjang, baris digeser), bukan kotak sejajar yang
   kaku. Tangga MENAIK (langkah awal paling bawah) membaca sebagai
   progres; bentuk tangga itu sendiri menunjukkan arah. Jangan memaksa
   panah ke celah sempit (14 px).
7. **Bentuk background: HARUS berani dan niat, atau tidak ada sama
   sekali.** Aksen kecil yang nanggung terbaca sebagai noise dan harus
   dihapus. Bentuk background tidak boleh masuk area konten; aksen hanya
   di zona padding atau di belakang kartu (kartu berlatar putih).
   Lingkaran atau oval besar di belakang grafik atau tabel menabrak
   informasi dan menyakitkan mata, walau warnanya cocok.
8. **Kartu persegi tidak boleh menembus bentuk miring di belakangnya.**
   Fit harus dihitung (inset ditambah ukuran trapesium disesuaikan).
9. **Garis perbandingan (putus-putus) harus di atas bar atau dihapus;**
   kalau panjang bar saja sudah menunjukkan terbaik atau terjelek, hapus
   garisnya.
10. **Bentuk mini di tepi** (segitiga atau trapesium kecil) yang tidak
    berani sekaligus tidak tak terlihat adalah gangguan. Buang.
11. **Kotak callout butuh label penjelas** (judul kecil) supaya pembaca
    tahu angka itu untuk apa.
12. **Panel judul** (tint ditambah garis atas koral 6 px) adalah uji batas
    maksimal yang LOLOS. Pertahankan sebagai perlakuan judul standar pada
    varian berani.
13. **Aset adalah bagian dari build, bukan opsi.** Foto atau ilustrasi
    lisensi bebas dipakai sejak awal (slide 1 panel foto vertikal, kredit
    di footer ditambah referensi). Hotlink bisa gagal di render headless,
    jadi embed sebagai base64 data URI supaya file mandiri. **Pitch deck
    kaya aset di tiap slide:** tiap slide punya gambar atau aset visual
    yang relevan dengan isinya, bukan cuma 2-3 foto di cover, solusi,
    atau ask; sumber hanya lisensi bebas (Wikimedia Commons CC0 atau
    domain publik, Pexels), tidak pernah AI-generated; lisensi
    diverifikasi sebelum dipakai. **Prinsip ruang besar:** foto lingkungan
    atau area HANYA dipakai kalau dapat ruang besar (panel penuh,
    full-bleed, atau pita selebar slide yang substansial) supaya audiens
    paham gambar itu menunjukkan apa; kalau slide tidak bisa memberi ruang
    besar, foto DIHAPUS, bukan diperkecil atau dipindah ke pojok. Foto
    yang tidak mengilustrasikan isi slide dihapus walau ruangnya ada.
14. **Kontras.** Koral di atas biru sekitar 2,2:1 tidak terbaca. Teks di
    atas koral atau tint memakai ink gelap (#023A6B); aksen koral di atas
    biru memakai putih (sekitar 4,7:1).
15. **Sudut bersarang harus konsentris.** Radius dalam sama dengan radius
    luar dikurangi padding (kartu di dalam kartu atau panel). Sudut yang
    tidak cocok terlihat salah walau selisihnya kecil.
16. **Border pakai alpha, bukan hex solid.** Border solid terlihat jelek
    di atas latar yang berbeda; warna alpha menyatu dengan latar apa pun.
    Ini penting karena deck kita memakai banyak latar berwarna.
17. **Warna di OKLCH, bukan HSL.** Mata mempersepsi lightness tidak
    merata. Palet dan gradien dibangun di OKLCH supaya lightness yang
    sama terlihat sama dan gradien tidak mengabu di tengah (gradien
    memakai "in oklch").
18. **Bobot ikon disamakan dengan bobot teks.** Ikon tipis di sebelah teks
    tebal terlihat ceroboh; samakan stroke ikon dengan weight font di
    sebelahnya.
19. **Simetri: isi panel terdistribusi vertikal.** Isi panel harus
    tersebar vertikal (flex space-between atau center), jangan menumpuk di
    atas dengan ruang kosong lebih dari 40 px di bawah teks. Deck
    case-competition hampir tidak punya ruang kosong; layout harus BOLD
    dan tidak boxy.

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

Token ini adalah token default v1. Token ini adalah fallback bila user
tidak memilih palet dan tidak ada acuan. Deck yang mengunci palet dari
`references/palette-library.md` memakai token palet itu; deck MieLestari
misalnya memakai navy `#0B2E6E` dan `#12264A`, biru `#1F4E9C`, emas
`#E8A33D` dan `#F5B544`, dengan Poppins dan Montserrat. Token lengkap,
angka kontras, delapan aturan aksen, dan daftar periksa untuk menghindari
tampilan generik ada di `references/design-tokens.md`.

## Tata letak file proyek deck

```
deck/
  content-id.md            draf Indonesia, satu bagian per slide
  content-en.md            teks Inggris final, urutan slide sama
  check_numbers_final.py   checker angka dan gaya (sesuaikan SHEET)
  canonical-numbers.json   angka kanonik, satu-satunya sumber kebenaran
  frozen-spec.md           checklist Spesifikasi Beku (Alur kerja langkah 10)
  .src/
    slides/                satu HTML per slide, deck.css, deck.json
    media/                 grafik (PNG), foto, font, build_charts_v2.py
    index.html             dokumen gabungan (dihasilkan)
    validate/              PNG per halaman dari PDF final (dihasilkan)
  deck.pdf                 output akhir
```

## Dependensi

- `academic-humanizer` (humanizer Inggris; MIT; AIScientists-Dev;
  v0.3.3): enam layer, audit dulu baru tulis ulang, angka dan sitasi
  dipertahankan, tidak pernah mengarang bukti. Sumber:
  https://github.com/AIScientists-Dev/academic-humanizer. Ringkasannya di
  `references/humanizer-rules.md`.
- `humanizer-indonesia` (humanizer Indonesia; MIT; adhiprib; v1.7.2): draf,
  audit, lalu revisi akhir. Membuang tanda AI dan bahasa terjemahan. Sumber:
  https://github.com/adhiprib/humanizer-indonesia. Ringkasannya di
  `references/humanizer-rules.md`.
- Panduan presentasi dari skill `documents` (satu file HTML per slide,
  ditambah `deck.css` dan `deck.json`, dirakit dengan cara yang sama setiap
  kali): pola tata letak yang diikuti skill ini.
- Skrip di `scripts/`: `assemble_deck.mjs`, `render_audit.mjs`,
  `validate_pdf.sh`, `build_charts_v2.py`, `check_numbers_final.py`,
  `check_notebook_vs_deck.py`, `build_deck.py`. Lihat
  `references/toolchain.md` untuk peran tiap skrip dan asalnya.
- Tool riset dan build yang diminta user: **Statista** untuk riset pasar
  (ukuran pasar, data industri, perilaku konsumen; sebagian besar konten
  berbayar, jadi pakai statistik gratisnya dan sitasi sumbernya, dan
  jangan pernah mengklaim angka yang tidak bisa diverifikasi); **Google
  Trends** untuk insight konsumen (gratis, tren pasar real-time dan
  perubahan minat konsumen, bukti pendukung untuk slide masalah dan tren
  serta appendix); **Canva / Google Slides** untuk desain deck saat build
  (tier dasar gratis). Ketiganya adalah tool umum yang direkomendasikan
  user, bukan kutipan dari materi pihak ketiga, dan tidak ada materi
  pihak ketiga yang disalin ke repo ini.
- Tool yang dibutuhkan perintah build: Python dengan matplotlib, Bun,
  Playwright dengan headless Chromium, `pdfinfo` dan `pdffonts` (dari
  poppler-utils), dan file font Source Sans 3. Versinya tidak dicatat di
  skill ini.

## Yang masih belum diadopsi

Item-item ini adalah keputusan terbuka, bukan aturan. Jangan ajarkan
sebagai aturan sampai diuji dan diadopsi di versi baru.

- **Jalur PPTX teks-editable** (python-pptx atau jalur lain). PPTX yang
  didukung hari ini hanya berbasis gambar (satu PNG hasil render per
  slide). Lihat `references/toolchain.md`.
- **Density switch professional vs pitch.** Tetap ada sebagai preset.
  Catatan: selera user adalah tipografi display yang berani bahkan untuk
  deck professional, jadi "berani" bukan cuma milik pitch.
- **Ekstraksi palet otomatis penuh** dari gambar acuan. Mekanisme yang
  terbukti adalah "tampilkan 3-4 opsi dari pustaka, user kunci".
- **Daftar aset gratis.** Daftar sumber berlisensi gratis; lisensinya
  terverifikasi pada Oktober 2026 dan daftar itu diteliti ulang pada
  November 2026; daftar itu harus diverifikasi ulang sebelum diadopsi
  ke skill ini.
- **Sitiran processing fluency.** Paper (Reber et al. 2004) diusulkan
  sebagai pendukung desain carousel; paper itu BELUM terverifikasi, jadi
  jangan dikutip.

## File referensi

| File | Isinya |
|---|---|
| `references/deck-rules.md` | Aturan tugas dan rencana 15 slide |
| `references/number-verification.md` | Disiplin angka, checker, kasus nyata |
| `references/design-tokens.md` | Warna, font, ukuran, aturan foto dan aksen |
| `references/toolchain.md` | Pipeline build, skrip, gate, batas PPTX |
| `references/humanizer-rules.md` | Kedua skill humanizer, ringkas, dengan peringatan |
| `references/worked-example.md` | Deck churn Company A, angka dan peta slide |
| `references/case-competition-mode.md` | Spesifikasi Mode Case-Competition dan contoh kerja MieLestari |
| `references/palette-library.md` | 51 palet bernama dengan label cocok |
| `references/palette-picker-2026-11-24.html` | Pemilih palet visual, ke-51 palet |
| `references/alur-kerja-v2-flowchart-2026-11-24.html` | Diagram alir alur kerja (HTML) |
| `references/alur-kerja-v2-flowchart-2026-11-24.pdf` | Diagram alir alur kerja (PDF) |
| `references/roadmap.md` | Ide untuk versi mendatang; tidak ada yang di sini menjadi aturan |
| `CHANGELOG.md` | Riwayat versi, apa yang berubah, apa yang masih terbuka |
| `examples/content-en.md` | Teks deck Inggris final (contoh kerja) |
| `examples/content-id.md` | Teks draf Indonesia (contoh kerja) |
| `scripts/` | Skrip toolchain, disalin apa adanya |
