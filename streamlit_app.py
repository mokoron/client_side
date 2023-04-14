import streamlit as st
from streamlit.components.v1 import html

faq = {
    "Вопрос 1": {"Ответ": "Ответ на вопрос 1", "Варианты ответов": ["Ответ 1", "Ответ 2", "Ответ 3"]},
    "Вопрос 2": {"Ответ": "Ответ на вопрос 2", "Варианты ответов": ["Ответ 1", "Ответ 2", "Ответ 3"]},
    "Вопрос 3": {"Ответ": "Ответ на вопрос 3", "Варианты ответов": ["Ответ 1", "Ответ 2", "Ответ 3"]},
}

selected_question = st.sidebar.selectbox("Выберите вопрос", list(faq.keys()))

col1, col2, col3 = st.beta_columns(3)

with col1:
    for question in faq:
        expander = st.beta_expander(question)
        with expander:
            if question == selected_question:
                answer = html.radio("Выберите ответ", faq[selected_question]["Варианты ответов"])
                st.write(f"Ответ на вопрос '{selected_question}': {answer}")
                style = """
                    input[type="radio"] {
                        visibility: hidden;
                    }
                    label[for^="radio"] {
                        display: block;
                        padding: 5px 10px;
                        border: 1px solid #CCC;
                        border-radius: 5px;
                        cursor: pointer;
                    }
                    label[for^="radio"]:hover {
                        background-color: #EEE;
                    }
                    input[type="radio"]:checked + label {
                        background-color: #DDD;
                    }
                """
                html(f'<style>{style}</style>')
            else:
                st.write(faq[question]["Ответ"])

with col2:
    st.write(f"Подсказка: {faq[selected_question]['Подсказка']}")
    st.write("Варианты ответов:")
    for option in faq[selected_question]["Варианты ответов"]:
        st.write(f"- {option}")

with col3:
    st.write(f"Ответ на вопрос '{selected_question}':")
    st.write(faq[selected_question]["Ответ"])
