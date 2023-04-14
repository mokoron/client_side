import streamlit as st
import pandas as pd


faq = {
    "Вопрос 1": {"Ответ": "Ответ на вопрос 1", "Подсказка": "Подсказка для вопроса 1"},
    "Вопрос 2": {"Ответ": "Ответ на вопрос 2", "Подсказка": "Подсказка для вопроса 2"},
    "Вопрос 3": {"Ответ": "Ответ на вопрос 3", "Подсказка": "Подсказка для вопроса 3"},
}

selected_question = None

col1, col2, col3 = st.beta_columns(3)

with col1:
    for question in faq:
        expander = st.beta_expander(question, expanded=(question == selected_question))
        if expander.clicked:
            selected_question = question
        with expander:
            if question == selected_question:
                answer = st.text_input("Введите ответ:")
                if answer:
                    faq[selected_question]["Ответ"] = answer
            else:
                st.write(faq[question]["Ответ"])

with col2:
    if selected_question is None:
        st.write("Выберите вопрос в левой колонке.")
    else:
        st.write(f"Подсказка: {faq[selected_question]['Подсказка']}")
        st.write("Варианты ответов:")
        st.write("1. Ответ 1")
        st.write("2. Ответ 2")
        st.write("3. Ответ 3")
        st.write("4. Ответ 4")
        st.write("5. Ответ 5")

with col3:
    if selected_question is None:
        st.write("Выберите вопрос в левой колонке.")
    else:
        st.write(f"Ответ на вопрос '{selected_question}':")
        st.write(faq[selected_question]["Ответ"])
