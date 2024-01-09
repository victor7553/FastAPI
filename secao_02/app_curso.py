from typing import List,Optional, Any
from typing import Annotated

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import FastAPI
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import Depends

from time import sleep

from fastapi import HTTPException
from fastapi import status
from models import Curso
from models import cursos

def fake_db():
  try:
    print('Abrinco conexão com banco de dados...')
    sleep(1)
  finally:
    print('Fechando a conexão com banco de dados...')
    sleep(1)

app = FastAPI(
  title='API de cursos',
  version='0.0.1',
  description='Uma API para estudos'
  )


# Busca todos os recursos #
@app.get('/cursos', 
         description='Retorna todos os cursos ou uma lista vazia.', 
         summary='Retorna todos os cursos', 
         response_model=List[Curso], 
         response_description='Cursos encontrados com sucesso.')
async def get_cursos(db: Any = Depends(fake_db)):
  return cursos


# Buscar um recurso especifico #
@app.get('/cursos/{curso_id}', description='Retorna um único curso.', summary='Retorna um curso definido')
async def get_curso(curso_id: int = Path(title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3), db: Any = Depends(fake_db)):
  try:
    curso = cursos[curso_id]
    return curso
  except KeyError:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

# Criar um novo recurso #
@app.post('/cursos', description='Adiciona um curso não existente.', summary='Cria um novo curso', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
  next_id: int = len(cursos) + 1
  curso.id = next_id
  cursos.append(curso)
  return curso

# ataulizar um recurso existente #
@app.put('/cursos/{curso_id}', description='Atuliza um curso já existente.', summary='Atualiza curso')
async def put_curso(curso_id:int, curso: Curso, db: Any = Depends(fake_db)):
  if curso_id in cursos:
    cursos[curso_id] = curso
    del curso.id

    return curso
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com esse id {curso_id}')

# Deletar um recurso #
@app.delete('/cursos/{curso_id}', description='Deleta um curso existente.', summary='Deleta curso')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
  if curso_id in cursos:
    del cursos[curso_id]
    #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com esse id {curso_id}')


@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt= 5), b: int = Query(default=None, gt= 10), x_geek: str = Header(default=None), c: Optional[int] = None ):
  soma: int = a + b
  if c:
    soma = soma + c
    
    print(f'X_GEEK: {x_geek}')

    return {'resultado': soma}


if __name__ == '__main__':
  import uvicorn

  uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)