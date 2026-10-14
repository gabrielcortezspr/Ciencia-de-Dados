# TP1 – Ciência de Dados 1 (EST/UEA – 2026/02)

Análise exploratória de **duas** bases reais com Pandas e Matplotlib.
Entrega: **19/10** · Defesas: 20 e 22/10.

> O enunciado não pede para escolher entre as bases: as duas devem ser analisadas.

## Bases

| Base | Fonte | Arquivo | Status |
|------|-------|---------|--------|
| Netflix Movies and TV Shows | https://www.kaggle.com/datasets/shivamb/netflix-shows | `data/netflix_titles.csv` | pendente (baixar do Kaggle) |
| Students Performance in Exams | https://www.kaggle.com/spscientist/students-performance-in-exams | `data/StudentsPerformance.csv` | ok – 1000 linhas × 8 colunas |

## Estrutura do notebook (`TP1.ipynb`) e pontuação

| Seção | Conteúdo | Pontos |
|-------|----------|--------|
| 1 | Netflix – conhecendo e preparando os dados | 1,0 |
| 2 | Netflix – investigação (8 perguntas) | 1,2 |
| 3 | Netflix – visualização (≥ 4 gráficos) | 0,8 |
| 4 | Students – conhecendo e preparando os dados | 1,0 |
| 5 | Students – análise de desempenho (10 itens) | 1,5 |
| 6 | Students – visualização (≥ 5 gráficos) | 1,0 |
| 7 | Investigação livre (2 perguntas por base) | 1,0 |
| 8 | Conclusões | 0,5 |

## Diário de descobertas

- **Students**: sem valores ausentes e sem duplicados. Médias: Matemática 66,1,
  Leitura 69,2, Escrita 68,1. Existe nota 0 em Matemática (possível outlier).

## Como executar

```bash
pip install -r requirements.txt
jupyter notebook TP1.ipynb
```
