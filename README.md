# TP1 – Ciência de Dados 1 (EST – 2026/02)

Análise exploratória de **duas** bases reais com Pandas e Matplotlib.
Entrega: **19/10** · Defesas: 20 e 22/10 · Trabalho **individual**.

> O enunciado não pede para escolher entre as bases: as duas devem ser analisadas.

## Bases (Kaggle, já salvas em `data/`)

Para baixar de novo: `python baixar_dados.py` (não precisa de login no Kaggle).

| Base | Fonte | Arquivo esperado | Esperado |
|------|-------|------------------|----------|
| Netflix Movies and TV Shows | https://www.kaggle.com/datasets/shivamb/netflix-shows | `data/netflix_titles.csv` | ~8807 linhas × 12 colunas |
| Students Performance in Exams | https://www.kaggle.com/spscientist/students-performance-in-exams | `data/StudentsPerformance.csv` | 1000 linhas × 8 colunas |

Usar as versões **oficiais do Kaggle**. Cópias antigas da Netflix (ex.: TidyTuesday 2021,
~7787 linhas) mudam contagens e datas – não usar.

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

Notebook: 8,0 pontos · Defesa: 0 a 1,0 · Nota final = notebook × defesa.

### Detalhamento do enunciado

**1. Netflix – conhecendo os dados:** carregar CSV; nº de linhas/colunas; 5 primeiras e
5 últimas linhas; listar colunas; tipos; valores ausentes por coluna; duplicados;
`describe()` e afins; explicar em texto ≥ 3 características/problemas.

**2. Netflix – investigação** (cada item: código + resultado + breve interpretação):
1. Quantos Movies e quantos TV Shows?
2. Top 10 países com mais produções.
3. Top 10 diretores com mais produções.
4. 5 ratings mais frequentes.
5. Produções lançadas por ano.
6. Década com mais títulos.
7. Só filmes: 10 durações mais frequentes.
8. Filme mais antigo e mais recente.

**3. Netflix – gráficos (Matplotlib, ≥ 4):** Movies × TV Shows; Top 10 países; títulos por
ano; um livre. Todos com título, eixos identificados, legenda quando necessária, bom tamanho.

**4. Students – conhecendo os dados:** carga; `head()`/`tail()`; shape; tipos; ausentes;
duplicados; `describe()`; média e mediana das três notas; explicar ≥ 3 informações do `describe()`.

**5. Students – desempenho:**
1. Média de Matemática, Leitura e Escrita.
2. Mediana de cada disciplina.
3. Disciplina com maior média.
4. Nova coluna `media_geral` (média das três notas).
5. Top 10 estudantes por `media_geral`.
6. % de aprovados (`media_geral` ≥ 70).
7. Média geral por gênero.
8. Média com vs. sem curso preparatório.
9. Média geral por escolaridade dos pais.
10. Grupo (race/ethnicity) com maior média geral.

Sem testes de hipótese – conclusões apenas descritivas.

**6. Students – gráficos (≥ 5, cada um com interpretação textual):** distribuição de
Matemática; médias das 3 disciplinas; média geral por gênero; com/sem curso preparatório;
um livre com descoberta interessante.

**7. Investigação livre:** 2 perguntas próprias por base (4 no total), diferentes das
anteriores e não triviais (contagem direta vale menos). Para cada uma:
pergunta → seleção/tratamento → análise com Pandas → gráfico Matplotlib → conclusão.
Exemplos do professor: participação de países na Netflix ao longo das décadas; efeito do
curso preparatório nas três disciplinas.

**8. Conclusões** (seção final chamada "Conclusões"): ≥ 3 descobertas Netflix; ≥ 3
descobertas estudantes; características das bases que dificultaram; qual base permitiu
análises mais interessantes e por quê; limitações.

## Status / próximos passos

- [x] Estrutura do repositório e plano
- [x] Baixar os dois CSVs do Kaggle para `data/` (14/10, conferidos: 8807×12 e 1000×8)
- [x] `TP1.ipynb` com as 8 seções, executado do início ao fim sem erros (14/10)
- [ ] Revisar o texto com a própria voz e treinar a defesa (20 e 22/10)

## Diário de descobertas

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

## Como executar

```bash
pip install -r requirements.txt
python baixar_dados.py   # só se data/ estiver vazio
jupyter notebook TP1.ipynb
```
