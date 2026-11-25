# kurori-deck-skill

Membangun deck proposal bisnis yang didukung analisis data, dengan cara
yang dipakai pada deck proposal bisnis aslinya: draf bahasa Indonesia
dulu, lalu humanizer, angka diverifikasi ke notebook yang dieksekusi,
satu file HTML per slide, dan render PDF dengan pipeline yang bisa
diulang. Maksimal 15 slide; setiap angka membawa sitasi di slide tempat
angka itu muncul.

Asal: deck proposal bisnis aslinya (churn telekomunikasi Company A), November 2026. Paket yang sudah jadi diserahkan ke penulisnya; file PDF
deck itu tidak disertakan di sini. Yang disertakan adalah metodenya,
aturannya, toolchain-nya, dan teks deck sebagai contoh kerja.

## Isi repo

| Path | Isinya |
|---|---|
| `SKILL.md` | Skill-nya, dalam bahasa Inggris (mulai dari sini) |
| `SKILL-id.md` | Skill-nya, dalam bahasa Indonesia (isi sama, ditulis ulang natural) |
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
| `CHANGELOG.md` | Riwayat versi, apa yang berubah, apa yang masih terbuka |
| `examples/content-en.md` | Teks deck Inggris final (contoh kerja) |
| `examples/content-id.md` | Teks draf Indonesia (contoh kerja) |
| `scripts/` | Skrip toolchain, disalin apa adanya |

## Instalasi

Skill ini netral terhadap host: isinya folder Markdown dan skrip, dan bisa
dipakai di AI host apa pun yang memuat skill dari folder. Salin seluruh
folder `kurori-deck-skill` ke direktori skill host yang dipakai, lalu arahkan
host ke folder itu dengan cara host tersebut memuat skill lokal.

- Claude Code: salin ke `~/.claude/skills/kurori-deck-skill/`
- Codex: salin ke direktori skill pada instalasi Codex
- Muse: salin ke `~/workspace/custom-skills/kurori-deck-skill/`
- Host lain: salin ke direktori tempat host itu membaca skill lokal

Tidak ada langkah build dan tidak ada instalasi tambahan untuk teks skill
itu sendiri. Skrip toolchain butuh runtime masing-masing saat build
dijalankan (Bun, Python 3 dengan matplotlib dan pandas, Playwright dengan
Chromium, `pdfinfo`, `pdffonts`, `pdftoppm`). Lihat
`references/toolchain.md`.

Kedua skill humanizer adalah proyek terpisah dan tidak dibundel di sini.
Instal dengan cara yang sama, dari repo masing-masing, bila ingin pipeline
bahasa yang lengkap:

- `academic-humanizer` (Inggris): AIScientists-Dev/academic-humanizer,
  https://github.com/AIScientists-Dev/academic-humanizer, MIT, v0.3.3
- `humanizer-indonesia` (Indonesia): adhiprib/humanizer-indonesia,
  https://github.com/adhiprib/humanizer-indonesia, MIT, v1.7.2

## Cara pakai

1. Baca dulu `SKILL.md` (atau `SKILL-id.md`).
2. Baca README dan file tutorial tugas langsung dari dokumennya, dan
   tuliskan aturan yang benar sebelum mulai menulis draf.
3. Ikuti lima belas langkah alur kerja secara berurutan: routing metode
   dulu, bekukan brief di gate langkah 7, build dari Spesifikasi Beku,
   dan jangan lewati langkah verifikasi angka: checker harus melaporkan
   nol masalah sebelum deck dibangun.
4. Sesuaikan `scripts/check_numbers_final.py` dengan deck yang baru dengan
   mengganti lembar angka terverifikasi (`SHEET`) dengan angka terverifikasi
   yang baru. Biarkan larangan gaya apa adanya.
5. Pakai `examples/content-en.md` dan `examples/content-id.md` sebagai
   bentuk teks deck: satu bagian per slide, Title, Composition, Exhibit,
   Content, Footnote.
6. Untuk deck yang dinilai dingin tanpa presenter, pakai Mode
   Case-Competition (`references/case-competition-mode.md`).

## Aturan keras, singkatnya

Jumlah slide mengikuti tugas; 15 adalah sweet spot, bukan floor keras.
Minimal satu model dengan nama, metrik, dan skor ditulis eksplisit di teks
slide. Kutipan langsung di bawah 40% dari teks deck, sebagai patokan.
Setiap angka membawa sumbernya di slide yang sama. Data pasar hanya setelah
sumbernya terbukti bisa dibuka. Skor model harus cocok dengan notebook yang
dieksekusi. Transkrip chat AI tidak pernah dipublikasikan (hanya URL sesi).
Tanpa em-dash, tanpa en-dash di teks slide, tanpa emoji, tanpa gaya
penulisan AI. Nama model dikecualikan dari larangan kata. Angka tidak pernah
dikarang atau disalin dari ingatan.

## Yang bukan bagian skill ini

Framework pitch deck yang di v1 terdaftar sebagai kandidat (H-P-S-I-T-C,
SCR Framework, Pyramid Principle, One slide One message, metode BLUF,
Data Slide Formula, pendekatan Storyboard, tes "So what?") diadopsi di v2
sebagai pool router. Yang masih bukan bagian skill ini: jalur PPTX
teks-editable (PPTX hari ini hanya berbasis gambar), density switch
professional vs pitch, ekstraksi palet otomatis penuh, daftar aset gratis
(butuh verifikasi ulang), dan sitiran processing fluency (paper belum
terverifikasi). Lihat `CHANGELOG.md`.

## Lisensi

MIT. Copyright 2026 Rajendriya Wigar Punagi. Lihat `LICENSE`.
