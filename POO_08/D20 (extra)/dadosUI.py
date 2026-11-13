import streamlit as st
import random

class DadosUI:
    def main():
        st.header("Dados")
        if st.button("D20"):
            st.write(random.randint(1,20))

        if st.button("D12"):
            st.write(random.randint(1,12))

        if st.button("D10"):
            st.write(random.randint(1,10))

        if st.button("D8"):
            st.write(random.randint(1,8))

        if st.button("D6"):
            st.write(random.randint(1,6))

        if st.button("D4"):
            st.write(random.randint(1,4))