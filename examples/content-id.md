# Deck v2: GCI World 2026 Final Assignment (Company A, churn telekomunikasi)

Blueprint singkat (langkah 1 sampai 3 workflow)
- Tujuan: meyakinkan eksekutif Company A bahwa program retensi bertarget layak diuji lewat pilot dengan kelompok kontrol.
- Audiens: eksekutif tanpa latar ML. Satu ide per slide, satu exhibit per slide hasil.
- Pesan kunci: churn naik tajam setelah handset berusia 300 hari, model cukup untuk memprioritaskan pelanggan, program impas pada save rate rendah, tetapi save rate belum terbukti.
- Alur cerita: hook (1-2), masalah (3-4), insight (5-8), solusi (9-12), biaya (13), kesimpulan (14), referensi (15).

### Slide 1
Judul: Pelanggan pergi mendadak setelah handset mencapai 300 hari, dan tawaran retensi impas jika menahan 2,3% dari pelanggan yang akan pergi (asumsi tinggal 12 bulan)
Komposisi: Katalog 350, kategori 08, nomor 335 (title slide). Arketipe: tab foto menara telekomunikasi duotone navy kecil di kiri, panel navy di belakang, kolom teks bergeser ke kanan, satu blok emas lembut di kolom teks. Alasan: pembuka tenang yang langsung menaruh dua angka tesis, dan blok emas lembut menandai satu angka yang harus diingat.
Exhibit: tidak ada. Slide judul tidak membawa grafik. Foto menara telekomunikasi, dipotong dan diwarnai ulang menjadi duotone navy, terletak sebagai tab kecil di kiri. Foto: Väinö Parjanen / Pexels [13].
Isi:
- Sebuah proposal berbasis data untuk Company A, operator telekomunikasi anonim.
- Churn artinya pelanggan pergi 31-60 hari setelah tanggal observasi. Save rate artinya bagian pelanggan yang tadinya akan pergi tetapi dipertahankan oleh tawaran.
- Pasar referensi: Indonesia, dipakai hanya sebagai latar pasar. Hasil model tidak diklaim mewakili pelanggan Indonesia.
- GCI World 2026 Final Assignment | Rajendriya
- Blok emas lembut: Impas pada save rate 2,3% (asumsi tinggal 12 bulan)
Footnote: tidak ada. Kalimat pasar referensi pindah ke isi.

### Slide 2
Judul: Pasar acuan Indonesia memiliki sekitar 297 juta pelanggan aktif, dan sekitar 97% di antaranya prabayar, sehingga pelanggan mudah pindah
Komposisi: Katalog 350, kategori 08, nomor 338 (two content). Arketipe: split vertikal 35/65, panel navy berisi tiga angka, sisi putih berisi grafik. Alasan: konteks pasar dibaca sekilas lewat tiga angka, grafik operator menjadi bukti pendukung.
Exhibit: Panel navy dengan tiga angka: 297 juta pelanggan aktif (Q3 2026, Komdigi [2]), 97% prabayar (PwC [1]), USD 17-18 miliar revenue telekomunikasi 2025 (PwC [1]). Grafik batang horizontal pelanggan per operator: Telkomsel 157,6 juta (Sep 2025) [7], Indosat 91,5 juta (Q3 2026) [4], XLSmart 70 juta (Q3 2026) [5]. Tanggal dan penanda sitasi tiap batang ditulis di batang. Anotasi: Operator terbesar, memakai angka pelanggan dari laporan masing-masing. Angka operator memakai tanggal dan definisi berbeda, sehingga tidak berjumlah 297 juta angka Komdigi.
Isi:
- Revenue telekomunikasi 2025 sekitar USD 17-18 miliar (PwC) [1].
- Pelanggan seluler aktif Q3 2026 sekitar 297 juta menurut Komdigi (Kementerian Digital Indonesia) [2], dan sekitar 97% adalah prabayar [1].
- ARPU (rata-rata revenue bulanan per pelanggan) pada Q3 2026 adalah Rp46.000 di Indosat [4] dan Rp47.500 di XLSmart [5], dalam rupiah Indonesia.
- Secara global, orang menyimpan handset sekitar 3,5 tahun rata-rata, jauh lebih lama dari 300 hari ketika churn melonjak di data kami [6].
- Batas: Company A anonim. Indonesia hanya pasar referensi, dan hasil model tidak diklaim mewakili pelanggan Indonesia.
Footnote: [1] PwC Indonesia, Jun 2026. [2] Kompas, 13 Nov 2026 (pernyataan Komdigi). [3] Biometric Update, Nov 2026. [4] Counterpoint, Nov 2026 (Indosat). [5] Investing.com, Nov 2026 (XLSmart). [6] GSMA, Jun 2026. [7] PT Telkom Indonesia, Hasil Sembilan Bulan 2025 (Tidak Diaudit), 2025. URL lengkap di slide 15. Batas: Company A anonim. Indonesia hanya pasar referensi, dan hasil model tidak diklaim mewakili pelanggan Indonesia.

### Slide 3
Judul: Kami memprediksi pelanggan mana yang akan churn 31-60 hari setelah tanggal observasi, sehingga bisnis punya waktu bertindak sebelum hari ke-31
Komposisi: Katalog 350, kategori 08, nomor 346 (timeline page). Arketipe: navy full-bleed, satu pertanyaan di tengah, garis waktu di bawah. Alasan: slide definisi masalah harus memaksa audiens membaca satu pertanyaan bisnis sebelum melihat data.
Exhibit: Garis waktu horizontal: hari 0 (tanggal observasi, tanggal saat kami melihat tiap pelanggan; model memberi skor risiko tiap pelanggan pada hari 0), jendela tindakan (hari 0-30: bisnis bertindak), hari 31 (jendela churn dibuka), jendela churn hari 31-60 (target bernilai 1 jika pelanggan pergi di sini). Hanya jendela churn yang diberi blok emas lembut. Dua angka di bawah garis waktu: 30.000 pelanggan uji untuk akurasi dan AUC (pelanggan yang belum pernah dilihat model), 100.000 pelanggan Company A dalam data.
Isi:
- Pertanyaan bisnis: pelanggan mana yang akan churn, dan faktor apa yang bisa diubah bisnis sebelum itu terjadi?
- Sekitar 97% pelanggan adalah prabayar (PwC [1]), sehingga pelanggan mudah pindah.
- Untuk setiap pelanggan, model menjawab ya atau tidak: apakah pelanggan ini akan pergi 31-60 hari setelah tanggal observasi?
- 30.000 pelanggan uji untuk akurasi dan AUC (pelanggan yang belum pernah dilihat model).
- 100.000 pelanggan Company A dalam data.
Footnote: Definisi churn: Company A Dataset Overview [8]. AUC dijelaskan di slide 7. Nilai bisnis dihitung terpisah di slide 12.

### Slide 4
Judul: Dua batas data: churn 49,6% hanya berlaku untuk dataset ini, dan hanya 26.705 dari 100.000 baris yang lengkap
Komposisi: Katalog 350, kategori 08, nomor 344 (big number page). Arketipe: angka sangat besar 49,6% sebagai fokus, pita empat angka di atas, dua kelompok batas di bawah. Alasan: dua fakta berangka yang paling sering disalahbaca ditaruh dalam satu komposisi dengan bobot visual terbesar.
Exhibit: Angka tipografis 49,6% di panel emas lembut dengan teks navy, berjudul 'Churn di jendela 31-60 hari, hanya di dataset ini.' Dua kelompok di bawah: Limit 1: angka 49,6% (kanan) dan Limit 2: data tidak lengkap (kiri, di bawah panel emas). Pita empat angka di atas: 100.000 pelanggan, 342.969 nilai hilang, 73,3% baris dengan minimal satu nilai hilang, 26.705 baris lengkap.
Isi:
- Dua file digabung lewat Customer_ID: Client.csv (akun, perangkat, demografi) dan Record.csv (pemakaian, tagihan, kualitas panggilan, target churn).
- 342.969 nilai hilang: 73,3% baris punya minimal satu nilai hilang.
- Usia handset (eqpdays) bernilai negatif pada 133 pelanggan, sampai -5 hari: kami memperlakukannya sebagai kesalahan data.
- 49,6% pelanggan di dataset churn dalam jendela 31-60 hari setelah observasi. Angka ini hanya berlaku untuk dataset ini, dan kami tidak memakainya sebagai dasar perhitungan dampak.
- Pelanggan yang pergi dan pelanggan yang bertahan hampir seimbang. Model yang selalu menebak 'bertahan' mencapai akurasi 0,5044 (AUC 0,5000, sama seperti lempar koin). Itulah tolok ukur untuk model di slide 7.
- Komdigi menyebut churn turun dari sekitar 20% ke 2,8% pada Q3 2026 [3], tetapi definisinya tidak dipublikasikan, jadi kami tidak membandingkannya dengan 49,6% pada data kami.
- Dampak finansial dihitung dari jumlah pelanggan yang ditawari dan save rate (slide 12).
Footnote: Analisis penulis atas Client.csv dan Record.csv [8][9].

### Slide 5
Judul: Churn melonjak dari 37,4% pada handset berusia 270-300 hari menjadi 60,3% pada handset berusia 300-330 hari, selisih 22,9 poin persen
Komposisi: Katalog 350, kategori 08, nomor 349 (data chart page). Arketipe: navy full-bleed, grafik dengan warna terbalik (batang putih), blok emas lembut sebagai anotasi. Alasan: ini temuan utama, jadi diberi latar paling pekat dan satu grafik besar.
Exhibit: Batang 10 kelompok pelanggan berukuran sama menurut usia handset (eqpdays), tinggi batang adalah churn rate: 40,0%, 43,1%, 37,5%, 37,3%, 61,0%, 58,1%, 52,7%, 53,3%, 54,4%, 58,3%. Garis tegak di antara desil 4 dan 5. Kotak emas lembut: Perbesar pita usia 30 hari. 270-300 hari: 37,4%. 300-330 hari: 60,3%. Selisih: 22,9 poin persen. Label sumbu: 10 kelompok pelanggan berukuran sama, dari handset termuda ke tertua.
Isi:
- Handset lebih muda dari 300 hari: churn 39,5% (39.926 pelanggan). Handset 300 hari atau lebih: 56,3% (60.073 pelanggan).
- Bentuknya anak tangga, yang kami sebut tebing 300 hari. Setelah lompatan, churn bertahan di 52,7% sampai 61,0% pada kelompok pelanggan 5 sampai 10. Pada pita usia 30 hari yang lebih sempit, pita 330-360 hari menunjukkan 62,4%.
- Kami belum tahu penyebabnya. Lompatan setajam ini lebih mirip aturan bisnis (misalnya akhir kontrak atau hak upgrade) daripada penuaan perangkat bertahap. Ini hipotesis yang belum kami uji.
Footnote: Satu pelanggan tidak memiliki catatan usia handset, sehingga dua kelompok berjumlah 99.999, bukan 100.000 [9].

### Slide 6
Judul: Dua segmen risiko menampung 64,7% pelanggan yang pergi, dan P1 bernilai lebih tinggi (USD 78,55 per bulan)
Komposisi: Katalog 350, kategori 08, nomor 348 (matrix page). Arketipe: grafik Marimekko 65% lebar dan rel definisi 35% di kanan. Alasan: lebar kolom menunjukkan ukuran segmen dan tinggi menunjukkan churn, jadi dua dimensi terbaca sekaligus.
Exhibit: Marimekko. Lebar kolom adalah jumlah pelanggan (P1 17.117, P2 33.800, Sisanya 49.083). Tinggi adalah churn rate (63,6%, 62,5%, 35,7%). P1 emas lembut, P2 navy, Sisanya abu-abu. Revenue per bulan tertulis di kolom (USD 78,55 dan USD 45,72). Anotasi: Churn P1 hampir sama dengan P2 (63,6% vs 62,5%). Legenda: lebar kolom = jumlah pelanggan. Tinggi kolom = bagian yang churn.
Isi:
- P1: risiko tinggi (skor model 0,5 atau lebih), handset 300 hari atau lebih, revenue USD 48,20 per bulan atau lebih (mata uang diasumsikan USD). Jumlahnya 17.117 pelanggan (17,1%), churn 63,6%, dan revenue USD 78,55 per bulan.
- P2: risiko tinggi, bukan P1. Jumlahnya 33.800 pelanggan (33,8%), churn 62,5%, dan revenue USD 45,72 per bulan.
- Semua pelanggan lain (49.083), churn 35,7%.
- P1 dan P2 bersama sekitar setengah dari semua pelanggan, tetapi menampung hampir dua pertiga pelanggan yang pergi (64,7% pada data uji). P1 mulai tepat di tebing 300 hari, jadi segmen dan lompatan churn sejalan. Jumlah pelanggan memakai semua 100.000 pelanggan. Angka 64,7% diukur pada 30.000 data uji.
Footnote: Analisis penulis [9].

### Slide 7
Judul: Model terbaik kami (XGBoost) benar untuk sekitar 6 dari 10 pelanggan dan mengalahkan Random Forest dengan selisih 1,00 poin persen
Komposisi: Katalog 350, kategori 08, nomor 339 (comparison page). Arketipe: grafik titik di kiri dan kartu cara membaca di kanan. Alasan: eksekutif perlu tahu apa arti akurasi, dan grafik titik menampilkan ketidakpastian yang tidak terlihat di tabel.
Exhibit: Grafik titik akurasi untuk empat model dengan pita margin galat sekitar ±0,55 poin persen, ditambah kolom AUC berupa angka. Garis acuan pada 0,5044. Anotasi: XGBoost vs Random Forest, selisih 1,00 poin persen. Chip emas lembut: Berguna untuk memeringkatkan pelanggan, bukan untuk memastikan. Baris teks di bawah grafik mencantumkan semua skor akurasi (AUC), diikuti catatan singkat tentang alasan tiap model dipilih.
Isi:
- Akurasi (AUC): tebakan mayoritas 0,5044 (0,5000), Logistic Regression 0,5961 (0,6295), Random Forest 0,6257 (0,6785), XGBoost 0,6357 (0,6938).
- Tentang model: Logistic Regression adalah baseline sederhana yang mudah dijelaskan. XGBoost dan Random Forest menggabungkan banyak pohon keputusan dan dapat menangkap pola berbentuk tangga seperti lompatan pada 300 hari. Ketiganya dilatih pada 70.000 pelanggan yang sama dan diuji pada 30.000 pelanggan yang sama.
- Model utama: XGBoost (akurasi 0,6357, AUC 0,6938). Chip emas lembut: Berguna untuk memeringkatkan pelanggan, bukan untuk memastikan. Sekitar 6 dari 10 pelanggan diprediksi benar.
- Cara membaca AUC: AUC mengukur seberapa baik model memeringkatkan pelanggan yang kemungkinan pergi di atas pelanggan yang kemungkinan bertahan. Skor 0,5000 sama seperti lempar koin.
- Margin galat akurasi sekitar ±0,55 poin persen. Selisih dengan Random Forest 1,00 poin persen.
- Skor terkalibrasi dengan baik (kesalahan kalibrasi ECE 0,0052).
- Fitur tambahan yang kami bangun tidak membantu. Akurasi pada pemeriksaan silang internal 0,6224 dengan fitur itu dan 0,6239 tanpa, jadi kami tidak memakainya.
Footnote: Semua model memakai 30.000 data uji yang sama. Akurasi dari pemeriksaan silang internal tidak sebanding langsung dengan akurasi data uji [9].

### Slide 8
Judul: Usia handset dan lama berlangganan berperingkat pertama dan kedua pada kedua ukuran importance, sedangkan customer care berperingkat 53 dan 45
Komposisi: Katalog 350, kategori 08, nomor 342 (content with caption). Arketipe: grafik peringkat 60% di kiri, empat kartu bukti bertumpuk di kanan, dipisah garis tipis navy. Alasan: importance saja menyesatkan, jadi peringkat dan bukti arah ditaruh berdampingan.
Exhibit: Grafik titik peringkat (1 teratas): untuk tiap fitur satu titik peringkat gain dan satu titik peringkat permutation. Usia handset (gain 1, permutation 2), lama berlangganan (gain 2, permutation 1), handset refurbished atau baru (gain 3, permutation 62), panggilan suara gagal (permutation 6, gain 18), panggilan customer care (gain 53, permutation 45). Fitur yang bisa diubah bisnis (usia handset, panggilan suara gagal) berwarna emas lembut.
Isi:
- Gain: seberapa besar model mengandalkan satu fitur. Permutation: seberapa besar akurasi turun saat fitur diacak.
- Gain: usia handset (43,2) nomor 1, lama berlangganan nomor 2, dan handset refurbished atau baru (29,1) nomor 3, tetapi handset refurbished atau baru berperingkat 62 pada permutation (0,0004).
- Permutation: lama berlangganan nomor 1, usia handset nomor 2, dan panggilan suara gagal (0,0106) nomor 6, tetapi panggilan suara gagal berperingkat 18 pada gain.
- Usia handset bergerak bersama lama berlangganan (korelasi 0,483) dan harga handset (-0,478), jadi kami juga mengujinya dengan faktor terkait yang ditahan tetap. Ia tetap prediktor terkuat, dan setiap langkah khas naik melipatgandakan odds churn sebesar 1,227.
- Harga juga berpengaruh: seperempat handset termurah churn 57,5% dan seperempat termahal 41,0%.
- Panggilan customer care nyaris tidak terkait dengan churn di model kami: berperingkat 53 (gain) dan 45 (permutation). Pelanggan yang pergi lebih jarang menelepon customer care (rata-rata 1,60 panggilan vs 1,98 untuk pelanggan yang bertahan).
- Yang bisa diubah bisnis: usia handset dan kualitas panggilan (panggilan suara gagal). Lama berlangganan tidak bisa diubah bisnis.
- Nilai importance memakai satuan masing-masing dan tidak sebanding antarjenis, dan importance tidak membuktikan sebab-akibat.
Footnote: Analisis penulis [9].

### Slide 9
Judul: Proposal 1 menawarkan handset baru kepada 17.117 pelanggan bernilai tinggi yang handsetnya sudah mencapai tebing 300 hari, yang churn-nya 63,6%
Komposisi: Katalog 350, kategori 08, nomor 343 (image with caption). Arketipe: penggaris horizontal di sepertiga atas, empat blok teks di bawah, dan foto samping tinggi di kanan. Alasan: penggaris memperlihatkan bahwa ambang P1 jatuh tepat pada tebing 300 hari, sehingga pemicu dan batas segmen sama.
Exhibit: Penggaris usia handset dengan penanda 270, 300, 330, dan 360 hari. Anotasi penggaris: P1 adalah 17.117 dari 60.073 pelanggan berusia 300 hari atau lebih (yang juga berisiko 0,5 atau lebih dan revenue USD 48,20 atau lebih). Garis navy di 300 hari. Blok emas lembut di 300 hari: P1 mulai di sini. Foto samping tinggi di kanan menampilkan dua tangan menyerahkan ponsel dari satu ke yang lain, diwarnai ulang ke navy. Foto: Ron Lach / Pexels [10].
Isi:
- Sasaran: Segmen P1 (usia handset 300 hari atau lebih, skor risiko model 0,5 atau lebih, revenue USD 48,20 atau lebih). Segmen ini berjumlah 17.117 pelanggan dengan revenue USD 78,55 per bulan.
- Tindakan: tawarkan penggantian handset, lewat subsidi atau tukar tambah, sesuai nilai pelanggan.
- Bukti: usia handset tetap prediktor terkuat setelah memperhitungkan faktor terkait seperti lama berlangganan, harga handset, revenue, dan pemakaian. Churn naik 22,9 poin persen melewati 300 hari.
- Batas: korelasi belum berarti sebab, jadi mengganti handset belum tentu menghilangkan lompatan. Biaya subsidi per handset belum diestimasi. Harga handset juga berpengaruh: seperempat handset termurah churn 57,5%, seperempat termahal 41,0%.
Footnote: Analisis penulis [9].

### Slide 10
Judul: Proposal 2 mengirim tawaran retensi USD 10 kepada 50.980 pelanggan dengan peluang pergi yang sama atau lebih tinggi
Komposisi: Katalog 350, kategori 08, nomor 338 (two content). Arketipe: panel navy 40% di kiri berisi persamaan biaya, empat blok teks putih di kanan, dan foto di dalam bagian bawah panel navy. Alasan: biaya mengikuti langsung dari jumlah pelanggan, jadi ia diberi panel sendiri.
Exhibit: Persamaan biaya: 50.980 pelanggan x USD 10 per penawaran = USD 509.800. Total diberi blok emas lembut dengan teks navy. Biaya mengikuti langsung dari jumlahnya: 50.980 pelanggan x USD 10 per penawaran = USD 509.800. Biaya USD 10 per penawaran adalah asumsi biaya kampanye. Foto di dalam panel navy menampilkan wanita memakai smartphone di kafe, diwarnai ulang ke navy. Foto: Hanna Pad / Pexels [11]. Grafik dua baris reach-versus-capture mengisi ruang kosong kanan bawah: baris 1 'Pelanggan yang mendapat tawaran', 50.980 dari 100.000 (batang teal slate); baris 2 'Pelanggan yang pergi di kelompok itu (data uji)', 64,7% pelanggan yang pergi (batang navy). Keterangan: Sekitar setengah pelanggan menampung hampir dua pertiga pelanggan yang pergi.
Isi:
- Sasaran: semua 50.980 pelanggan dengan skor 0,5 atau lebih. Kelompok ini mencakup Segmen P1 dan Segmen P2 (P2: 33.800 pelanggan, churn 62,5%, revenue USD 45,72).
- Tindakan: kirim tawaran retensi senilai USD 10 ke setiap pelanggan. Nilai ini asumsi biaya kampanye.
- Bukti: skor model cocok dengan churn nyata (kesalahan kalibrasi ECE 0,0052). P1 dan P2 menampung 64,7% pelanggan yang pergi di data uji.
- Batas: save rate tidak bisa diestimasi dari data ini. Sebagian pelanggan yang mendapat tawaran memang akan bertahan. Biaya tawaran itu sudah masuk total.
- P1 dan P2 berjumlah 50.917, selisih dari 50.980 sekitar 0,1%. Ini tidak mengubah hasil.
Footnote: Biaya USD 10 per penawaran adalah asumsi berlabel [9].

### Slide 11
Judul: Setiap pelanggan diberi skor, 50.980 yang berskor 0,5 atau lebih mendapat tawaran, dan pilot dengan kelompok kontrol mengukur save rate
Komposisi: Katalog 350, kategori 08, nomor 347 (process flow page). Arketipe: alur horizontal empat langkah dengan baseline bertingkat. Alasan: urutan keputusan adalah isi slide ini, dan tangga turun ke kanan menunjukkan penyaringan.
Exhibit: Diagram alur: (1) skor risiko XGBoost untuk 100.000 pelanggan, (2) cut-off 0,5 memilih 50.980 pelanggan, (3) setiap pelanggan terpilih mendapat tawaran retensi USD 10 dan pelanggan P1 juga mendapat tawaran penggantian handset, (4) pilot dengan kelompok kontrol mengukur save rate. Blok emas lembut hanya pada langkah 4: save rate belum diketahui. Di bawah alur, empat kolom berlanjut: funnel di bawah langkah 1-2 (100.000 dinilai, 50.980 terpilih pada cut-off 0,5, 17.117 juga mendapat tawaran handset), kalimat kalibrasi, dan kartu cut-off; tile foto hampir persegi di bawah langkah 3 menampilkan pelanggan di konter toko ponsel, diwarnai ulang ke navy; diagram pilot di bawah langkah 4 membagi pelanggan terpilih menjadi kelompok yang ditawari dan kelompok kontrol (teal slate), dan membandingkan churn pada kedua kelompok menghasilkan save rate. Foto: Sami Abdullah / Pexels [12].
Isi:
- Langkah 1: model memberi skor risiko untuk setiap pelanggan. 100.000 pelanggan dinilai.
- Langkah 2: pelanggan dengan skor 0,5 atau lebih masuk daftar tawaran. 50.980 terpilih.
- Langkah 3: setiap pelanggan terpilih mendapat tawaran retensi USD 10. Pelanggan P1 (17.117) juga mendapat tawaran penggantian handset.
- Langkah 4: pilot dengan kelompok kontrol mengukur save rate, angka yang tidak bisa kami estimasi dari data ini. Save rate belum diketahui.
- Kami mulai dari 0,5 sebagai cut-off (threshold) yang hati-hati. Pada asumsi di slide 12, cut-off yang lebih rendah bisa menghasilkan lebih banyak jika save rate sama untuk semua pelanggan. Kami menetapkan cut-off akhir setelah pilot.
- Skor terkalibrasi dengan baik (ECE 0,0052), jadi skor dapat dibaca sebagai peluang churn.
Footnote: Kalibrasi dihitung pada data uji [9].

### Slide 12
Judul: Jika tawaran menahan 10% pelanggan yang akan pergi, program menghasilkan bersih USD 1.729.464 dalam 12 bulan (sebelum biaya handset dan biaya jasa)
Komposisi: Katalog 350, kategori 08, nomor 349 (data chart page). Arketipe: grafik garis selebar halaman, pita asumsi navy di bagian bawah. Alasan: asumsi harus selalu terlihat bersama hasil, jadi pita asumsi menempel pada grafik.
Exhibit: Grafik garis: sumbu x save rate, sumbu y hasil bersih (USD), untuk periode bertahan 12 bulan. Tiga titik skenario berlabel: 10% (+USD 1.729.464), 20% (+USD 3.968.727), 30% (+USD 6.207.991). Berlian emas lembut dengan garis tepi navy menandai titik impas 2,3% pada grafik. Panel impas di samping grafik mencantumkan save rate impas berdasarkan periode bertahan: 2,3% (12 bulan), 4,6% (6 bulan), 9,1% (3 bulan), dengan garis referensi navy 10% dan rumus: hasil bersih = pelanggan terselamatkan x USD 58,21 per bulan x bulan bertahan, dikurangi USD 509.800.
Isi:
- Asumsi: nilai pelanggan USD 58,21 per bulan, 50.980 pelanggan ditawari, biaya USD 10 per penawaran (total USD 509.800), dan periode bertahan 12 bulan.
- Save rate 10% memberi hasil bersih +USD 1.729.464, 20% memberi +USD 3.968.727, dan 30% memberi +USD 6.207.991.
- Impas adalah save rate 2,3% dengan masa bertahan 12 bulan. Angkanya naik menjadi 4,6% pada 6 bulan dan 9,1% pada 3 bulan.
- Data kami tidak memiliki kelompok yang menerima tawaran dan kelompok pembanding yang tidak menerima, jadi save rate tidak bisa diestimasi dari data ini. Angka 10%, 20%, dan 30% adalah skenario. Hasil ini belum termasuk biaya penggantian handset dan biaya jasa USD 144.000.
- Nilai pelanggan Company A (USD 58,21 per bulan) sekitar 23 kali revenue Indosat per pelanggan (sekitar USD 2,54 per bulan [4]), jadi angka dolar tidak langsung berlaku untuk pasar Indonesia.
Footnote: Semua angka dolar adalah asumsi berlabel [9]. Angka 49,6% dari dataset tidak dipakai di perhitungan ini.

### Slide 13
Judul: Biaya jasa tahun pertama sebagai perkiraan adalah USD 144.000: 140 hari-orang dengan USD 600 per hari, plus dukungan USD 5.000 per bulan
Komposisi: Katalog 350, kategori 08, nomor 336 (title and content). Arketipe: navy full-bleed dengan tabel biaya, total dalam blok emas lembut di kanan. Alasan: kuotasi adalah dokumen komersial, jadi tabel polos lebih tepat daripada ilustrasi.
Exhibit: Tabel empat baris: tarif harian USD 600 per hari, implementasi 140 hari-orang (USD 84.000), dukungan USD 5.000 per bulan selama 12 bulan (USD 60.000), total tahun pertama USD 144.000 (blok emas lembut). Di bawahnya daftar ruang lingkup usulan.
Isi:
- Tarif harian: USD 600 per hari.
- Implementasi: 140 hari-orang (USD 84.000).
- Dukungan: USD 5.000 per bulan selama 12 bulan (USD 60.000).
- Total tahun pertama: USD 144.000.
- Ruang lingkup usulan: pipeline skor risiko, desain pilot dengan kelompok kontrol, pengukuran save rate, dukungan operasional.
- Sebagai pembanding, skenario save rate 10% memberi hasil bersih USD 1.729.464 sebelum biaya jasa.
- Kuotasi indikatif: tarif dan hari adalah asumsi perencanaan sampai ruang lingkup disepakati.
Footnote: tidak ada. Kalimat kuotasi indikatif ada di isi.

### Slide 14
Judul: Usia handset 300 hari atau lebih adalah sinyal churn terkuat yang bisa ditindaklanjuti bisnis, dan pilot menentukan apakah program layak diskalakan
Komposisi: Katalog 350, kategori 08, nomor 337 (section title page). Arketipe: navy full-bleed dengan tiga temuan bernomor dan satu blok emas lembut berisi rekomendasi. Alasan: aturan skill meminta deck berakhir di kesimpulan.
Exhibit: tidak ada.
Isi:
- Temuan 1: churn naik 22,9 poin persen setelah handset mencapai 300 hari.
- Temuan 2: model cukup untuk memeringkatkan pelanggan menurut risiko (akurasi 0,6357, AUC 0,6938), tetapi belum bisa memastikan pelanggan mana pun.
- Temuan 3: program impas pada save rate 2,3% (periode bertahan 12 bulan), tetapi save rate belum terbukti.
- Blok emas lembut: Keputusan yang diminta: setujui pilot dengan kelompok kontrol untuk mengukur save rate, lalu tetapkan cut-off akhir.
Footnote: Semua dampak finansial adalah skenario berasumsi (slide 12).

### Slide 15
Judul: Angka pasar bersumber dari rujukan publik berikut, dan semua angka model berasal dari analisis kami atas data Company A
Komposisi: Katalog 350, kategori 08, nomor 338 (two content). Arketipe: dua kolom daftar, huruf kecil, tanpa emas lembut. Alasan: slide rujukan harus rapi dan terbaca, tanpa elemen yang bersaing dengan isi.
Exhibit: tidak ada.
Isi:
- [1] PwC Indonesia, Indonesia telecommunications sector overview and market update, Jun 2026. https://www.pwc.com/id/en/pwc-publications/industries-publications/tmt/indonesia-telecom-market-outlook.html
- [2] Kompas, Exceeding Target, 41.49 Million Users Have Registered for Biometric SIM Cards, 13 Nov 2026. https://go.kompas.com/read/2026/11/13/132446674/exceeding-target-4149-million-users-have-registered-for-biometric-sim-cards
- [3] Biometric Update, Indonesia surpasses 2026 biometric SIM target with 41M registrations, Nov 2026. https://www.biometricupdate.com/202611/indonesia-surpasses-2026-biometric-sim-target-with-41m-registrations
- [4] Counterpoint Research, Indosat Q3 2026 Revenue Grows 11.1%, Nov 2026. https://counterpointresearch.com/en/insights/indosat-q3-2026-revenue-grows
- [5] Investing.com, XLSMART Q3 2026 slides: record ARPU, integration nears completion, Nov 2026. https://www.investing.com/news/company-news/xlsmart-q3-2026-slides-record-arpu-integration-nears-completion-93CH-5034927
- [6] GSMA, Mobile Device Circularity Key Facts and Figures, Jun 2026. https://www.gsma.com/solutions-and-impact/connectivity-for-good/external-affairs/wp-content/uploads/2026/06/Mobile-Device-Circularity-Factsheet.pdf
- [7] PT Telkom Indonesia, Hasil Sembilan Bulan 2025 (Tidak Diaudit), 2025. https://aro.telkom.co.id/minio/show/data/lampiran/1761838522183_original_TLKM-9M25-Info-Memo.pdf
- [8] GCI World 2026, Company A Dataset Overview dan tutorial notebook.
- [9] Analisis penulis atas Client.csv dan Record.csv (notebook terlampir).
- [10] Ron Lach, Two people exchanging a green mobile phone against a solid green background, Pexels, 4 Okt 2021. https://www.pexels.com/photo/9786072/. Foto dua tangan menyerahkan ponsel dari satu ke yang lain, diwarnai ulang ke navy, slide 9.
- [11] Hanna Pad, Woman Using Mobile Phone, Pexels, 18 Apr 2021. https://www.pexels.com/photo/woman-using-mobile-phone-7550823/. Foto wanita memakai smartphone di kafe, diwarnai ulang ke navy, slide 10.
- [12] Sami Abdullah, A customer examines smartphones in a modern Istanbul gadget store, Pexels, 24 Jul 2022. https://www.pexels.com/photo/12968298/. Foto pelanggan di konter toko ponsel, diwarnai ulang ke navy, slide 11.
- [13] Väinö Parjanen, Antenna Tower Under the Blue Sky, Pexels, 5 Aug 2021. https://www.pexels.com/photo/9073180/. Foto sampul, dipotong dan diwarnai ulang menjadi duotone navy (#14467C ke putih).
- Alat AI generatif dipakai untuk diskusi dan penyusunan. URL riwayat chat: https://app.kiro.dev/session/dff20d50-6c54-498c-aabe-d83d6b1b1d6b.
Footnote: Kutipan langsung membentuk kurang dari 40% dari teks slide.
