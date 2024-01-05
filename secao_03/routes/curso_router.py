from fastapi import APIRouter


router = APIRouter()

@router.get('/api/v1/cursos')
async def get_cursos():
  return{"Info": "Todos os cursos"}