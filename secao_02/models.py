from typing import Optional

from pydantic import BaseModel

class Curso(BaseModel):
  id: Optional[int] = None
  titulo: str
  aulas: int 
  horas: int

  
cursos = [
  Curso(id=1, titulo='algoritmo', aulas= 122, horas=58),
  Curso(id=2, titulo='Banco de dados', aulas= 87, horas=6)
]
 
