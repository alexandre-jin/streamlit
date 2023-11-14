from pathlib import Path
import streamlit as st


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.title("Jin Alexandre")
st.write("#")
st.subheader("🙎‍♂️ Profil personnel")
st.write("Actuellement en 2ème année en informatique, j'aimerais travailler dans le domaine des réseaux. Motivé, rigoureux et travailleur.")
st.write("#")
st.subheader("📚 Compétences & langues")
st.write("""
    - Anglais (A2-B1)
    - Réseaux
    - Packet Tracer
    - Linux
    - Golang
    - Java
    - HTML & CSS
    - JavaScript
""")

st.write("#")
tab1, tab2, tab3 = st.tabs(["Routeur virtuelle", "GLPI", "Forum web"])

with tab1:
    st.header("Routeur virtuelle")
    st.image("./images/routeur.PNG")

with tab2:
    st.header("GLPI")
    st.image("./images/GLPI.png")

with tab3:
    st.header("Forum web")
    st.image("./images/forum.png")

st.write("#")
st.subheader("Expériences pédagogiques")

st.subheader("ℹ Informations")
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("""
        - Portable : 06 95 52 49 38
        - E-mail : alexandrejin001@gmail.com
        - Linkedin : https://www.linkedin.com/in/alexandre-jin-758812277/
    """)
with col2:
    st.write("""
        - Âge : 18
        - Zone de recherche : Île-de-France
""")

