# Análise exploratória: Netflix e desempenho escolar

Análise exploratória de duas bases públicas do Kaggle com **Pandas** e **Matplotlib**: o
catálogo da Netflix (8.807 títulos) e as notas de 1.000 estudantes em três provas. Trabalho
prático (TP1) de Ciência de Dados 1, Engenharia da Computação na EST/UEA.

O notebook [`TP1.ipynb`](TP1.ipynb) cobre preparação dos dados, perguntas guiadas, gráficos e
duas investigações livres por base. Enunciado e critérios em [`docs/enunciado.md`](docs/enunciado.md).

## Principais descobertas

**Netflix**
- Sem duplicados; ausentes: `director` 2634 (30%), `country` 831, `cast` 825, `date_added` 10.
- 3 especiais do Louis C.K. tinham a duração em `rating` → corrigido na seção 1.
- 69,6% filmes; EUA em 3690 títulos (Índia 2ª, 1046); TV-MA + TV-14 ≈ 61%; pico de lançamentos em 2018.
- Livre 1: títulos adicionados até 1 ano após o lançamento caem de 82% (2015) para 51% (2021);
  defasagem média dos filmes sobe de 0,4 para 7,7 anos.
- Livre 2: mediana de duração dos filmes cai de ~106–114 min (1970–2000) para 97 min (2010/2020).

**Students**
- Sem ausentes/duplicados; médias Mat 66,1 · Leit 69,2 · Escr 68,1; nota 0 em Matemática.
- 45,9% com média geral ≥ 70; curso preparatório +7,6 pontos; grupo E maior média (72,75).
- Livre 1: gênero inverte por disciplina (homens +5,1 em Mat; mulheres +7,1 Leit e +9,2 Escr).
- Livre 2: almoço subsidiado + curso (67,8) ≈ almoço padrão sem curso (68,3); aprovados 21% → 69%
  entre os extremos.

## Bases (Kaggle, já salvas em `data/`)

Para baixar de novo: `python baixar_dados.py` (não precisa de login no Kaggle).

| Base | Fonte | Arquivo esperado | Esperado |
|------|-------|------------------|----------|
| Netflix Movies and TV Shows | https://www.kaggle.com/datasets/shivamb/netflix-shows | `data/netflix_titles.csv` | ~8807 linhas × 12 colunas |
| Students Performance in Exams | https://www.kaggle.com/spscientist/students-performance-in-exams | `data/StudentsPerformance.csv` | 1000 linhas × 8 colunas |

Usar as versões **oficiais do Kaggle**. Cópias antigas da Netflix (ex.: TidyTuesday 2021,
~7787 linhas) mudam contagens e datas – não usar.

## Como executar

Abra `TP1.ipynb` (VS Code, Jupyter ou Colab), escolha qualquer kernel Python 3 e rode tudo. A primeira
célula prepara o ambiente sozinha:

- se pandas/matplotlib não estiverem no kernel, cria `.venv/` com o mesmo Python, instala o
  `requirements.txt` nele e o usa na sessão (~2 min na primeira vez; depois reaproveita);
- se os CSVs não estiverem em `data/`, roda `baixar_dados.py`.

No VS Code, se ele pedir para instalar o `ipykernel` ao escolher o kernel, aceite. Depois da primeira
execução também dá para escolher o próprio `.venv` como kernel.

## Licença

Código sob [MIT](LICENSE). As bases pertencem aos seus autores no Kaggle.

