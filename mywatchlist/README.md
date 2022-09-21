Tautan aplikasi Heroku: https://tugas-3-caroline.herokuapp.com/mywatchlist/


1. Jelaskan perbedaan antara JSON, XML, dan HTML!

Perbedaan utama dari JSON, XML, dan HTML adalah HTML digunakan untuk membuat struktur teks pada laman web yang kemudian di-render ke browser, 
XML umumnya digunakan untuk membuat struktur data atau pesan, dan JSON digunakan untuk merepresentasikan data sebagai pasangan key-value yang
dapat dengan mudah dikonversikan dari atau menjadi obyek JavaScript. 

HTML (HyperText Markup Languange) berfokus pada pembuatan struktur, bukan menata teks. Artinya, HTML akan menandai bagian mana dari laman yang
merupakan judul, heading, paragraf, dan lainnya yang akan di-render ke web browser. HTML juga memiliki seperangkat tag yang sudah disediakan
sebelumnya yang dapat digunakan untuk berbagai tujuan.

Sama seperti HTML, XML (Extensible Markup Language) merupakan sebuah markup languange. Namun, XML digunakan untuk menyimpan dan men-transport
data. Pada umumnya, XML digunakan untuk mengirim data terstruktur dalam sistem berbasis web.

JSON (JavaScript Object Notation) sebenarnya adalah format lain yang dapat digunakan untuk menyimpan dan men-transport data. Tetapi, perbedaan
yang dapat dilihat dengan jelas adalah JSON dapat dengan mudah dikonversikan menjadi obyek JavaScript dan sebaliknya.


2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan dalam pengimplementasian sebuah platform karena kegiatan delivery tersebut akan menghubungkan browser dengan file/data yang di-request. Pada umumnya, browser akan melakukan request dan kemudian server akan me-return. Namun, dalam beberapa konteks tertentu, ada juga
data delivery yang file-nya tidak disimpan di server, namun di-generate oleh kode program.


3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Untuk membuat suatu aplikasi baru bernama mywatchlist, gunakan perintah “python manage.py startapp wishlist”. Kemudian, tambahkan mywatchlist pada
variable installed apps di folder project_django. Akan muncul folder mywatchlist, kemudian isi file models.py di dalam folder tersebut dengan class yang berisi komponen dari laman mywatchlist. Setelah itu, lakukan migrasi dan tambahkan sebuah folder json yang isinya data dari komponen pada laman mywatchlist, juga masukkan data tersebut ke dalam database Django lokal.

Kemudian, buka file views.py di folder mywatchlist dan buat sebuah fungsi yang menerima parameter request dan mengembalikan render. Buat juga
sebuah folder bernama templates di dalam folder mywatchlist dan isifolder tersebut dengan sebuah file html yang diisi dengan data yang diperlukan.
Setelah itu, buat sebuah file di dalam folder mywatchlist yang akan digunakan untuk melakukan routing terhadap fungsi views sehingga halaman HTML
dapat ditampilkan melalui browser. Path dari aplikasi tersebut juga harus didaftarkan ke variable urlpatterns pada folder project_django.

Untuk menghubungkan models dengan views dan template, import models yang sudah dibuat ke dalam file views.py, kemudian panggil fungsi query ke
model database dan simpan hasil query tersebut ke dalam sebuah variable. Selanjutnya, untuk melakukan mapping, lakukan iterasi terhadap variable
dari data.

Untuk mengembalikan data dalam bentuk XML, JSON, dan HTTP, buat fungsi yang menerima parameter request pada file views.py, kemudian impor
HttpResponse dan Serializer. Selanjutnya, buat sebuah variable yang akan menyimpan hasil query dari seluruh data. Tambahkan juga return berupa
HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON/XML dan parameter content type-nya. Selanjutnya, impor
fungsi yang sudah dibuat ke file urls.py dan tambahkan path url tersebut ke dalam variable urlpatterns.

Untuk melakukan deployment ke Heroku, buka konfigurasi repositori GitHub dan buat dua action secrets yang isinya API key yang didapatkan dari
Heroku dan nama aplikasi Heroku yang dibuat. Kemudian, buka Heroku dan hubungkan ke GitHub dengan memilih method deployment GitHub. Terakhir,
sesuaikan nama aplikasi yang dibuat dan pengaturan yang ada.


<<<<<<< HEAD
Tangkapan layar Postman: https://github.com/carolineest/Tugas2/issues/2#issue-1381104194
=======
Tangkapan layar Postman: https://github.com/carolineest/Tugas2/issues/2#issue-1381104194
>>>>>>> 38482d3b5771c52eafd5714350537d3114c95286
