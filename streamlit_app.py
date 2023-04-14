import streamlit as st

faq = {
    "Does your organization have a physical security policy?": {"Answer": "Answer for question 1", "Hint": "hint for question 1"},
    "What is your organizations SLA for incident response notifications?": {"Answer": "Ответ на вопрос 2", "Hint": "Подсказка для вопроса 2"},
    "Does your organization use a VPN when remote connections need access to the internal network?": {"Answer": "Ответ на вопрос 3", "Hint": "Подсказка для вопроса 3"},
}

if __name__ == '__main__':
    st.set_page_config(layout="wide")
    
    col1, col2, col3 = st.beta_columns(3)

    with col1:
        for question in faq:
            button_pressed = st.button(f"Select a question {question}")
            if button_pressed:
                selected_question = question
                break
        
        if 'selected_question' not in locals():
            selected_question = None
                    
        if selected_question:
            answer_input = st.empty()
            answer = st.text_input("Your answer:")
            if answer:
                faq[selected_question]["Answer"] = answer
        else:
           # st.write("Select a question")
                    
    with col2:
        st.write(f"FAQ: {faq[selected_question]['Hint']}" if selected_question else "")
        st.write("Possible answer:")
        st.write("1. Answer 1")
        st.write("2. Answer 2")
        st.write("3. Answer 3")
        st.write("4. Answer 4")
        st.write("5. Answer 5")

    with col3:
        st.write(f"Answer '{selected_question}': {faq[selected_question]['Answer']}" if selected_question else "")
