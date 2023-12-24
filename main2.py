from typing import List,Optional

from fastapi import FastAPI

from fastapi import HTTPException
from fastapi import status
from FastAPI.models import Curso

app = FastAPI()

cursos = {
  1:{
    "titulo": "programacao para leigos",
    "aulas": 122,
    "horas": 58
  },
  2:{
    "titulo": "programacao para leigos",
    "aulas": 87,
    "horas": 6

  }

}

@app.get('/cursos')
async def get_cursos():
  return cursos



@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
  try:
    curso = cursos[curso_id]
    return curso
  except KeyError:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post('/cursos')
async def post_curso(curso: Curso):
  next_id: int = len(cursos) + 1
  cursos[next_id] = curso
  del curso.id 
  return curso

if __name__ == '__main__':
  import uvicorn

  uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)