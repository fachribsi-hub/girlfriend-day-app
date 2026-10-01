import streamlit as st

# ==========================================================
# ATUR KUNCI JAWABAN KUIS DI SINI (Gunakan huruf kecil semua)
# ==========================================================
JAWABAN_QUIZ_1 = "hitam"        # Pertanyaan 1: Warna favorit cowo
JAWABAN_QUIZ_2 = "mie goreng"   # Pertanyaan 2: Makanan favorit cowo
JAWABAN_QUIZ_3 = "18 september"   # Pertanyaan 3: Tanggal jadian / tanggal spesial

# Pengaturan Judul dan Layout Halaman
st.set_page_config(page_title="Happy Girlfriend Day! 💕", page_icon="💖", layout="centered")

# Menggunakan Session State untuk menyimpan status progres & input user
if "step" not in st.session_state:
    st.session_state.step = 1
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "gf_love_msg" not in st.session_state:
    st.session_state.gf_love_msg = ""

# CSS Tambahan untuk mempercantik tampilan tombol dan kotak
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.2em;
        font-weight: bold;
        background-color: #ff4b4b;
        color: white;
    }
    .stButton>button:hover {
        background-color: #ff6b6b;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------------
# HALAMAN 1: ISIAN DATA (FORM)
# ------------------------------------
if st.session_state.step == 1:
    st.title("💖 Special Girlfriend Day 💖")
    st.subheader("Selamat Datang! Isi data dulu yaa sebelum lanjut 😊")
    
    with st.form("user_info_form"):
        name = st.text_input("Nama Kamu/Panggilan Kesayangan:")
        submit = st.form_submit_button("Lanjut ke Kuis! ✨")
        
        if submit:
            if name.strip() == "":
                st.warning("Isi nama kamu dulu dong cantik! 😊")
            else:
                st.session_state.user_name = name.strip()
                st.session_state.step = 2
                st.rerun()

# ------------------------------------
# HALAMAN 2: KUIS INTERAKTIF (3 PERTANYAAN)
# ------------------------------------
elif st.session_state.step == 2:
    st.title(f" Kuis Uji Ketepatan, {st.session_state.user_name}! 🧐")
    st.write("Jawab 3 pertanyaan ini dengan benar ya! Kalau salah ga akan bisa lanjut~")
    st.write("---")
    
    with st.form("quiz_form"):
        ans1 = st.text_input("1. Apa warna favorit cowok kamu?")
        ans2 = st.text_input("2. Apa makanan favorit cowok kamu?")
        ans3 = st.text_input("3. Tanggal berapa hari spesial / jadian kita? (Contoh: 12 Desember)")
        
        submit_quiz = st.form_submit_button("Cek Jawaban 🚀")
        
        if submit_quiz:
            # Pengecekan jawaban (diubah ke huruf kecil agar toleran penulisan)
            q1_correct = ans1.strip().lower() == JAWABAN_QUIZ_1.lower()
            q2_correct = ans2.strip().lower() == JAWABAN_QUIZ_2.lower()
            q3_correct = ans3.strip().lower() == JAWABAN_QUIZ_3.lower()
            
            if q1_correct and q2_correct and q3_correct:
                st.success("WAAAH HEBAT! Semua jawaban kamu BENAR! 🎉")
                st.session_state.step = 3
                st.rerun()
            else:
                st.error("Waduh ada jawaban yang masih salah nih! Coba tebak lagi yaa 😜")

# ------------------------------------
# HALAMAN 3: UNGKAPAN RASA SAYANG
# ------------------------------------
elif st.session_state.step == 3:
    st.title(" Coba Tuliskan Perasaanmu ❤️")
    st.write(f"Sebelum lanjut, coba ketik kalimat atau ungkapan rasa sayang kamu buat cowok kamu di bawah ini...")
    
    with st.form("love_letter_form"):
        gf_msg = st.text_area("Tulis kalimat sayang kamu di sini:", height=150)
        submit_msg = st.form_submit_button("Kirim Ungkapan Sayang 💌")
        
        if submit_msg:
            if gf_msg.strip() == "":
                st.warning("Tulis dulu dong walau sedikit! 😉")
            else:
                st.session_state.gf_love_msg = gf_msg.strip()
                st.session_state.step = 4
                st.rerun()

# ------------------------------------
# HALAMAN 4: BALASAN DARI COWOKNYA
# ------------------------------------
elif st.session_state.step == 4:
    st.title(" Balasan Untukmu... 💖")
    
    st.info(f"**Pesan yang kamu tulis tadi:**\n\n\"{st.session_state.gf_love_msg}\"")
    st.write("---")
    
    # Pesan Balasan Romantis dari Kamu
    st.success("""
    sayangggg.. inii pertama kalinyaa akuu belajarr kayakk ginii, terimakasih sudahh mauu klik klik setiapp slidenyaa yangg akuu usahainn bisa walauu pake AI.. tapi bikinn inii jugaa pake effort lhoo!!.. akuuu sayanggg bangettt samaa kamuu, akuu harap dengan jadinyaa website ini.. akuu bisaa bikinn kamuu bangga dan terharu bahagiaa. i loveee youuuuu sayangggggg 💗💗💗
    """)
    
    if st.button("Lanjut ke Game Tebak Amplop 🎁"):
        st.session_state.step = 5
        st.rerun()

# ------------------------------------
# HALAMAN 5: GAME TEBAK AMPLOP (3 OPSI)
# ------------------------------------
elif st.session_state.step == 5:
    st.title(f"Pilih Amplop Keberuntunganmu! 📦")
    st.write("Ada 3 amplop di bawah ini. Cuma ada 1 amplop Jackpot yang isinya pesan spesial!")
    st.write("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📦 Amplop 1"):
            st.error("😜 ZONK! Coba pilih amplop lain ya~")

    with col2:
        if st.button("📦 Amplop 2"):
            st.session_state.step = 6
            st.rerun()

    with col3:
        if st.button("📦 Amplop 3"):
            st.warning("🤪 ZONK JUGA! Ayo tebak lagi!")

# ------------------------------------
# HALAMAN 6: JACKPOT (KATA-KATA PESAN SPESIAL)
# ------------------------------------
elif st.session_state.step == 6:
    st.balloons()  # Efek balon terbang
    st.title("🎉 SELAMAT! KAMU DAPAT JACKPOT! 🎉")
    st.subheader(f"Happy Girlfriend Day, {st.session_state.user_name}! ❤️")
    
    st.success("""
    **Pesan Spesial Untukmu:**
    
    Makasih ya udah hadir dan buat hari-hari aku jadi lebih bermakna. 
    Kamu itu salah satu alasan kenapa aku selalu tersenyum setiap hari. 
    
    Tetap jadi diri kamu yang lucu, baik, dan penyayang ya. 
    *Happy Girlfriend Day! I'm so lucky to have you in my life!* 💖✨
    """)
    
    if st.button("🔄 Ulang dari Awal"):
        st.session_state.step = 1
        st.rerun()