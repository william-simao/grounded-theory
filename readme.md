Este diretório é usado para armazenar os códigos gerados no processamento dos dados da Grounded Theory. O diretório possui as seguintes classes:

- main.py: principal classe do projeto
- normalizer.py: classe para normalização dos dados. Utilizado apenas para verificar se todos os REA foram lidos
- reader.py: classe responsável por ler os REA e armazená-los em uma estrutura de dados
- cleaner.py: classe para realizar a limpeza dos dados (tokenização, lowercase e remoção de caracteres especiais)
- lexical_selection: classe responsável pela análise lexica dos REA
- unsupervised: classe responsável por aplicar as regras de classificação não supervisionadas
- lda: classe responsável pelo algoritmo "Latent Dirichlet Allocation" (LDA)
