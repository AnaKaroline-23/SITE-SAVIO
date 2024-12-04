import streamlit as st


st.title("SEU CADASTRO")
st.session_state.usu_reserv["nome"] = st.text_input(
        "Nome:", value=st.session_state.usu_reserv["nome"] or ""
    )
st.session_state.usu_reserv["email"] = st.text_input(
        "Email:", value=st.session_state.usu_reserv["email"] or ""
    )
st.session_state.usu_reserv["senha"] = st.text_input(
        "Senha:", type="password", value=st.session_state.usu_reserv["senha"] or ""
    )
if st.button("Cadastrar"):
    email = st.session_state.usu_reserv["email"]
    nome = st.session_state.usu_reserv["nome"]
    senha = st.session_state.usu_reserv["senha"]

if len(nome) < 4:
        st.warning("Digite um nome com pelo menos 4 caracteres.")
elif len(email) < 6:
    st.warning("Digite um e-mail válido.")
elif len(senha) < 7:
    st.warning("Digite uma senha com pelo menos 7 caracteres.")
else:
    st.success("Suas credenciais foram cadastradas com sucesso!")