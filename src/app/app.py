import streamlit as st
import torch
from PIL import Image
import styles
import utils
import time

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
    
    # Dropdown chọn mode phân tích
    st.markdown("### 🎯 Chế Độ Phân Tích")
    analysis_mode = st.selectbox(
        "Chọn phương pháp phân tích:",
        [
            "CNN",
            "ResNet18", 
            "MobileNetV3",
            "Ensemble (Tỉ lệ: 30-40-30)"
        ],
        index=3,  # Mặc định chọn Ensemble
        help="Lựa chọn phương pháp phân tích ảnh X-quang"
    )
    
    st.markdown("---")
        
    # Load models từ utils.py
    st.markdown("### 📊 Trạng Thái Hệ Thống")
    # Load 3 models
    cnn_model, resnet_model, mobilenet_model, st_cnn, st_resnet, st_mobi = utils.load_models()
    
    # Hiển thị status card
    for s in [st_cnn, st_resnet, st_mobi]:
        color = "🟢" if s["status"] == "success" else "🔴"
        st.markdown(f"""<div class="model-card model-{s['status']}"><p style="margin:0;">{color} {s['msg']}</p></div>""", unsafe_allow_html=True)
    
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
                    <b>Chọn mode:</b> Lựa chọn phương pháp phân tích ở sidebar.
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
            <p><strong>Chế độ đã chọn:</strong> {analysis_mode}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Hiển thị thông tin về mode được chọn
        mode_info = {
            "CNN": "Sử dụng mô hình CNN tùy chỉnh",
            "ResNet18": "Sử dụng mô hình ResNet18",
            "MobileNetV3": "Sử dụng mô hình MobileNetV3 nhẹ và nhanh",
            "Ensemble (Tỉ lệ: 30-40-30)": "Kết hợp 3 mô hình với tỉ lệ: CNN 30%, ResNet18 40%, MobileNetV3 30%"
        }
        
        st.info(f"**Mode đang dùng:** {mode_info[analysis_mode]}")
        
        # Nút phân tích
        analyze_button = st.button(
            "🚀 Bắt Đầu Phân Tích AI",
            type="primary",
            use_container_width=True,
            help="Nhấn để hệ thống bắt đầu phân tích ảnh"
        )
        
        if analyze_button:
            # Tạo progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Hiển thị thời gian bắt đầu
            start_time = time.time()
            status_text.text(f"⏱️ Bắt đầu phân tích lúc: {time.strftime('%H:%M:%S')}")
            
            # Phân tích ảnh với progress bar
            for i in range(1, 101, 20):
                progress_bar.progress(i)
                time.sleep(0.1)
            
            # Đo thời gian inference
            inference_start = time.time()
            
            # Khởi tạo biến cho kết quả
            scores = {}
            final_score = 0.0
            inference_time = 0.0
            
            # Tính điểm từng model dựa trên mode được chọn
            try:
                # Nếu là mode đơn lẻ hoặc ensemble
                if analysis_mode in ["CNN", "Ensemble (Tỉ lệ: 30-40-30)"] and cnn_model:
                    inp, _ = utils.preprocess_image_exact(image, 'cnn')
                    with torch.no_grad():
                        score_cnn = torch.softmax(cnn_model(inp), dim=1)[0][1].item()
                    scores["CNN"] = score_cnn
                
                if analysis_mode in ["ResNet18", "Ensemble (Tỉ lệ: 30-40-30)"] and resnet_model:
                    inp, _ = utils.preprocess_image_exact(image, 'resnet')
                    with torch.no_grad():
                        score_resnet = torch.softmax(resnet_model(inp), dim=1)[0][1].item()
                    scores["ResNet18"] = score_resnet
                
                if analysis_mode in ["MobileNetV3", "Ensemble (Tỉ lệ: 30-40-30)"] and mobilenet_model:
                    inp, _ = utils.preprocess_image_exact(image, 'resnet')
                    with torch.no_grad():
                        score_mobilenet = torch.softmax(mobilenet_model(inp), dim=1)[0][1].item()
                    scores["MobileNetV3"] = score_mobilenet
                
                # Kiểm tra xem model có sẵn hay không
                if analysis_mode == "CNN":
                    if "CNN" in scores:
                        final_score = scores["CNN"]
                    else:
                        st.error("⚠️ Mô hình CNN không khả dụng. Vui lòng kiểm tra lại trạng thái hệ thống.")
                        progress_bar.empty()
                        status_text.empty()
                        st.stop()
                
                elif analysis_mode == "ResNet18":
                    if "ResNet18" in scores:
                        final_score = scores["ResNet18"]
                    else:
                        st.error("⚠️ Mô hình ResNet18 không khả dụng. Vui lòng kiểm tra lại trạng thái hệ thống.")
                        progress_bar.empty()
                        status_text.empty()
                        st.stop()
                
                elif analysis_mode == "MobileNetV3":
                    if "MobileNetV3" in scores:
                        final_score = scores["MobileNetV3"]
                    else:
                        st.error("⚠️ Mô hình MobileNetV3 không khả dụng. Vui lòng kiểm tra lại trạng thái hệ thống.")
                        progress_bar.empty()
                        status_text.empty()
                        st.stop()
                
                elif analysis_mode == "Ensemble (Tỉ lệ: 30-40-30)":
                    # Kiểm tra xem có đủ 3 model không
                    if "CNN" in scores and "ResNet18" in scores and "MobileNetV3" in scores:
                        # Tính theo tỉ lệ: CNN = 0.3, ResNet18 = 0.4, MobileNetV3 = 0.3
                        final_score = (scores["CNN"] * 0.3) + (scores["ResNet18"] * 0.4) + (scores["MobileNetV3"] * 0.3)
                    else:
                        st.error("⚠️ Không đủ mô hình để thực hiện Ensemble. Vui lòng kiểm tra lại trạng thái hệ thống.")
                        progress_bar.empty()
                        status_text.empty()
                        st.stop()
                
            except Exception as e:
                st.error(f"⚠️ Lỗi khi phân tích: {str(e)}")
                progress_bar.empty()
                status_text.empty()
                st.stop()
            
            inference_end = time.time()
            inference_time = inference_end - inference_start
            
            progress_bar.progress(100)
            time.sleep(0.2)
            progress_bar.empty()
            status_text.empty()
            
            # Tính tổng thời gian
            end_time = time.time()
            total_time = end_time - start_time
            
            # Hiển thị thời gian dự đoán
            st.markdown(f"""
            <div class="card" style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);">
                <h4>⏱️ Thông Tin Thời Gian</h4>
                <p><strong>Thời gian inference:</strong> {inference_time:.3f} giây</p>
                <p><strong>Tổng thời gian xử lý:</strong> {total_time:.3f} giây</p>
                <p><strong>Bắt đầu:</strong> {time.strftime('%H:%M:%S', time.localtime(start_time))}</p>
                <p><strong>Kết thúc:</strong> {time.strftime('%H:%M:%S', time.localtime(end_time))}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Hiển thị kết quả từng model nếu có nhiều model
            if analysis_mode == "Ensemble (Tỉ lệ: 30-40-30)" and len(scores) >= 2:
                st.markdown("### 📊 Kết Quả Chi Tiết Từng Model")
                cols = st.columns(len(scores))
                for idx, (model_name, score) in enumerate(scores.items()):
                    with cols[idx]:
                        st.metric(
                            label=model_name,
                            value=f"{score*100:.1f}%",
                            delta=None,
                            help=f"Độ tin cậy từ {model_name}"
                        )
            
            # --- HIỂN THỊ KẾT QUẢ CUỐI CÙNG ---
            if final_score >= 0.8:
                result_class = "pneumonia-result"
                result_icon = "🔴"
                result_title = "VIÊM PHỔI (Nguy cơ cao)"
                result_class = "result-card pneumonia-result blink-danger"
                st.toast('⚠️ Phát hiện dấu hiệu bất thường nghiêm trọng!', icon='🚨')
            elif 0.5 <= final_score < 0.8:
                result_class = "warning-result"
                result_icon = "🟡"
                result_title = "NGHI NGỜ VIÊM PHỔI"
                result_class = "result-card pneumonia-result blink-danger"
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
            
            # Hiển thị kết quả
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
                <p style="color: #666; font-size: 0.9rem; margin-top: 0.5rem;">
                <strong>Phương pháp:</strong> {analysis_mode}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Thông tin kỹ thuật chi tiết
            with st.expander("📊 Thông tin kỹ thuật chi tiết"):
                col_tech1, col_tech2 = st.columns(2)
                with col_tech1:
                    st.markdown("**🎯 Thông số hệ thống:**")
                    st.markdown(f"- **Mode đang dùng:** {analysis_mode}")
                    st.markdown(f"- **Điểm tổng hợp:** {final_score:.4f}")
                    st.markdown(f"- **Thời gian inference:** {inference_time:.3f} giây")
                    
                    if scores:
                        st.markdown("**📈 Điểm từng model:**")
                        for model_name, score in scores.items():
                            st.markdown(f"- {model_name}: {score:.4f}")
                    
                    if analysis_mode == "Ensemble (Tỉ lệ: 30-40-30)":
                        st.markdown("**⚖️ Trọng số Ensemble:**")
                        st.markdown("- CNN Model: 30%")
                        st.markdown("- ResNet18: 40%")
                        st.markdown("- MobileNetV3: 30%")
                
                with col_tech2:
                    st.markdown("**⚙️ Thông số xử lý ảnh:**")
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
        <strong>📝 Lưu ý:</strong> Hệ thống hỗ trợ các định dạng JPG, PNG, JPEG<br>
        <strong>🎯 Chú ý:</strong> Chọn phương pháp phân tích ở sidebar trước khi upload
        </p>
    </div>
    """, unsafe_allow_html=True)

# Hiển thị Footer
styles.show_footer()