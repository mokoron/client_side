import streamlit as st
import pandas as pd


faq = {
    "Вопрос 1": {"Ответ": "Ответ на вопрос 1", "Подсказка": "Подсказка для вопроса 1"},
    "Вопрос 2": {"Ответ": "Ответ на вопрос 2", "Подсказка": "Подсказка для вопроса 2"},
    "Вопрос 3": {"Ответ": "Ответ на вопрос 3", "Подсказка": "Подсказка для вопроса 3"},
}

if __name__ == '__main__':
    st.set_page_config(layout="wide")
    
    col1, col2, col3 = st.beta_columns(3)

    with col1:
        for question in faq:
            expander = st.beta_expander(question)
            with expander:
                if st.button("Выбрать вопрос"):
                    answer = st.text_input("Введите ответ:")
                    if answer:
                        faq[question]["Ответ"] = answer
                else:
                    st.write(faq[question]["Ответ"])

    with col2:
        selected_question = st.radio("Выберите вопрос", list(faq.keys()))
        st.write(f"Подсказка: {faq[selected_question]['Подсказка']}")
        st.write("Варианты ответов:")
        st.write("1. Ответ 1")
        st.write("2. Ответ 2")
        st.write("3. Ответ 3")
        st.write("4. Ответ 4")
        st.write("5. Ответ 5")

    with col3:
        st.write(f"Ответ на вопрос '{selected_question}':")
        st.write(faq[selected_question]["Ответ"])
