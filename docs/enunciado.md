# TP1 · enunciado e critérios de avaliação

Trabalho individual de Ciência de Dados 1 (EST/UEA, 2026/02). Entrega em 19/10, defesas em 20 e 22/10.

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
