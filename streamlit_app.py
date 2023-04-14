import streamlit as st
import pandas as pd

import streamlit as st

# Вопросы и ответы в формате словаря
faq = {
    "Вопрос 1": {
        "Ответ": "Ответ на вопрос 1",
        "Подсказка": "Это подсказка для вопроса 1"
    },
    "Вопрос 2": {
        "Ответ": "Ответ на вопрос 2",
        "Подсказка": "Это подсказка для вопроса 2"
    },
    "Вопрос 3": {
        "Ответ": "Ответ на вопрос 3",
        "Подсказка": "Это подсказка для вопроса 3"
    }
}

# Создание трех равных колонок
col1, col2, col3 = st.beta_columns(3)

# Создание виджетов "аккордеон" для списка вопросов в первой колонке
with col1:
    st.write("## Список вопросов")
    for question in faq.keys():
        with st.beta_expander(question):
            st.write(faq[question]["Подсказка"])
            # Форма для ввода ответа на выбранный вопрос
            with st.form(key=question):
                answer = st.text_input("Введите ответ здесь:")
                submit_button = st.form_submit_button("Отправить ответ")

# Отображение подсказки и вариантов ответа во второй колонке
with col2:
    st.write(f"## Подсказка")
    st.write(faq[selected_question]["Подсказка"])
    st.write(f"## Варианты ответа")
    options = ["Вариант 1", "Вариант 2", "Вариант 3", "Вариант 4", "Вариант 5"]
    selected_option = st.radio("", options)

# Отображение ответа на выбранный вопрос в третьей колонке
with col3:
    st.write(f"## Ответ на вопрос: {selected_question}")
    st.write(faq[selected_question]["Ответ"])
