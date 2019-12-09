# Welcome to the colorize-black-and-white-image wiki!
Thông thường, ảnh chỉ được chỉnh màu bằng tay bởi các công cụ hỗ trợ photoshop. Chúng gần như không thể thực hiện với số lượng ảnh lớn. Chúng tôi mong rằng dự án > colorize-black-and-white-image có thể tự động tô màu ảnh đen trắng với độ chính xác cao và giống với ảnh màu gốc.
Một số ứng dụng:
* Ứng dụng trong việc tô màu, khôi phục các ảnh cũ
* Ứng dụng trong việc truyền ảnh, giảm dung lượng truyền nếu chỉ cần truyền ảnh đen trắng và đến đích mới tô màu...

## Hướng dẫn cài đặt
1. Thiết lập môi trường
2. Training model
3. Running Test
### 1. Thiết lập môi trường

   Chúng tôi sử dụng gói [Anaconda](https://www.anaconda.com/download/) để cài đặt môi trường cho dự án Colorize.
Để cài đặt môi trường [Tensorflow](https://www.tensorflow.org/tutorials/), mở Anaconda Prompt nhập dòng lệnh:

`(base) C:\Users\MyPC> conda create -n tensorflow1 pip python=3.5`

Sau đó kích hoạt môi trường:

`(base) C:\Users\MyPC> activate tensorflow1`

`       (tensorflow1) C:\Users\MyPC>pip install --ignore-installed --upgrade tensorflow`

và cài đặt thêm một số gói tiện ích khác dưới đây:

`(tensorflow1) C:\> pip install pillow`

`(tensorflow1) C:\> pip install jupyter`

`(tensorflow1) C:\> pip install matplotlib`

`(tensorflow1) C:\> pip install opencv-python`

`(tensorflow1) C:\> pip install Flask`

`(tensorflow1) C:\> pip install Keras`

`(tensorflow1) C:\> pip install scikit-image`

### 2. Training model
Chúng tôi cung cấp sẵn một số model đã được training, tuy nhiên khuyến khích các bạn tự training cho dự án của các bạn.
Bạn có thể tải model tại [Training Model](https://drive.google.com/file/d/1kE0oIXP5UruXEkhA2WAp7T74MHr4BuKo/view?usp=sharing) 
Hoặc chạy thử với tập dữ liệu mẫu của riêng bạn

### 3. Running Test
Sau khi kích hoạt môi trường Tensorflow thực hiện test như sau

Bước 1: Clone Project bằng lệnh:

`git clone https://github.com/nguyenthithuy97/colorize-black-and-white-image.git`

Bước 2: Trỏ vào thư mục chính của project tử Anaconda Prompt

`(tensorflow1) C:\> cd C:\Users\MyPC\Desktop\colorize-black-and-white-image`

Bước 3: Chạy test.py

`(tensorflow1) C:\Users\MyPC\Desktop\colorize-black-and-white-image> python test.py`

Màn hình hiển thị yêu cầu nhập tên ảnh trong thư mục images, Kết quả:

![result ](https://www.dropbox.com/s/49t5nqaf7fo1h05/rose.PNG?dl=0)
