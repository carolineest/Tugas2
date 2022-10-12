Caroline Esther (2106751915)

#Tugas 6

##Jelaskan perbedaan antara *asynchronous programming* dengan *synchronous programming.*

*Asynchronous programming* merupakan pendekatan yang tidak terikat pada protokol input maupun output. Pada pendekatan pemrograman ini, proses jalannya program tidak harus terikat dengan proses lain atau dapat berjalan secara independen. Pengguna dapat terus berinteraksi dengan laman ketika data dimuat. Sedangkan pada *synchronous programming*, proses akan dieksekusi satu persatu sesuai dengan urutan dan prioritas *task*. Pada pendekatan ini, pengguna harus menunggu ketika laman dimuat.

##Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma *Event-Driven Programming*. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

*Event-Driven Programming* adalah paradigma pemrograman yang alurnya ditentukan oleh suatu *event* yang merupakan keluaran/tindakan yang dilakukan pengguna atau berupa pesan dari program lainnya. Pada tugas ini, salah satu contoh penerapannya adalah *mouse* *event* *click* di `todolist.html` ketika ingin menghapus *task* dengan men-*click* button `Delete Task`

##Jelaskan penerapan *asynchronous programming* pada AJAX.
Asynchronous JavaScript and XML (AJAX) adalah salah satu konsep yang menerapkan metode *asynchronous programming* dalam menjalankan pekerjaannya. AJAX merupakan teknik yang memungkinkan halaman web diperbarui secara *asynchronous*, yang berarti bahwa *browser* tidak perlu memuat ulang seluruh halaman ketika hanya sedikit data pada halaman yang berubah. AJAX hanya meneruskan informasi yang diperbarui ke dan dari server. Biasa nya AJAX digunakan untuk melakukan permintaan data (*request*) dan menangani sebuah tanggapan (*handling response*), baik *response* dalam bentuk XML, Javascript maupun JSON dari sebuah Rest API. 

##Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas.
1. Membuat dua fungsi baru pada file `views.py` yang akan mengatasi penambahan dan penghapusan *task* yang mengembalikan data *task* dalam bentuk JSON.
2. Menambahkan path `/todolist/json` dan `/todolist/add` pada *file* `urls.py` yang mengarah ke *view* pada poin 1.
3. Membuat fungsi yang berisi pengimplementasian AJAX GET pada *file* `todolist.html`.
4. Membuat tombol `Add Task` yang akan membuka sebuah modal dengan form untuk menambahkan task pada file `todolist.html`. Kemudian, membuat fungsi yang berisi pengimplementasian AJAX POST untuk menambahkan task baru tersebut. List terbaru setelah ditambah task baru akan secara *asynchronous* ditampilkan.


###Referensi
- https://binus.ac.id/malang/2022/05/asynchronous-vs-synchronous-programming/
- http://www.myspsolution.com/news-events/solace-event-driven/
- https://www.dicoding.com/blog/mengenal-fungsi-asynchronous-request-pada-javascript/
- https://www.thoughtco.com/use-asynchronous-or-synchronous-ajax-2037228#:~:text=AJAX%2C%20which%20stands%20for%20asynchronous,to%20and%20from%20the%20server.