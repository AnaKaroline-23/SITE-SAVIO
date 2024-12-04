import streamlit as st
import datetime

# Conectando no CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Defina uma seleção de página para navegação
page = st.sidebar.selectbox("Escolha a página", ["Seu Perfil", "Reservas"])

# Verificar se a sessão está inicializada
if "usu_reserv" not in st.session_state:
    st.session_state["usu_reserv"] = {"nome": "", "email": ""}
if "reservations" not in st.session_state:
    st.session_state["reservations"] = []

# Página: Seu Perfil
if page == "Seu Perfil":
    st.title("SEU PERFIL")
    
    # Verifica se as informações do usuário estão completas
    if all(st.session_state.usu_reserv.values()):
        st.write("Nome:", st.session_state.usu_reserv["nome"])
        st.write("Email:", st.session_state.usu_reserv["email"])
    else:
        st.warning("Faça o Cadastro Primeiro")

# Página: Reservas
if page == "Reservas":
    st.title("Controle de Reservas")

    # Verifica se o usuário está cadastrado antes de permitir acessar as reservas
    if not all(st.session_state.usu_reserv.values()):
        st.warning("Por favor, faça o cadastro antes de acessar as reservas.")
    else:
        st.write(f"Bem-vindo(a), {st.session_state.usu_reserv['nome']}!")

        available_rooms = [
            "Auditório",
            "Laboratório",
            "Biblioteca",
            "Sala ds1",
            "Sala sist1",
            "Sala agn1",
            "Sala adm1",
        ]

        # Exibe reservas feitas
        if st.session_state.reservations:
            st.subheader("Reservas Feitas:")
            for res in st.session_state.reservations:
                st.write(
                    f"Sala: {res['room']} - Data: {res['date']} - Horário: {res['time']} - Motivo: {res['reason']}"
                )
        else:
            st.write("Nenhuma reserva feita ainda.")

        # Seção para fazer nova reserva
        st.subheader("Nova Reserva")
        room = st.selectbox("Escolha uma sala", available_rooms)
        date = st.date_input("Escolha a data", min_value=datetime.date.today())
        motivo = st.text_input("Diga o motivo")
        time_input = st.text_input("Digite o horário (formato HH:MM)", "09:00")

        try:
            time = datetime.datetime.strptime(time_input, "%H:%M").time()
        except ValueError:
            st.warning("Formato de hora inválido! Utilize o formato HH:MM (ex: 14:30).")
            time = None

        if st.button("Reservar"):
            if time:
                reservation_exists = False
                for res in st.session_state.reservations:
                    if (
                        res["room"] == room
                        and res["date"] == str(date)
                        and res["time"] == str(time)
                    ):
                        reservation_exists = True
                        break

                if reservation_exists:
                    st.warning("Esta sala já está reservada nesse horário.")
                else:
                    st.session_state.reservations.append(
                        {
                            "room": room,
                            "date": str(date),
                            "time": str(time),
                            "reason": motivo,
                        }
                    )
                    st.success(
                        f"Sala {room} reservada para {date} às {time}. Motivo: {motivo}"
                    )
            else:
                st.warning("Por favor, insira uma hora válida.")
