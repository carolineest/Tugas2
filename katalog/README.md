Link aplikasi Heroku: https://tugas2-caroline.herokuapp.com/katalog/

- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut 
  kaitan antara urls.py, views.py, models.py, dan berkas html;
  
  Bagan: https://github.com/carolineest/Tugas2/issues/1#issue-1373477117
  
  Pada server Django, awalnya request yang masuk akan diproses melalui urls. Request kemudian akan diteruskan ke views yang 
  memproses permintaan tersebut. Views tersebut sebelumnya sudah didefinisikan oleh developer. Jika terdapat proses yang 
  memerlukan keterlibatan database, maka views akan memanggil query ke models yang kemudian akan melakukan transaksi data 
  dengan database. Selanjutnya, database akan mengembalikan hasil query tersebut ke views. Hasil proses tersebut akan 
  dipetakan ke HTML yang sudah ditentukan setelah request selesai diproses dan HTML akan dikembalikan ke user sebagai respons.
  
- Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa 
  menggunakan virtual environment?
  
  Virtual environment adalah tools untuk membuat lingkungan virtual python yang tertutup dan tidak bisa diakses secara 
  sembarangan. Program python yang berjalan di dalam virtual environment ini memiliki modul-modulnya sendiri, sehingga 
  program dari luar tidak dapat mengaksesnya. Virtual environment memungkinkan penggunaan dependencies yang berbeda-beda 
  antara proyek satu dengan yang lainnya yang berjalan pada satu sistem operasi yang sama. Tanpa menggunakan virtual 
  environment, kita tetap bisa membuat aplikasi web berbasis Django.
  
- Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

  Sebelum memulai pengimplementasian, masuk ke dalam repositori yang sudah di-clone di komputer, kemudian buat dan nyalakan 
  virtual environment. Untuk membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari 
  model dan dikembalikan ke dalam sebuah HTML, buka views.py yang ada pada folder katalog dan buat sebuah fungsi yang menerima 
  parameter request dan mengembalikan render(request, "katalog.html"). Kemudian, pada folder bernama templates di dalam folder 
  aplikasi katalog, modifikasi isi dari berkas katalog.html dengan menambahkan ID dan isi table.

  Selanjutnya, untuk melakukan routing, pada berkas bernama urls.py yang ada di dalam folder aplikasi katalog, 
  import path dari django.urls dan show_katalog, buat variable bernama app_name dengan value nama aplikasinya, dan buat variable 
  yang isinya path show_katalog. Kemudian, daftarkan aplikasi katalog ke urls.py yang ada pada folder project_django. 

  Pada fungsi views yang sudah ada sebelumnya, import models ke dalam berkas views.py. Kemudian, panggil fungsi query ke model 
  database dan simpan hasil query tersebut ke dalam sebuah variable. Tambahkan pula variable tersebut ke parameter pada pengembalian 
  fungsi render yang sudah ada. Selanjutnya, buka file HTML pada folder template di dalam folder katalog. Modifikasi isi berkas 
  tersebut dengan menambahkan data yang diperlukan. Terakhir, lakukan iterasi terhadap variable list_barang yang telah di-render ke 
  dalam HTML untuk menampilkan daftar barang ke dalam tabel. Untuk memeriksa data di halaman web, jalankan proyek Django tersebut dan 
  buka di browser.

  Untuk melakukan deployment ke Heroku, buka konfigurasi repositori GitHub dan buat dua action secrets yang isinya API key yang 
  didapatkan dari Heroku dan nama aplikasi heroku yang dibuat. Kemudian, buka Heroku dan hubungkan ke GitHub dengan memilih method 
  deployment GitHub. Terakhir, sesuaikan nama aplikasi yang dibuat dan pengaturan yang ada.
