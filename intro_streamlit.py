import streamlit as st

st.title('Ma première application Streamlit')

# Sélecteur de texte
option = st.selectbox('Choisissez une option', ['Option 1', 'Option 2', 'Option 3'])
st.write('Vous avez sélectionné :', option)

# Curseur
valeur = st.slider('Sélectionnez une valeur', 0, 100, 50)
st.write('Valeur sélectionnée :', valeur)

# Af ichage de données tabulaires
import pandas as pd

df = pd.DataFrame({
'Nom': ['Alice', 'Bob', 'Charlie'],
'Âge': [30, 35, 40]
})
st.write(df)


# Af ichage d'un graphique
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graphique de sin(x)')
st.pyplot()


# Changez le thème
st.markdown("""
<style>
body {
background-color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)


# Texte mis en forme
st.markdown('**Gras** :boom:')
st.write('Texte en _italique_.')

