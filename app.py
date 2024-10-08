import streamlit as st

# Configurando o layout da página principal
st.image('https://raw.githubusercontent.com/acker241/viva-Halsten/main/topo.png')

# Criando o grid 4x4 para navegação
st.header("Explore Nossos Serviços")

ic1, ic2, ic3 = st.columns([0.2, 0.4, 0.4])

with ic1:
    st.image('https://raw.githubusercontent.com/acker241/viva-Halsten/main/pages/perfilTransp.png', width=120)
with ic2:
    st.write('')
    st.write('')
    st.write('')    
    st.write('Como está hoje Fulano de Tal?')

cols = st.columns(4)

# Definindo as opções clicáveis
with cols[0]:
    if st.button("Refuge Campo"):
        st.query_params['page'] = "refuge_campo"
with cols[1]:
    if st.button("Refuge Litoral"):
        st.query_params['page'] =  "refuge_litoral"
with cols[2]:
    if st.button("Vivência Halsten"):
        st.query_params['page'] = "vivencia_halsten"
with cols[3]:
    if st.button("Halsten Energia"):
        st.query_params['page'] = "halsten_energia"



# Capturando a página atual pela query string

if st.query_params.get_all("page") == []:
    page = ''
else:
    page = st.query_params.get_all("page")[0]


# Funções das páginas específicas
def refuge_campo_page():
    st.header("Refuge Campo")
    st.subheader("Estadias no Campo")
    st.write("Explore opções de estadias curtas no campo com diversas atividades ao ar livre.")
    col1, col2 = st.columns(2)
    with col1:
        st.image('https://raw.githubusercontent.com/acker241/viva-Halsten/main/chales/10.png')
        st.image('https://raw.githubusercontent.com/acker241/viva-Halsten/main/chales/11.png')
    with col2:
        st.image('https://raw.githubusercontent.com/acker241/viva-Halsten/main/chales/12.png')
        st.image('https://raw.githubusercontent.com/acker241/viva-Halsten/main/chales/13.png')
    # Aqui você pode adicionar mais funcionalidades, como listagem de opções, reserva, etc.

def refuge_litoral_page():
    st.header("Refuge Litoral")
    st.subheader("Estadias no Litoral")
    st.write("Aproveite estadias curtas no litoral com acesso a praias, esportes aquáticos e muito mais.")
    # Aqui você pode adicionar funcionalidades semelhantes às da página Refuge Campo.

def halsten_energia_page():
    st.header("Halsten Energia")
    st.subheader("Suas Faturas de Energia")
    st.write("Veja suas faturas anteriores e acompanhe o impacto ambiental positivo:")
    # Simulação de faturas e estimativas
    faturas = {
        "Julho 2024": "R$ 150,00",
        "Junho 2024": "R$ 160,00",
        "Maio 2024": "R$ 170,00",
    }
    for mes, valor in faturas.items():
        st.write(f"**{mes}:** {valor}")
    st.subheader("Estimativa de Carbono Não Emitido")
    st.write("Você ajudou a não liberar 1.2 toneladas de CO2 por utilizar energia solar!")

def vivencia_halsten_page():
    st.header("Vivência Halsten")
    st.subheader("Explore os Empreendimentos")
    st.write("Selecione um empreendimento para ver serviços e utilidades nas redondezas.")
    # Simulação de um grid para selecionar empreendimentos
    empreendimentos = ["Halsten Prime", "Halsten Garden", "Halsten Beach"]
    cols = st.columns(len(empreendimentos))
    for i, empreendimento in enumerate(empreendimentos):
        with cols[i]:
            if st.button(empreendimento):
                st.query_params['page'] =f"vivencia_{empreendimento.lower().replace(' ', '_')}"
                st.rerun()

def vivencia_detalhes_page(empreendimento):
    st.header(f"Vivência {empreendimento}")
    st.subheader(f"Serviços e utilidades próximos ao {empreendimento}")
    # Simulação de serviços por região
    servicos = {
        "Halsten Prime": ["Supermercado A", "Farmácia B", "Escola C"],
        "Halsten Garden": ["Academia D", "Padaria E", "Clínica F"],
        "Halsten Beach": ["Restaurante G", "Praia H", "Parque I"]
    }
    for servico in servicos.get(empreendimento, []):
        st.write(f"- {servico}")

# Navegação baseada na página selecionada
if page == "refuge_campo":
    refuge_campo_page()
elif page == "refuge_litoral":
    refuge_litoral_page()
elif page == "halsten_energia":
    halsten_energia_page()
elif page == "vivencia_halsten":
    vivencia_halsten_page()
elif page.startswith("vivencia_"):
    empreendimento = page.replace("vivencia_", "").replace("_", " ").title()
    vivencia_detalhes_page(empreendimento)
else:
    st.write("Selecione uma das opções acima para explorar os serviços disponíveis.")

# Rodapé
st.markdown("---")
st.markdown("© 2024 - Halsten Incorporadora")
