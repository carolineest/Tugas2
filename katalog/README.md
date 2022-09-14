Link aplikasi Heroku: https://tugas2-caroline.herokuapp.com/katalog/

- Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut 
  kaitan antara urls.py, views.py, models.py, dan berkas html;
  
  Bagan: https://github.com/carolineest/Tugas2/issues/1#issue-1373477117
  
  Pada server Django, awalnya _request_ yang masuk akan diproses melalui urls. _Request_ kemudian akan diteruskan ke views yang 
  memproses permintaan tersebut. Views tersebut sebelumnya sudah didefinisikan oleh _developer_. Jika terdapat proses yang 
  memerlukan keterlibatan _database_, maka views akan memanggil _query_ ke models yang kemudian akan melakukan transaksi data 
  dengan _database_. Selanjutnya, _database_ akan mengembalikan hasil _query_ tersebut ke views. Hasil proses tersebut akan 
  dipetakan ke HTML yang sudah ditentukan setelah _request_ selesai diproses dan HTML akan dikembalikan ke user sebagai respons.
  
- Jelaskan kenapa menggunakan _virtual environment_? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa 
  menggunakan _virtual environment_?
  
  _Virtual environment_ adalah _tools_ untuk membuat lingkungan virtual python yang tertutup dan tidak bisa diakses secara 
  sembarangan. Program python yang berjalan di dalam _virtual environment_ ini memiliki modul-modulnya sendiri, sehingga 
  program dari luar tidak dapat mengaksesnya. _Virtual environment_ memungkinkan penggunaan _dependencies_ yang berbeda-beda 
  antara proyek satu dengan yang lainnya yang berjalan pada satu sistem operasi yang sama. Tanpa menggunakan _virtual 
  environment_, kita tetap bisa membuat aplikasi web berbasis Django.
  
- Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

  Sebelum memulai pengimplementasian, masuk ke dalam repositori yang sudah di-_clone_ di komputer, kemudian buat dan nyalakan 
  _virtual environment_. Untuk membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari 
  model dan dikembalikan ke dalam sebuah HTML, buka views.py yang ada pada folder katalog dan buat sebuah fungsi yang menerima 
  parameter request dan mengembalikan render(request, "katalog.html"). Kemudian, pada folder bernama templates di dalam folder 
  aplikasi katalog, modifikasi isi dari berkas katalog.html dengan menambahkan ID dan isi tabel.

  Selanjutnya, untuk melakukan _routing_, pada berkas bernama urls.py yang ada di dalam folder aplikasi katalog, 
  _import_ path dari django.urls dan show_katalog, buat _variable_ bernama app_name dengan _value_ nama aplikasinya, dan buat _variable_ 
  yang isinya path show_katalog. Kemudian, daftarkan aplikasi katalog ke urls.py yang ada pada folder project_django. 

  Pada fungsi views yang sudah ada sebelumnya, _import_ models ke dalam berkas views.py. Kemudian, panggil fungsi _query_ ke _model 
  database_ dan simpan hasil _query_ tersebut ke dalam sebuah _variable_. Tambahkan pula _variable_ tersebut ke parameter pada pengembalian 
  fungsi render yang sudah ada. Selanjutnya, buka file HTML pada folder template di dalam folder katalog. Modifikasi isi berkas 
  tersebut dengan menambahkan data yang diperlukan. Terakhir, lakukan iterasi terhadap _variable_ list_barang yang telah di-_render_ ke 
  dalam HTML untuk menampilkan daftar barang ke dalam tabel. Untuk memeriksa data di halaman web, jalankan proyek Django tersebut dan 
  buka di _browser_.

  Untuk melakukan _deployment_ ke Heroku, buka konfigurasi repositori GitHub dan buat dua _action secrets_ yang isinya API key yang 
  didapatkan dari Heroku dan nama aplikasi Heroku yang dibuat. Kemudian, buka Heroku dan hubungkan ke GitHub dengan memilih _method 
  deployment_ GitHub. Terakhir, sesuaikan nama aplikasi yang dibuat dan pengaturan yang ada.
