# 🧠 Churn Prediction API

Esta API fue desarrollada con **FastAPI** y tiene como objetivo predecir la probabilidad de que un cliente abandone un servicio (churn), utilizando un modelo de machine learning previamente entrenado. Está diseñada para ofrecer respuestas rápidas y precisas, facilitando la toma de decisiones estratégicas basadas en datos.

## 📌 Objetivo

El propósito de esta API es exponer un modelo de clasificación que evalúa el riesgo de churn a partir de datos específicos del cliente. Permite que **aplicaciones web**, **sistemas internos** o **tableros analíticos** envíen solicitudes con información relevante de clientes y reciban una predicción inmediata sobre su probabilidad de abandono.

Esta solución está pensada para integrarse de forma sencilla en pipelines de datos o flujos de trabajo de análisis, contribuyendo a estrategias de **retención de clientes**, segmentación proactiva y optimización de campañas de fidelización.

## ⚙️ Tecnologías utilizadas

- Python 3.10+
- FastAPI
- Scikit-Learn
- Uvicorn
- Pandas / NumPy
- Pydantic (para validación de datos)
- Joblib (para cargar el modelo entrenado)

## 🚀 Instalación y ejecución local

```bash
# 1. Clona el repositorio
git clone https://github.com/cesareduardo/churn-prediction-api.git
cd churn-prediction-api

# 2. Crea un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Ejecuta la API
uvicorn main:app --reload
```

La API estará disponible en:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Documentación automática disponible en:  
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🧪 Cómo usar la API

### Endpoint principal: `/churn-api/v1/predict/list`

**Método**: `POST`  
**Descripción**: Recibe los datos de un cliente y devuelve una predicción (`0` o `1`) junto con la probabilidad de churn.

**Ejemplo de solicitud:**

```json
POST /predict
Content-Type: application/json

{
    "clients": [
        {
            "days": 22,
            "is_month_to_month": 1,
            "is_optical_fiber": 1,
            "is_electronic_check": 1,
            "internet": 1
        },
        {
            "days": 488,
            "is_month_to_month": 0,
            "is_optical_fiber": 0,
            "is_electronic_check": 0,
            "internet": 1
        }
    ]
}
```

**Ejemplo de respuesta:**

```json
{
    "predictions": [
        {
            "prediction": 1,
            "probability": 0.567523793287211
        },
        {
            "prediction": 0,
            "probability": 0.020939054214131975
        }
    ]
}
```

## 🔗 Enlaces Relacionados

-  **App Web del modelo**: [Repositorio de la app](https://github.com/Lacruz0599/Churn-Predictor-Web-App)
-  **Modelo de Ml usado en la api**: [Predicción De Abandono De Clientes Telecom](https://github.com/Lacruz0599/prediccion-de-abandono-de-clientes-Telecom)


## 📬 Contacto

César Eduardo Cruz Cabrera  
📧 cesareduardocruzcabrera@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/cesar-eduardo-cruz-cabrera)

---

Este proyecto es parte de mi portafolio como científico de datos en formación.  
¡Gracias por visitar!
```
