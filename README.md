# 🫁 Phát Hiện Viêm Phổi Từ Ảnh X-quang Phổi

## Course Project – Digital Image Processing

---

## 📌 1. Giới thiệu

Viêm phổi là bệnh nguy hiểm, gây tử vong cao nếu không được phát hiện sớm. Phân tích ảnh X-quang (Chest X-ray – CXR) là một trong những phương pháp phổ biến giúp chẩn đoán viêm phổi.  

Dự án này xây dựng hệ thống **phân loại ảnh X-quang thành 2 nhóm:**
- **NORMAL** – Phổi bình thường  
- **PNEUMONIA** – Có dấu hiệu viêm phổi  

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

## 🧠 5. Huấn luyện mô hình

### 5.1 Chuẩn bị dữ liệu

Trước khi huấn luyện, cần chạy các notebook tiền xử lý:

```bash
jupyter nbconvert --to notebook --execute src/preprocess/download_and_preprocess.ipynb

jupyter nbconvert --to notebook --execute src/preprocess/split_dataset.ipynb
```

### 5.2 Huấn luyện trên Google Colab (Khuyến nghị)

Do yêu cầu GPU, khuyến nghị sử dụng Google Colab để huấn luyện:

1. Upload notebook lên Google Colab
2. Chọn Runtime > Change runtime type > GPU (T4)
3. Chạy toàn bộ notebook

### 5.3 Các mô hình

#### CNN tự xây dựng
- **Notebook:** `src/model/cnn.ipynb`
- **Cấu trúc:** 4 Conv blocks + 2 FC layers
- **Hyperparameters:**
  - Batch size: 32
  - Learning rate: 0.001
  - Epochs: 50 (early stopping patience: 10)
- **Input:** Grayscale 224x224

```bash
jupyter nbconvert --to notebook --execute src/model/cnn.ipynb
```

#### ResNet18 (Fine-tuning)
- **Notebook:** `src/model/resnet18_finetune_eval.ipynb`
- **Phương pháp:** Transfer learning 2 phase
  - Phase 1: Freeze backbone, train FC (5 epochs, lr=1e-3)
  - Phase 2: Unfreeze layer4 + FC (5 epochs, lr=1e-4)
- **Input:** RGB 224x224 (ImageNet normalization)

```bash
jupyter nbconvert --to notebook --execute src/model/resnet18_finetune_eval.ipynb
```

#### MobileNetV3-Large (Fine-tuning)
- **Notebook:** `src/model/mobilenetv3.ipynb`
- **Phương pháp:** Freeze 10 layers đầu, train phần còn lại
- **Hyperparameters:**
  - Batch size: 32
  - Backbone LR: 1e-4, Classifier LR: 1e-3
  - Epochs: 50 (early stopping patience: 7)
- **Input:** RGB 224x224 (ImageNet normalization)

```bash
jupyter nbconvert --to notebook --execute src/model/mobilenetv3.ipynb
```

### 5.4 Kết quả huấn luyện

| Model | Val Accuracy | Training Time |
|-------|--------------|---------------|
| CNN | ~96% | ~12 phút |
| ResNet18 | ~97% | ~10 phút |
| MobileNetV3 | ~97% | ~5 phút |

### 5.5 Model Output

Model được lưu tại thư mục **`models/`**:
- `cnn_best.pth` - CNN model
- `resnet18_best.pth` - ResNet18 model
- `mobilenetv3_best.pth` - MobileNetV3 model

---

## 🖼 6. Demo dự đoán viêm phổi

Từ thư mục gốc, di chuyển vào thư mục src\app:
- cd src/app

Chạy app:
```
streamlit run app.py
```

Chức năng:

* Upload ảnh X-quang phổi
* Dự đoán NORMAL / PNEUMONIA
* Hiển thị xác suất

---

