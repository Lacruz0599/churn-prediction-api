from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import predict_rouths

app = FastAPI()


origins = [
    "https://churn-predictor-web-app-6vcvxfmwkirzmp6stkngay.streamlit.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    predict_rouths.router,
    prefix='/churn-api/v1')
