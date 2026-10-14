# Revisão do TP1 – lista de defeitos (14/10)

Revisão completa do que está na `main`: README, `baixar_dados.py`, os dois CSVs e o `TP1.ipynb`
(texto, código, saídas e os 13 gráficos). Cada afirmação numérica do texto foi recalculada a partir dos CSVs.

**Resumo:** nenhum erro de conta nem item obrigatório faltando. Todos os números citados conferem.
**Atualização 14/10:** todos os itens foram corrigidos no notebook, exceto a reescrita do texto com sua voz.
Além da lista, a correção achou mais um: o G13 mostrava média 59,0 e o texto 58,9 (arredondamento duplo) – corrigido.

Os defeitos eram de **clareza dos gráficos** (alguns não se explicam sozinhos) e de **argumentação**
(afirmações mais fortes do que o gráfico mostra). Marque `[x]` ao corrigir.

## Prioridade alta – pode custar ponto ou ser questionado na defesa

- [x] **G10 (Netflix livre 1 – defasagem) é o gráfico mais confuso.** Tem dois eixos Y (anos e %), barras de
  "% novos" que juntam filmes e séries enquanto as linhas separam por tipo, e o título não diz o que concluir.
  Correção: dois painéis lado a lado: (a) % de títulos "novos" por ano; (b) defasagem por tipo. Título com a
  conclusão: "A Netflix adiciona cada vez mais filmes de acervo".
- [x] **G10 usa média, que é puxada por clássicos.** Filmes em 2021: média 7,7 anos, mas **mediana 3**. Um punhado de
  filmes antigos infla a média. Usar a **mediana** (0 → 3 anos), que conta a mesma história sem esse viés, e
  ajustar o texto ("sobe de 0,4 para 7,7" → usar os valores de mediana).
- [x] **G10/texto: hipótese sobre `release_year` das séries está sem evidência no notebook.** O texto diz que "parece"
  ser o ano da última temporada. A evidência existe: das 14 defasagens negativas (adicionado *antes* de lançar),
  **12 são séries**. Mostrar essa contagem no notebook transforma o "parece" em argumento.
- [x] **G3 (títulos por ano): a queda final engana quem olha só o gráfico.** Nada indica que 2021 está incompleto
  (coleta em set/2021). Marcar 2021 (linha tracejada ou anotação "2021 parcial").
- [x] **Texto 2.5 pula 2019:** diz "pico em 2018 e queda em 2020 e 2021 é esperada", mas a queda começa em 2019
  (1147 → 1030), que é um ano completo. A justificativa "ano incompleto" não explica 2019/2020; a explicação
  correta é que títulos recentes ainda estavam entrando no catálogo (e a pandemia em 2020). Reescrever.
- [ ] **(PENDENTE – só você pode fazer) Texto escrito por IA.** O trabalho é individual com defesa oral: reescrever as interpretações com suas
  palavras e garantir que sabe explicar cada escolha (não preencher ausentes, `explode`, mediana × média, etc.).

## Prioridade média – gráficos que não se explicam sozinhos

- [x] **G5 (histograma de Matemática): as linhas de média (66,1) e mediana (66) ficam uma em cima da outra.**
  A legenda promete duas linhas, o leitor vê uma. Manter só a média, ou dizer na legenda "média ≈ mediana".
  Bom marcar a nota 0 (é só 1 aluno) com uma anotação, já que o texto fala dela.
- [x] **G9 (Leitura × Escrita): o texto afirma o que o gráfico não mostra.** "Pontos azuis ficam mais abaixo da
  diagonal" não dá para ver (1000 pontos em 617 posições, muita sobreposição). O número existe: escrita − leitura
  = **−2,2** para homens e **−0,1** para mulheres. Colocar esse número no título/legenda ou trocar a afirmação.
- [x] **G6 (médias das 3 disciplinas) e G7 (média por gênero): escala 0–100 achata as diferenças.** É honesto
  (barras começam em zero), mas o gráfico sozinho parece dizer "tudo igual". Colocar a conclusão no título
  (ex.: "Matemática tem a menor média, ~3 pontos abaixo de Leitura").
- [x] **Títulos descrevem, não concluem.** Na maioria dos gráficos o título diz *o que* é plotado, não *o que se vê*.
  Para "explicar sozinho", usar o título como conclusão e o subtítulo como descrição (G1–G9).
- [x] **Cores com significados trocados entre gráficos.** Azul = filmes (G1), masculino (G7), matemática (G6),
  "padrão com curso" (G13); vermelho = feminino (G7) e "subsidiado" (G13); verde = leitura (G6) e "com curso" (G8).
  Fixar um mapa de cores por variável (ex.: gênero sempre o mesmo par, curso sempre cinza/verde).
- [x] **G4 (adições por ano):** 32 títulos adicionados antes de 2014 e os 10 sem data foram cortados sem aviso.
  Citar no texto ou rodapé.

## Prioridade baixa – acabamento

- [x] **Grade passa por cima das barras** (G1, G5–G8, G13): `plt.rcParams['axes.axisbelow'] = True` e grade só
  no eixo Y nos gráficos de barras verticais.
- [x] **Separador decimal misturado:** texto usa vírgula (66,1), gráficos usam ponto (66.1, "correlação = 0.95").
  Escolher um padrão (ex.: `locale` ou formatar com `str.replace('.', ',')` nos rótulos).
- [x] **Nomes em inglês nos gráficos** (países no G2; "female/male", "group A–E" e níveis de escolaridade nas tabelas).
  Aceitável, mas traduzir países e categorias deixa o trabalho mais consistente.
- [x] **Saída feia em 2.5:** `por_ano.idxmax(), por_ano.max()` imprime `(np.int64(2018), np.int64(1147))`.
  Trocar por `print(f'Ano com mais títulos: {por_ano.idxmax()} ({por_ano.max()} títulos)')`.
- [x] **G11 (duração por década):** a década de 1960 (n=23) domina a impressão de "queda" no gráfico. O texto já
  ressalva, mas o gráfico pode começar em 1970 ou destacar que 1960 é amostra pequena.
- [x] **Seção 1:** o texto diz "alguns com espaço no início" em `date_added`: são **88** linhas, vale citar o número.

## Conferido e sem problemas

- Todos os itens obrigatórios das seções 1–8 do enunciado estão presentes (8 perguntas Netflix, 10 itens
  Students, 4 + 5 gráficos, 4 perguntas livres com pergunta → tratamento → análise → gráfico → conclusão,
  seção final "Conclusões").
- Números do texto recalculados: tipos, top países/diretores/ratings, décadas, durações, filme mais antigo,
  médias, medianas, aprovados (45,9%), por gênero/curso/escolaridade/grupo, perguntas livres, conclusões.
- Afirmações qualitativas verificadas: Rajiv Chilaka (20 dos 22 títulos são *Chhota Bheem*); Jan Suter e
  Raúl Campos (100% stand-up, México/Argentina/Chile); 91% das séries sem diretor; 1 aluno com nota 0.
- Notebook roda do início ao fim sem erros nem avisos; `baixar_dados.py` reproduz os CSVs byte a byte.
- Nenhum gráfico com eixo truncado, rótulo faltando ou dado errado.
