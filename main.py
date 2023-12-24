
from fastapi import FastAPI

app = FastAPI()


@app.get("/mensagem")
def mensagem():
    return {"Hello": "ola victor hugo"}


# executando o arquivo direto = python main.py
# liberando a rota pra qualquer usuario

# if __name__ == '__main__':
#     import uvicorn

#     uvicorn.run("main.app", host="0.0.0.0", port=8000, log_level="info", reload=True)