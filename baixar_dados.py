"""Baixa as duas bases oficiais do Kaggle para data/.

Uso: python baixar_dados.py
Não precisa de login: usa o endpoint público de download do Kaggle.
"""
import io
import urllib.request
import zipfile
from pathlib import Path

DATA = Path(__file__).parent / "data"

BASES = {
    "shivamb/netflix-shows": "netflix_titles.csv",
    "spscientist/students-performance-in-exams": "StudentsPerformance.csv",
}

for slug, arquivo in BASES.items():
    url = f"https://www.kaggle.com/api/v1/datasets/download/{slug}"
    with urllib.request.urlopen(url) as resp:
        conteudo = resp.read()
    with zipfile.ZipFile(io.BytesIO(conteudo)) as z:
        (DATA / arquivo).write_bytes(z.read(arquivo))
    print(f"{slug} -> data/{arquivo}")
