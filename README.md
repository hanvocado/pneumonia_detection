# 🫁 Phát Hiện Viêm Phổi Từ Ảnh X-quang Bằng CNN & ResNet

## Course Project – Digital Image Processing / Deep Learning

---

## 📌 1. Giới thiệu

Viêm phổi là bệnh nguy hiểm, gây tử vong cao nếu không được phát hiện sớm. Phân tích ảnh X-quang (Chest X-ray – CXR) là một trong những phương pháp phổ biến giúp chẩn đoán viêm phổi.  

Dự án này xây dựng hệ thống **phân loại ảnh X-quang thành 2 nhóm:**
- **NORMAL** – Phổi bình thường  
- **PNEUMONIA** – Có dấu hiệu viêm phổi  

Nhóm sử dụng 2 mô hình:
- **CNN**  
- **ResNet18**  

Dataset: **Chest X-Ray Pneumonia** trên Kaggle  
Link: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

---

## 📁 2. Cấu trúc thư mục

```
pneumonia-detection/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│ ├── train/
│ ├── val/
│ └── test/
│
├── src/
│ ├── preprocess/
│ ├── model/
│ ├── app/
│ └── utils/
│
├── models/            
```

---

## 🧪 3. Cài đặt môi trường

- Activate venv

```bash
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS, Linux
```

- Install libraries

```
pip install -r requirements.txt
```


---

## 🛠️ 4. Quy trình tiền xử lý (Preprocessing Pipeline)

### Bấm run all trong `src/preprocess/download_and_preprocess.ipynb` để tải và tiền xử lý ảnh.

### Bấm run all trong `src/preprocess/split_dataset.ipynb` để tăng cường dữ liệu và split dataset.

---

## 🧠 5. Mô hình sử dụng

### 🔷 CNN tự xây dựng

* 3 convolution blocks
* BatchNorm + ReLU
* MaxPooling
* Dropout + Fully-connected

### 🔶 ResNet18 (Fine-tuning)

* Pretrained (ImageNet)
* Freeze một số layer
* Thay FC cuối thành binary classifier

---

## 🚀 6. Huấn luyện mô hình

### ▶ Train CNN

```
python 
```

### ▶ Train ResNet

```
python 
```

Model lưu tại: **/models**

---

## 📊 7. Đánh giá mô hình

```
python 
```

Gồm:

* Accuracy
* Precision / Recall / F1
* Confusion Matrix
* ROC Curve

Kết quả dự kiến:

| Model    | Accuracy | F1-score |
| -------- | -------- | -------- |
| CNN      |          |          |
| ResNet18 |          |          |

---

## 🖼 8. Demo dự đoán ảnh

Chạy app:

```
python
```

Chức năng:

* Upload ảnh X-ray
* Dự đoán NORMAL / PNEUMONIA
* Hiển thị xác suất

---

