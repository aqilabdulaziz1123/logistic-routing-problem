## Aqil abdul aziz / 13518002

1. Algoritma pathfinding yang saya gunakan adalah gbfs dengan mengambil next step yang lebih dekat dengan tujuan secara garis lurus, sedangkan untuk mTsp, saya menggunakan greedy, dengan langkah sebagai berikut,
    1. Kurir 1 cek paling murah kemana, anggap kota X
    2. Cek apakah ada kurir Y lain yang lebih murah dari posisi mereka ke X
    3. Jika ada, kurir 1 tidak diberangkatkan, namun kurir Y
    4. Lanjut mengecek langkah untuk kurir selanjutnya setiap suatu rute sudah ditetapkan, terus sehingga semua kota pelanggan sudah dikunjungi
    5. ketika semua sudah mencapai rumah pelanggan, semua pun mencari jalan pulang

2. Tidak perlu menginstall apa apa, library yang digunakan untuk visualisasi tersedia di graphics.py, courtesy of https://mcsp.wartburg.edu/zelle/python/graphics, cukup run py main.py dan input sesuai instruksi