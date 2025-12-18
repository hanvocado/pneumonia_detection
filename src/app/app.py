import streamlit as st
import torch
from PIL import Image
import styles
import utils

# ==========================================
# CẤU HÌNH TRANG WEB
# ==========================================
st.set_page_config(
    page_title="PneumoScan AI - Hệ Thống Chẩn Đoán Viêm Phổi",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Áp dụng CSS
styles.apply_custom_css()

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="color: #333; font-weight: 700;">⚙️ Bảng Điều Khiển</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🏥 Pneumonia Check")
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=80)
        
    # Load models từ utils.py
    st.markdown("### 📊 Trạng Thái Hệ Thống")
    cnn_model, resnet_model, st_cnn, st_resnet = utils.load_models()
    
    col1, col2 = st.columns(2)
    with col1:
        status_color = "🟢" if st_cnn["status"] == "success" else "🔴"
        st.markdown(f"""
        <div class="model-card model-{st_cnn['status']}">
            <h4 style="margin: 0;">{status_color} CNN Model</h4>
            <p style="font-size: 0.8rem; margin: 0.2rem 0;">{st_cnn['msg']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        status_color = "🟢" if st_resnet["status"] == "success" else "🔴"
        st.markdown(f"""
        <div class="model-card model-{st_resnet['status']}">
            <h4 style="margin: 0;">{status_color} ResNet18</h4>
            <p style="font-size: 0.8rem; margin: 0.2rem 0;">{st_resnet['msg']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 👥 Đội Ngũ Phát Triển")
    
    with st.expander("✨ Thông tin dự án & Thành viên", expanded=False):
        st.markdown("""
        <div style="background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0;">
            <p style="color: #6366f1; font-weight: 700; margin-bottom: 5px; font-size: 1rem;">
                🚀 NHÓM 7
            </p>
            <p style="color: #475569; font-size: 0.9rem; font-weight: 600; margin-bottom: 10px;">
                Dự án PneumoScan AI
            </p>
            <hr style="margin: 10px 0; border: 0.5px solid #e2e8f0;">
            <p style="font-weight: 600; font-size: 0.85rem; margin-bottom: 5px; color: #1e293b;">
                🎓 Thành viên:
            </p>
            <ul style="list-style-type: none; padding-left: 0; margin-bottom: 15px; color: #475569; font-size: 0.85rem;">
                <li style="margin-bottom: 3px;">• Nguyễn Thị Ngọc Hân</li>
                <li style="margin-bottom: 3px;">• Nguyễn Minh Quang</li>
                <li style="margin-bottom: 3px;">• Nguyễn Phương Thi</li>
                <li style="margin-bottom: 3px;">• Nguyễn Thị Thu Linh</li>
                <li style="margin-bottom: 3px;">• Lê Hồ Quốc Huy</li>
            </ul>
            <div style="background-color: #eff6ff; padding: 8px; border-radius: 5px;">
                <p style="margin: 0; font-size: 0.8rem; color: #1d4ed8;">
                    <strong>📚 GV hướng dẫn:</strong><br>Thầy Võ Lê Phúc Hậu
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    with st.expander("📋 Hướng dẫn sử dụng", expanded=False):
        st.markdown("""
        <div style="background-color: #f0fdf4; padding: 15px; border-radius: 10px; border: 1px solid #bbf7d0;">
            <p style="color: #166534; font-weight: 700; margin-bottom: 10px; font-size: 1rem;">
                Các bước thực hiện:
            </p>
            <div style="font-size: 0.85rem; color: #1e293b; line-height: 1.6;">
                <div style="margin-bottom: 8px;">
                    <span style="background: #16a34a; color: white; border-radius: 50%; padding: 2px 7px; margin-right: 5px; font-weight: bold;">1</span> 
                    <b>Tải ảnh:</b> Chọn file X-quang phổi từ thiết bị.
                </div>
                <div style="margin-bottom: 8px;">
                    <span style="background: #16a34a; color: white; border-radius: 50%; padding: 2px 7px; margin-right: 5px; font-weight: bold;">2</span> 
                    <b>Kiểm tra:</b> Xem trước ảnh để đảm bảo hình ảnh rõ nét.
                </div>
                <div style="margin-bottom: 8px;">
                    <span style="background: #16a34a; color: white; border-radius: 50%; padding: 2px 7px; margin-right: 5px; font-weight: bold;">3</span> 
                    <b>Phân tích:</b> Nhấn nút <i>"🚀 Bắt đầu Phân tích AI"</i>.
                </div>
                <div style="margin-bottom: 8px;">
                    <span style="background: #16a34a; color: white; border-radius: 50%; padding: 2px 7px; margin-right: 5px; font-weight: bold;">4</span> 
                    <b>Kết quả:</b> Đọc chẩn đoán và độ tin cậy của AI.
                </div>
            </div>
            <hr style="margin: 10px 0; border: 0.5px solid #bbf7d0;">
            <div style="background-color: #fff; padding: 8px; border-radius: 5px; border-left: 4px solid #f59e0b;">
                <p style="margin: 0; font-size: 0.8rem; color: #92400e;">
                    ⚠️ <b>Định dạng:</b> Hỗ trợ JPG, PNG, JPEG. Hình ảnh nên có chất lượng tốt nhất để đạt độ chính xác cao.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# GIAO DIỆN CHÍNH
# ==========================================
# Hiển thị Header
styles.show_header()

st.markdown("""
<div class="card">
    <h2 style="color: #333; margin-bottom: 1rem;">📤 Tải Lên Ảnh X-quang</h2>
    <p style="color: #666;">Vui lòng tải lên ảnh X-quang phổi để hệ thống phân tích</p>
</div>
""", unsafe_allow_html=True)

# Upload section
uploaded_file = st.file_uploader(
    "Kéo thả file vào đây hoặc click để chọn",
    type=["jpg", "png", "jpeg"],
    label_visibility="collapsed"
)

if uploaded_file is not None:
    # Hiển thị ảnh
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📷 Ảnh Gốc")
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, use_container_width=True, caption="Ảnh X-quang đã tải lên")

        with st.expander("👁️ Xem góc nhìn của AI (Preprocessed)"):
            # Gọi hàm xử lý từ utils.py
            _, ai_visual = utils.preprocess_image_exact(image, 'cnn') 
            st.image(ai_visual, caption="Ảnh sau khi tăng tương phản", use_container_width=True)
            st.info("AI tập trung vào các chi tiết phổi sau khi đã lọc bớt nhiễu sáng.")
    
    with col2:
        st.markdown("### 🔍 Thông Tin Ảnh")
        st.markdown(f"""
        <div class="card">
            <p><strong>Tên file:</strong> {uploaded_file.name}</p>
            <p><strong>Kích thước:</strong> {image.size[0]} x {image.size[1]} pixels</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Nút phân tích
        analyze_button = st.button(
            "🚀 Bắt Đầu Phân Tích AI",
            type="primary",
            use_container_width=True,
            help="Nhấn để hệ thống bắt đầu phân tích ảnh"
        )
        
        if analyze_button:
            with st.spinner("🔄 Đang phân tích với AI..."):
                # Phân tích CNN
                res_cnn = {"label": "N/A", "score": 0.0}
                if cnn_model:
                    input_cnn, _ = utils.preprocess_image_exact(image, 'cnn')
                    with torch.no_grad():
                        out = cnn_model(input_cnn)
                        probs = torch.softmax(out, dim=1)[0]
                        res_cnn["score"] = probs[1].item()
                        res_cnn["label"] = "VIÊM PHỔI" if res_cnn["score"] > 0.5 else "BÌNH THƯỜNG"
                
                # Phân tích ResNet
                res_resnet = {"label": "N/A", "score": 0.0}
                if resnet_model:
                    input_resnet, _ = utils.preprocess_image_exact(image, 'resnet')
                    with torch.no_grad():
                        out = resnet_model(input_resnet)
                        probs = torch.softmax(out, dim=1)[0]
                        res_resnet["score"] = probs[1].item()
                        res_resnet["label"] = "VIÊM PHỔI" if res_resnet["score"] > 0.5 else "BÌNH THƯỜNG"
                
                # Hiển thị kết quả từng model
                st.markdown("### 📊 Kết Quả Phân Tích Từng Model")
                
                col_cnn, col_resnet = st.columns(2)
                
                with col_cnn:
                    cnn_color = "#10b981" if res_cnn["label"] == "BÌNH THƯỜNG" else "#ef4444"
                    cnn_icon = "✅" if res_cnn["label"] == "BÌNH THƯỜNG" else "⚠️"
                    st.markdown(f"""
                    <div class="card">
                        <h3 style="color: {cnn_color};">{cnn_icon} CNN Model</h3>
                        <h2 style="color: {cnn_color}; margin: 1rem 0;">{res_cnn['label']}</h2>
                        <p><strong>Độ tin cậy:</strong> {res_cnn['score']*100:.1f}%</p>
                        <div style="background: #e5e7eb; height: 10px; border-radius: 5px; margin: 1rem 0;">
                            <div style="background: {cnn_color}; width: {res_cnn['score']*100}%; height: 100%; border-radius: 5px;"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_resnet:
                    resnet_color = "#10b981" if res_resnet["label"] == "BÌNH THƯỜNG" else "#ef4444"
                    resnet_icon = "✅" if res_resnet["label"] == "BÌNH THƯỜNG" else "⚠️"
                    st.markdown(f"""
                    <div class="card">
                        <h3 style="color: {resnet_color};">{resnet_icon} ResNet18</h3>
                        <h2 style="color: {resnet_color}; margin: 1rem 0;">{res_resnet['label']}</h2>
                        <p><strong>Độ tin cậy:</strong> {res_resnet['score']*100:.1f}%</p>
                        <div style="background: #e5e7eb; height: 10px; border-radius: 5px; margin: 1rem 0;">
                            <div style="background: {resnet_color}; width: {res_resnet['score']*100}%; height: 100%; border-radius: 5px;"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Kết quả tổng hợp
                st.markdown("### 🎯 Kết Luận Tổng Hợp")
                
                weight_cnn = 0.4
                weight_resnet = 0.6
                final_score = (res_cnn['score'] * weight_cnn) + (res_resnet['score'] * weight_resnet)
                
                if final_score >= 0.8:
                    result_class = "pneumonia-result"
                    result_icon = "🔴"
                    result_title = "VIÊM PHỔI (Nguy cơ cao)"
                    result_class = "result-card pneumonia-result blink-danger" # Thêm class blink
                    st.toast('⚠️ Phát hiện dấu hiệu bất thường nghiêm trọng!', icon='🚨')
                elif 0.5 <= final_score < 0.8:
                    result_class = "warning-result"
                    result_icon = "🟡"
                    result_title = "NGHI NGỜ VIÊM PHỔI"
                    result_class = "result-card pneumonia-result blink-danger" # Thêm class blink
                    st.toast('⚠️ Phát hiện dấu hiệu bất thường!', icon='🚨')
                elif 0.2 <= final_score < 0.5:
                    result_class = "normal-result"
                    st.balloons()
                    result_icon = "🟢"
                    result_title = "BÌNH THƯỜNG"
                    st.toast('Ổn: Phổi có vẻ khỏe mạnh', icon='✨')
                else:
                    result_class = "normal-result"
                    st.balloons()
                    result_icon = "🟢"
                    result_title = "PHỔI KHỎE MẠNH"
                    st.toast('Tuyệt vời: Phổi có vẻ rất khỏe mạnh', icon='✨')
                
                st.markdown(f"""
                <div class="result-card {result_class}">
                    <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                        <span style="font-size: 2rem; margin-right: 1rem;">{result_icon}</span>
                        <h2 style="margin: 0;">{result_title}</h2>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 10px; margin: 1rem 0;">
                        <h3 style="color: #333; margin-bottom: 0.5rem;">📈 Độ tin cậy hệ thống: {final_score*100:.1f}%</h3>
                        <div style="background: linear-gradient(90deg, #3b82f6, #8b5cf6); height: 15px; border-radius: 10px; width: {final_score*100}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("📊 Thông tin kỹ thuật chi tiết"):
                    col_tech1, col_tech2 = st.columns(2)
                    with col_tech1:
                        st.markdown("**🎯 Trọng số Ensemble:**")
                        st.markdown("- CNN Model: 40%")
                        st.markdown("- ResNet18: 60%")
                        st.markdown(f"- **Điểm tổng hợp:** {final_score:.3f}")
                    
                    with col_tech2:
                        st.markdown("**⚙️ Thông số xử lý:**")
                        st.markdown(f"- Kích thước ảnh: 224×224px")
                        st.markdown(f"- Contrast Alpha: 2.5")
                        st.markdown(f"- Brightness Beta: -180")
                        st.markdown(f"- Gamma Correction: 1.0")

else:
    st.markdown("""
    <div class="upload-section">
        <div style="font-size: 4rem; margin-bottom: 1rem;">📤</div>
        <h3 style="color: #475569;">Kéo thả ảnh X-quang vào đây</h3>
        <p style="color: #94a3b8;">Hoặc click để chọn file từ máy tính</p>
        <p style="color: #64748b; font-size: 0.9rem; margin-top: 2rem;">
        <strong>📝 Lưu ý:</strong> Hệ thống hỗ trợ các định dạng JPG, PNG, JPEG
        </p>
    </div>
    """, unsafe_allow_html=True)

# Hiển thị Footer
styles.show_footer()