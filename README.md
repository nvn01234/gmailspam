### Bước 1

Tạo db `gmail` và chạy `extracted.sql`

import `extracted.json` sau khi extract feature vào bảng `extracted`

(Navicat có thể import được json)

### Bước 2
 
Cài các gói pip:
    
        $ pip install -r requirements.txt
        
### Bước 3
 
Lần lượt chạy các URL sau (đợi URL này hoàn thành mới được chạy URL tiếp)

- [detect ngôn ngữ](http://localhost:8000/detect)

- [tokenize](http://localhost:8000/tokenize)

