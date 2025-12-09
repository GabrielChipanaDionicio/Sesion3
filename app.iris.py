import streamlit as st
import joblib

############################# Barra Lateral##############################    

st.sidebar.image("imagenes/bcp_logo.png", caption="Aplicación de Modelo de Clasificación | Despliegue en Streamlit")

#############################Pagina 1##############################    

def page1():
    st.header('Predicción del dataset Iris 🍀', divider='rainbow')
    
    st.info("Dr. Jesus Alvarado Huayhuaz") 
    
    st.write("""
    El dataset Iris es uno de los conjuntos de datos más conocidos y utilizados en estadística, reconocimiento de patrones e inteligencia artificial. Fue introducido por el botánico y estadístico Ronald A. Fisher en 1936, en su artículo “The Use of Multiple Measurements in Taxonomic Problems”. Su objetivo original era demostrar el uso del análisis discriminante para clasificar especies de plantas a partir de mediciones morfológicas.
    
    El dataset contiene un total de 150 muestras de flores de iris, divididas equitativamente en tres especies:
    
    - Iris setosa
    
    - Iris versicolor
    
    - Iris virginica
    """ )
    
    st.image("imagenes/iris_dataset.png",
                     caption="Dataset Iris")
    
    st.write("""
    Para cada flor se registraron cuatro características morfométricas, medidas en centímetros:
    
    - Longitud del sépalo (sepal length)
    
    - Ancho del sépalo (sepal width)
    
    - Longitud del pétalo (petal length)
    
    - Ancho del pétalo (petal width)
    
    Estas mediciones fueron tomadas originalmente en la década de 1930 a partir de especímenes reales recolectados para estudios botánicos. Fisher utilizó este conjunto para ilustrar cómo las variables cuantitativas permiten separar estadísticamente especies a través de técnicas de clasificación.
    Actualmente, el dataset Iris es ampliamente usado para:
    
    1. Enseñanza de aprendizaje supervisado,
    
    2. Pruebas de modelos de clasificación,
    
    3. Demostraciones de técnicas estadísticas,
    
    4. Ejercicios iniciales de machine learning y visualización de datos.
    
    Su simplicidad, tamaño reducido y separabilidad parcial entre clases lo convirtieron en un estándar académico para introducir conceptos clave de la inteligencia artificial y el reconocimiento de patrones.
    """)

#############################Pagina 2##############################    

def page2():
    st.header('Predicción del dataset Iris 🍀', divider='rainbow')
    
    st.info("Dr. Jesus Alvarado Huayhuaz")
    
    st.image("imagenes/iris_dataset.png", caption="Dataset Iris")
    
    st.write("Ingresa las características de la flor:")

    iris_target_names = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }
    
    # ============================
    # Cargar modelos Iris
    # ============================
    
    knn_model = joblib.load('./model/modelo_iris_knn.pkl')
    svm_model = joblib.load('./model/modelo_iris_svm.pkl')
    tree_model = joblib.load('./model/modelo_iris_arbol.pkl')
    
    # Campos de entrada numéricos
    sepal_length = st.number_input('sepal length (cm)', min_value=0.0, max_value=10.0, step=0.1, value=5.9)
    sepal_width = st.number_input('sepal width (cm)', min_value=0.0, max_value=10.0, step=0.1, value=3.0)
    petal_length = st.number_input('petal length (cm)', min_value=0.0, max_value=10.0, step=0.1, value=5.0)
    petal_width = st.number_input('petal width (cm)', min_value=0.0, max_value=10.0, step=0.1, value=1.8)
    
    # Selección de modelos
    st.write("Selecciona los modelos que deseas usar para la predicción:")
    use_knn = st.checkbox("KNN")
    use_svm = st.checkbox("SVM")
    use_tree = st.checkbox("Árbol de Decisión")
    
    # Botón de predicción
    if st.button("Predecir"):
        features = [[sepal_length, sepal_width, petal_length, petal_width]]
    
        if not (use_knn or use_svm or use_tree):
            st.warning("Selecciona al menos un modelo.")
        else:
            st.write("### Resultados de la predicción")
    
            # KNN
            if use_knn:
                pred_knn = knn_model.predict(features)[0]
                #st.write(f"**KNN Predicción:** {pred_knn}")
                st.write(f"**KNN Predicción:** {pred_knn} ({iris_target_names[pred_knn]})")
    
    
            # SVM
            if use_svm:
                pred_svm = svm_model.predict(features)[0]
                #st.write(f"**SVM Predicción:** {pred_svm}")
                st.write(f"**SVM Predicción:** {pred_svm} ({iris_target_names[pred_svm]})")
    
    
            # Árbol de decisión
            if use_tree:
                pred_tree = tree_model.predict(features)[0]
                #st.write(f"**Árbol de Decisión Predicción:** {pred_tree}")
                st.write(f"**Árbol de Decisión Predicción:** {pred_tree} ({iris_target_names[pred_tree]})")



#############################Pagina 3##############################    

def page3():
    st.header('Glosario 🍀')    
    
    st.write("""

    1. KNN (K-Nearest Neighbors): Algoritmo de clasificación que predice la clase de un punto según las clases de sus vecinos más cercanos.
    
    2. SVM (Support Vector Machine): Clasificador que busca un hiperplano óptimo que separe las clases con el mayor margen posible.
    
    3. Árbol de decisión: Modelo que clasifica datos mediante una estructura de nodos y ramas basados en preguntas sobre las características.
    
    4. Joblib: Librería de Python para guardar y cargar objetos de manera eficiente, como modelos entrenados.
    
    5. Sklearn (scikit-learn): Biblioteca de Python para machine learning, que incluye algoritmos, métricas y utilidades de preprocesamiento.
    
    6. IRIS: Dataset clásico de flores de iris usado para clasificación, con 150 muestras y 4 características (sépalos y pétalos) de 3 especies.

    """)
    
################################################################### 
##########################Configuracion############################    
################################################################### 

page_names_to_funcs = {
  "El dataset": page1,
  "Predicciones": page2,
  "Glosario": page3,
}

selected_page = st.sidebar.selectbox("Selecciona", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
