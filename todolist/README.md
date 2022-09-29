Caroline Esther (2106751915)

Tautan aplikasi Heroku: [https://tugas-2-caroline.herokuapp.com/todolist/](https://tugas-2-caroline.herokuapp.com/todolist/)

- Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
    
    `{% csrf_token %}` adalah tag yang digunakan untuk menghindari serangan CSRF. Tag ini akan menghasilkan token acak di sisi server saat melakukan rendering pada page dan memastikan untuk melakukan pemeriksaan ulang token untuk setiap request yang datang kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. Token sifatnya unik per sesi user dan terdiri dari value acak yang panjang agar sulit ditebak.
    
    CSRF atau Cross-Site Request Forgery sendiri adalah serangan yang memaksa user yang diautentikasi untuk mengirimkan request ke aplikasi Web yang saat ini diautentikasi. Serangan CSRF mengeksploitasi kepercayaan yang dimiliki aplikasi Web pada user yang diautentikasi. Serangan CSRF mengeksploitasi kerentanan dalam aplikasi Web jika tidak dapat membedakan antara permintaan yang dihasilkan oleh user secara individu dan permintaan yang dibuat oleh pengguna tanpa persetujuan mereka.
    
    Jika potongan kode tersebut tidak ada, maka akan terdapat kemungkinan user atau situs web yang berniat jahat membuat user yang tidak curiga atau rentan melakukan sesuatu yang tidak mereka inginkan.

    
- Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan *generator* seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
    
    Kita dapat membuat elemen `<form>` secara manual tanpa menggunakan generator seperti `{{ form.as_table }}`. Secara garis umum, kita dapat men-generate table untuk menjadi struktur dari form dengan bantuan `<tr>` dan `<td>`. Kemudian, input dapat kita masukkan dengan `<input>`. Setelah itu, kita dapat membuat sebuah button untuk membantu submisi dengan mengubah atribut `type=` menjadi `submit`.
    

- Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada *database*, hingga munculnya data yang telah disimpan pada *template* HTML.

    Pertama-tama, pengguna akan melakukan submisi melalui HTML form. Setelah pengguna menekan button submit, HTTP request akan dikirimkan dan server akan menerima data. Kemudian, request tersebut akan diperiksa validitasnya. Jika valid, maka program akan menyesuaikan dengan views yang ada. Views akan mengirimkan HTTP response dan laman HTML yang sesuai pada pengguna.

- Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.
    
    Pertama-tama, nyalakan virtual environment. Untuk membuat suatu aplikasi baru bernama todolist, gunakan perintah “python manage.py startapp todolist”. Kemudian, tambahkan todolist pada variable installed apps di folder project_django dan akan muncul folder todolist. Di dalam folder tersebut, isi file models.py  dengan class yang berisi models yang pada konteks aplikasi ini adalah user, date, title, description, dan is_finished. Setelah itu, lakukan migrasi.
    
    Berikutnya, buka file views.py di folder todolist dan buat fungsi-fungsi views yang dibutuhkan. Pada tugas ini, terdapat fungsi show_todolist untuk menampilkan todolist, register untuk mengatasi register pengguna, login_user untuk mengatasi kegiatan login pengguna, logout_user untuk mengatasi kegiatan logout pengguna, create_task untuk mengatasi pembuatan task oleh pengguna, ubah_status untuk mengatasi pengubahan status task, dan hapus_status untuk menghapus task. Buat juga sebuah folder bernama templates di dalam folder todolist yang isinya adalah file-file HTML yang diisi dengan data yang diperlukan. Tugas 4 ini membutuhkan empat file HTML yang mengatasi pembuatan task, login, register, dan todolist. Pada keempat file HTML ini, dibuat element-element pada form seperti tombol, header, dan lainnya. Terutama pada file todolist.html, ditampilkan username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
    
    Setelah itu, buat sebuah file di dalam folder todolist bernama urls.py yang akan digunakan untuk melakukan routing terhadap fungsi views sehingga halaman HTML dapat ditampilkan melalui browser. Daftarkan routing sesuai dengan perintah soal. Path dari aplikasi tersebut juga harus didaftarkan ke variable urlpatterns pada folder project_django. 
    
    Untuk membuat form registrasi, login, dan logout, pada file views.py yang ada di folder todolist, impor redirect, UserCreationForm, messages, authenticate, login, dan logout. Kemudian, tambahkan fungsi register, login_user, dan logout_user untuk menghandle ketiga hal tersebut. Isi juga file HTML  yang dibuat sebelumnya sesuai dengan fungsi yang ada. Setelah itu, impor fungsi yang sudah dibuat pada file urls.py dan tambahkan path url ke urlpatterns untuk mengakses fungsi yang sudah diimpor. Untuk merestriksi akses halaman todolist, pada file views.py, impor login_required dan tambahkan kode “@login_required(login_url='/wishlist/login/')” tepat di atas fungsi show_todolist.
    
    Selanjutnya, untuk melakukan deployment ke Heroku, karena sudah termasuk ke aplikasi Heroku pada tugas sebelumnya, aplikasi sudah di-deploy secara otomatis. Aplikasi dapat langsung diakses dengan membuka link yang disediakan dengan tambahan “todolist/” di paling kanan url.
    
    Untuk membuat akun pengguna, klik daftar akun yang akan langsung menghubungkan ke form registrasi. Setelah registrasi berhasil, tampilan form login akan terbuka dan pengguna bisa melakukan input username beserta password yang sudah didaftarkan. Jika sudah masuk ke laman todolist, tambahkan task dengan menekan tombol yang ada dan isi task beserta deskripsinya pada form yang tersedia. Setelah menambahkan task, pengguna dapat langsung melihat task tersebut dan pengguna juga dapat mengubah status atau menghapus task.
    

Referensi:

- [https://www.educative.io/answers/what-is-a-csrf-token-in-django](https://www.educative.io/answers/what-is-a-csrf-token-in-django)
- [https://www.synopsys.com/glossary/what-is-csrf.html](https://www.synopsys.com/glossary/what-is-csrf.html)
- [https://edikartono.com/django/belajar-membuat-forms-django](https://edikartono.com/django/belajar-membuat-forms-django)