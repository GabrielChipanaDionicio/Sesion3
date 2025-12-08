import streamlit as st

# 1. IMPORTANTE: La configuración de página debe ser SIEMPRE lo primero, fuera de las funciones.
st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")

##############
# st.sidebar.image("imagenes/logo_isil_principal.jpg", caption="Actividad #1 | Contenido del Curso")
##############

############################# Pagina 1 ############################## 
def page1(): 
    # Todo el contenido de la función debe estar indentado (con sangría)
    st.title("Desarrollo de la IA | Timeline")
    st.markdown("---")
    
    st.write("Autor: Gabriel Chipana | ISIL")
    st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de la IA.")
    st.markdown("---")
    
    # --- URLs y Definición de Hitos ---
    base_url = "https://raw.githubusercontent.com/GabrielChipanaDionicio/SESION-1-Y-2/main/timeline_images/"
    
    hitos = {
        1: {
            "año": "Finales del S. XX",
            "nombre": "Sistemas de Puntuación de Riesgo (FICO)",
            "concepto": "Implementación de modelos estadísticos para asignar una puntuación de riesgo a individuos.",
            "descripcion": "El desarrollo de modelos como el FICO Score introdujo la metodología de usar datos históricos y algoritmos para evaluar el riesgo en tiempo real.",
            "figura_clave": "Fair Isaac Corporation (FICO) y pioneros de la estadística.",
            "imagen_url": base_url + "timeline1.png"
        },
        2: {
            "año": "Inicios del 2000",
            "nombre": "Autenticación de Doble Factor (2FA)",
            "concepto": "Requerir dos o más factores de verificación para el acceso a cuentas.",
            "descripcion": "Este desarrollo cambió el enfoque de la detección a la prevención activa. Al exigir un segundo código de verificación, se hizo más difícil el fraude.",
            "figura_clave": "Pioneros de la seguridad en banca online y SMS/Token.",
            "imagen_url": base_url + "timeline2.png"
        },
        3: {
            "año": "2000 - 2015",
            "nombre": "Adopción Global del Chip EMV",
            "concepto": "Transición de la banda magnética a tarjetas con un chip criptográfico.",
            "descripcion": "El chip EMV eliminó casi por completo el fraude físico por clonación en el punto de venta.",
            "figura_clave": "Consorcio EMV (Europay, Mastercard, Visa).",
            "imagen_url": base_url + "timeline3.png"
        },
        4: {
            "año": "Década de 2010",
            "nombre": "El Auge de Machine Learning (ML)",
            "concepto": "Uso de algoritmos de Aprendizaje Automático para analizar patrones masivos.",
            "descripcion": "Los modelos de IA y ML superaron las limitaciones de las reglas fijas, procesando ubicación, monto y comportamiento histórico.",
            "figura_clave": "Científicos de datos y equipos de riesgo bancario.",
            "imagen_url": base_url + "timeline4.png"
        },
        5: {
            "año": "Presente",
            "nombre": "Device Fingerprinting",
            "concepto": "Creación de un identificador único basado en características técnicas del dispositivo.",
            "descripcion": "Recopila parámetros técnicos para crear una 'huella' que persiste incluso si el usuario borra cookies.",
            "figura_clave": "Empresas de ciberseguridad y plataformas antifraude.",
            "imagen_url": base_url + "timeline5.png"
        }
    }
    
    # --- Interfaz de Streamlit ---
    opcion = st.slider(
        "Selecciona un punto del timeline",
        min_value=1,
        max_value=5,
        value=1,
        step=1,
        format="HITO N° %d"
    )
    
    st.markdown("---")
    
    # Obtener los datos del hito seleccionado
    data_hito = hitos[opcion]
    
    col1, col2 = st.columns([1, 2.5])
    
    with col1:
        st.header(data_hito["año"])
        st.image(data_hito["imagen_url"], caption=data_hito["nombre"], use_container_width=True)
    
    with col2:
        st.subheader(f":lock: {data_hito['nombre']}")
        st.caption(f"**Concepto Central:** {data_hito['concepto']}")
        st.markdown("---")
        st.write(data_hito["descripcion"])
        st.markdown(f"**🛡️ Actores Clave:** *{data_hito['figura_clave']}*")

############################# Pagina 2 ############################## 
def page2():
    st.title("Resolver ecuaciones de primer grado")
    st.write("Vamos a resolver una ecuación del tipo **ax + b = c**")

    # Definir coeficientes
    a = 3
    b = 5
    c = 20

    st.latex(f"{a}x + {b} = {c}")

    # Resultado correcto
    resultado_correcto = (c - b) / a

    # Input del usuario
    respuesta = st.number_input("Ingresa el valor de x:", step=0.1)

    # Botón para verificar
    if st.button("Verificar resultado"):
        if abs(respuesta - resultado_correcto) < 1e-6:
            st.success("¡Correcto! 🎉")
            st.balloons()
        else:
            st.error("Resultado incorrecto. Intenta nuevamente.")

############################# Pagina 3 ############################## 
def page3():
    st.title("Pendiente")

############################# Pagina 4 ############################## 
def page4():
    st.title("Pendiente")

############################# Pagina 5 ############################## 
def page5():
    st.title("Pendiente")

################################################################### 
######################### Configuracion ###########################     
###################################################################     

page_names_to_funcs = {
    "Grupo 01": page1,
    "Grupo 02": page2,
    "Grupo 03": page3,
    "Grupo 04": page4,
    "Grupo 05": page5,
}

selected_page = st.sidebar.selectbox("Selecciona", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
