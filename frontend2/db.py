import streamlit as st
from google.cloud import firestore
import random
import string
import json
from google.oauth2 import service_account




def guardar_datos(dato,user):
    
    #nos conectamos a la base de datos 
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project="linkscribe-20b7c")
    
    #cramos un nombre unico
    name = ''.join(random.choices(string.ascii_letters, k=10))

    # Once the user has submitted, upload it to the database
    doc_ref = db.collection("users").document(user)
    doc_ref.set({
            name:dato
                }, merge=True)

# And then render each post, using some light Markdown

def buscar_datos(user):
    
    #nos conectamos a la base de datos 
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project="linkscribe-20b7c")
    
    user_ref = db.collection("users").document(user)


    user_Data = user_ref.get()
    user2 = user_Data.to_dict()


    if user2 is not None:
        # Sidebar para la búsqueda por título
        st.header("Filtrar por Título")
        filtro_titulo = st.text_input("Ingrese el título a buscar:")
        
        # Filtrar datos por título
        datos_filtrados = [dato for dato_id, dato in user2.items() if filtro_titulo.lower() in dato.get("titulo", "").lower()]

        # Mostrar los datos filtrados
        st.header("Datos Filtrados")

        for item in datos_filtrados:
            if st.button(f"Ver Descripción de '{item['titulo'],item['categoria']}' ({item['link']})"):
                st.subheader("Descripción:")
                st.write(item["descripcion"])
    else:
        st.warning("No se encontraron datos para este usuario.")

                                    
#post = posts_ref.get()
#post2 = post.to_dict()
#category = post["category"]
#title = post["title"]
#url = post["url"]
#category = post2["dato2"]["category"]

#st.subheader(f"Post: {title}")
#st.write(f":link: [{url}]({url})")
#st.write(f"category: {category}")
#st.write(f"data: {post2} category {category}")
