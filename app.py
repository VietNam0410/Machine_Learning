# import streamlit as st
# import pandas as pd
# # import mlflow
# # import mlflow.sklearn
# # import joblib
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # from sklearn.model_selection import train_test_split, cross_val_score
# # from sklearn.ensemble import RandomForestClassifier
# # from sklearn.metrics import accuracy_score
# #Factorial

# import Factorial # Import module đầy đủ
# import os

# # Tiêu đề trang web
# st.title("Bộ sưu tập bài tập 🎯")

# #
# def main():
#     st.title("Factorial Calculator")
#     number = st.number_input("Enter a number", min_value=0, max_value=100, value=0)
#     if st.button("Calculate"):
#         result = Factorial.factorial(number)
#         st.write(f"Factorial of {number} is {result}")
#         st.balloons()
# #Hiển thị nội dung của bài tập được chọn

# if __name__ == "__main__":
#     main()

import streamlit as st
import pandas as pd
import os
import Factorial  # Import module Factorial

# import mlflow
# import mlflow.sklearn
# import joblib
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

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

