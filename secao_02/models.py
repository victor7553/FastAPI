from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
  id: Optional[int] = None
  titulo: str
  aulas: int 
  horas: int

  @validator('titulo')
  def validar_titulo(cls, value: str):
      palavras = value.split(' ')
      if len(palavras) < 1:
        raise ValueError('O título deve conter pelo menos 3 palavras')

      if value.islower():
         raise ValueError('O titulo deve comecar com letra maiuscula.')

      return value
  
  # @validator('aulas')
  # def validar_aulas(cls, value):
  #    aulas = value
  #    if len(aulas) > 134:
  #       raise ValueError('Grade de aulas errada')
  
cursos = [
  Curso(id=1, titulo='Algoritmo', aulas= 122, horas=58),
  Curso(id=2, titulo='Banco de dados', aulas= 87, horas=6)
]
 
