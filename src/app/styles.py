import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
        @keyframes blinker {
            50% { opacity: 0.5; }
            }
            .blink-danger {
            animation: blinker 1s linear infinite;
            border: 3px solid #ef4444 !important;
            background-color: #fee2e2 !important;
            }         


        /* Reset và font chữ */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        * { font-family: 'Inter', sans-serif; }
        
        /* Header chính */
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            color: white;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        .main-header h1 { font-size: 2.8rem; font-weight: 700; margin-bottom: 0.5rem; }
        .main-header p { font-size: 1.1rem; opacity: 0.9; font-weight: 300; }
        
        /* Card hiện đại */
        .card {
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            border: 1px solid #eaeaea;
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .card:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0,0,0,0.12); }
        
        /* Model status cards */
        .model-card { padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 5px solid; }
        .model-success { background: linear-gradient(90deg, #f0f9ff 0%, #e0f2fe 100%); border-left-color: #0ea5e9; }
        .model-error { background: linear-gradient(90deg, #fef2f2 0%, #fee2e2 100%); border-left-color: #ef4444; }
        
        /* Progress bar */
        .stProgress > div > div > div > div { background: linear-gradient(90deg, #3b82f6, #8b5cf6); border-radius: 10px; }
        
        /* Button */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; border: none; padding: 0.75rem 2rem; font-weight: 600;
            border-radius: 10px; transition: all 0.3s ease; width: 100%; font-size: 1rem;
        }
        .stButton > button:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3); }
        
        /* Upload section */
        .upload-section {
            border: 3px dashed #cbd5e1; border-radius: 15px; padding: 3rem;
            text-align: center; background: #f8fafc; transition: all 0.3s ease;
        }
        .upload-section:hover { border-color: #667eea; background: #f0f9ff; }
        
        /* Result cards */
        .result-card { padding: 1.5rem; border-radius: 15px; margin: 1rem 0; }
        .normal-result { background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%); border: 2px solid #10b981; }
        .pneumonia-result { background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); border: 2px solid #ef4444; }
        .warning-result { background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 2px solid #f59e0b; }
        
        /* Footer & Hidden items */
        .footer {
            text-align: center; padding: 2rem; margin-top: 3rem; color: #64748b;
            font-size: 0.9rem; border-top: 1px solid #e2e8f0;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def show_header():
    st.markdown("""
    <div class="main-header">
        <h1>🫁 PneumoScan AI</h1>
        <p>Hệ Thống Chẩn Đoán Viêm Phổi Bằng AI - Kết Hợp Ensemble Learning</p>
        <div style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.8;">
            <span>🎯 Độ chính xác cao | ⚡ Tốc độ xử lý nhanh | 🛡️ An toàn & Bảo mật</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_footer():
    st.markdown("""
    <div class="footer">
        <p><strong>🫁 PneumoScan AI</strong> - Hệ thống chẩn đoán viêm phổi bằng AI</p>
        <p style="font-size: 0.8rem; color: #94a3b8;">
        ⚠️ Lưu ý: Đây là công cụ hỗ trợ chẩn đoán, không thay thế ý kiến bác sĩ chuyên môn.<br>
        Mọi kết quả cần được xác nhận bởi chuyên gia y tế.
        </p>
        <p style="font-size: 0.7rem; color: #cbd5e1; margin-top: 1rem;">
        © 2025 Nhóm 7 - Dự án AI trong Y tế | Phiên bản 1.0
        </p>
    </div>
    """, unsafe_allow_html=True)