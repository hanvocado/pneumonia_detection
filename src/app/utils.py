import streamlit as st
import torch
import cv2
import numpy as np
from torchvision import transforms
from models import BasicCNN, get_resnet_model # Import từ file models.py

# ==========================================
# HÀM LOAD MODELS (VỚI CACHE)
# ==========================================
@st.cache_resource
def load_models():
    device = torch.device("cpu")
    
    # Load CNN
    cnn = BasicCNN()
    cnn_path = "../../../models/cnn_best.pth" #  Đảm bảo đường dẫn đúng
    try:
        cnn.load_state_dict(torch.load(cnn_path, map_location=device))
        cnn.eval()
        status_cnn = {"status": "success", "msg": "CNN đã sẵn sàng"}
    except Exception as e:
        cnn = None
        status_cnn = {"status": "error", "msg": f"Lỗi: {str(e)[:50]}..."}
    
    # Load ResNet
    resnet = get_resnet_model()
    resnet_path = "../../../models/resnet18_best.pth" #  Đảm bảo đường dẫn đúng
    try:
        resnet.load_state_dict(torch.load(resnet_path, map_location=device))
        resnet.eval()
        status_resnet = {"status": "success", "msg": "ResNet18 đã sẵn sàng"}
    except Exception as e:
        resnet = None
        status_resnet = {"status": "error", "msg": f"Lỗi: {str(e)[:50]}..."}
        
    return cnn, resnet, status_cnn, status_resnet

# ==========================================
# TIỀN XỬ LÝ ẢNH
# ==========================================
def preprocess_image_exact(image_pil, model_type):
    image_np = np.array(image_pil)
    image_resized = cv2.resize(image_np, (224, 224))
    
    if len(image_resized.shape) == 3:
        image_gray = cv2.cvtColor(image_resized, cv2.COLOR_RGB2GRAY)
    else:
        image_gray = image_resized
    
    alpha_contrast = 2.5
    beta_brightness = -180
    image_float = image_gray.astype(np.float32)
    image_adjusted = cv2.convertScaleAbs(image_float, alpha=alpha_contrast, beta=beta_brightness)
    
    gamma = 1
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(256)]).astype("uint8")
    image_enhanced = cv2.LUT(image_adjusted, table)
    ai_view_img = image_enhanced
    
    if model_type == 'cnn':
        img_tensor = transforms.ToTensor()(image_enhanced)
    else:
        img_rgb_simulated = cv2.merge([image_enhanced, image_enhanced, image_enhanced])
        transform_resnet = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        img_tensor = transform_resnet(img_rgb_simulated)

    return img_tensor.unsqueeze(0), ai_view_img