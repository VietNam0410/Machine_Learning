
import streamlit as st
import pandas as pd
import os
import Factorial  # Import module Factorial


# 🔥 Sidebar chọn bài tập
st.sidebar.header("📚 Chọn bài tập:")
exercise_options = ["Factorial Calculator"]  # Danh sách bài tập mặc định

# 🔍 Tự động tìm các bài tập trong thư mục exercises
if os.path.exists("exercises"):
    exercise_files = [f for f in os.listdir("exercises") if f.endswith(".py")]
    exercise_options.extend(exercise_files)

# 🛠 Hiển thị danh sách chọn bài tập
selected_exercise = st.sidebar.selectbox("Chọn bài tập:", exercise_options)

# 📌 Hiển thị nội dung của bài tập được chọn
def factorial_calculator():
    """Giao diện tính giai thừa."""
    st.header("🧮 Factorial Calculator")
    number = st.number_input("Nhập số:", min_value=0, max_value=100, value=0, step=1)
    if st.button("Tính giai thừa"):
        result = Factorial.factorial(number)
        st.success(f"{number}! = {result}")
        st.balloons()

# 🏃‍♂️ Chạy bài tập được chọn
if selected_exercise == "Factorial Calculator":
    factorial_calculator()
else:
    st.sidebar.write(f"🔄 Đang chạy `{selected_exercise}`...")
    exec(open(f"exercises/{selected_exercise}").read())

