# Sistema de Gestão de Peças, Qualidade e Armazenamento

## Descrição do Projeto

Este projeto implementa um sistema de automação digital para gestão de peças industriais, desenvolvido como trabalho acadêmico da disciplina de Algoritmos e Lógica de Programação.

O sistema simula o processo de inspeção automatizada de peças em uma linha de produção, avaliando a qualidade de cada peça com base em critérios técnicos pré-definidos (peso, cor e comprimento). As peças aprovadas são automaticamente armazenadas em caixas com capacidade limitada, enquanto as reprovadas são registradas com seus respectivos motivos de não conformidade.

## Problema Resolvido

Na indústria moderna, a inspeção manual de peças é um processo suscetível a erros humanos, lento e custoso. Este sistema automatiza:

- **Cadastro de peças** com identificação única
- **Avaliação de qualidade** baseada em critérios objetivos
- **Armazenamento inteligente** em caixas com capacidade controlada
- **Rastreabilidade completa** de peças aprovadas e reprovadas
- **Geração de relatórios** para análise gerencial

## Como Funciona

O sistema opera através de um menu interativo no terminal com as seguintes funcionalidades:

1. **Cadastrar nova peça**: Registra uma peça com ID, peso (g), cor e comprimento (cm)
2. **Listar peças**: Exibe todas as peças aprovadas e reprovadas
3. **Remover peça**: Remove uma peça do sistema pelo ID
4. **Listar caixas fechadas**: Mostra todas as caixas que atingiram a capacidade máxima
5. **Gerar relatório final**: Apresenta estatísticas consolidadas do sistema

### Critérios de Qualidade

Uma peça é **APROVADA** quando atende simultaneamente a todos estes critérios:

- **Peso**: entre 95g e 105g (inclusive)
- **Cor**: apenas azul (opção 1) ou verde (opção 2)
- **Comprimento**: entre 10cm e 20cm (inclusive)

Caso contrário, a peça é **REPROVADA** e os motivos são registrados.

### Sistema de Caixas

- Cada caixa armazena no máximo **10 peças aprovadas**
- Quando uma caixa atinge 10 peças, ela é automaticamente **fechada**
- Uma nova caixa é criada para receber as próximas peças aprovadas
- Peças reprovadas **não são armazenadas** em caixas

## Como Rodar o Programa

### Pré-requisitos

- Python 3.6 ou superior instalado no sistema
- Nenhuma biblioteca externa é necessária (usa apenas a biblioteca padrão)

### Passo a Passo

1. **Abra o terminal/prompt de comando** no diretório onde está o arquivo `main.py`

2. **Execute o programa** com o comando:

```bash
python main.py
```

Ou, em alguns sistemas:

```bash
python3 main.py
```

3. **Navegue pelo menu** digitando o número da opção desejada e pressionando ENTER

4. **Para sair**, escolha a opção `0`

## Exemplos de Uso

O sistema fornece feedback visual sobre o progresso de preenchimento das caixas.

### Exemplo 1: Cadastro de Peça Aprovada

```
Digite o ID da peça: P001
Digite o peso da peça (em gramas): 100

Cor da peça:
  1 - Azul
  2 - Verde
Escolha a cor (1 ou 2): 1
Digite o comprimento da peça (em centímetros): 15

✓ Peça cadastrada com sucesso!
  Status: APROVADA
[INFO] Nova caixa criada: Caixa #1
[INFO] Peça #P001 adicionada na Caixa #1 (1/10 peças)
```

### Exemplo 2: Cadastro de Peça Reprovada

```
Digite o ID da peça: P002
Digite o peso da peça (em gramas): 110

Cor da peça:
  1 - Azul
  2 - Verde
Escolha a cor (1 ou 2): 3
⚠ Erro: Digite 1 para azul ou 2 para verde.
Escolha a cor (1 ou 2): 1
Digite o comprimento da peça (em centímetros): 25

✓ Peça cadastrada com sucesso!
  Status: REPROVADA
  Motivos da reprovação:
    - Peso fora da faixa (95g-105g): 110.0g
    - Comprimento fora da faixa (10cm-20cm): 25.0cm
```

### Exemplo 3: Progresso de Preenchimento da Caixa

```
# Cadastrando a 9ª peça
✓ Peça cadastrada com sucesso!
  Status: APROVADA
[INFO] Peça #P009 adicionada na Caixa #1 (9/10 peças)

# Cadastrando a 10ª peça (caixa será fechada)
✓ Peça cadastrada com sucesso!
  Status: APROVADA
[INFO] Peça #P010 adicionada na Caixa #1 (10/10 peças)
[INFO] Caixa #1 FECHADA (capacidade máxima atingida)

# Próxima peça aprovada (nova caixa será criada)
✓ Peça cadastrada com sucesso!
  Status: APROVADA
[INFO] Nova caixa criada: Caixa #2
[INFO] Peça #P011 adicionada na Caixa #2 (1/10 peças)
```

### Exemplo 4: Listagem de Peças

```
✓ PEÇAS APROVADAS:
  ID: P001
    Peso: 100.0g
    Cor: azul
    Comprimento: 15.0cm
    Caixa: #1

  ID: P003
    Peso: 98.0g
    Cor: verde
    Comprimento: 12.0cm
    Caixa: #1

✗ PEÇAS REPROVADAS:
  ID: P002
    Peso: 110.0g
    Cor: vermelho
    Comprimento: 25.0cm
    Motivos da reprovação:
      - Peso fora da faixa (95g-105g): 110.0g
      - Cor inválida (apenas azul ou verde): vermelho
      - Comprimento fora da faixa (10cm-20cm): 25.0cm

Total: 2 aprovadas | 1 reprovadas
```

### Exemplo 5: Relatório Final

```
RELATÓRIO FINAL DO SISTEMA

1. RESUMO GERAL
   Total de peças cadastradas: 15
   Peças aprovadas: 12
   Peças reprovadas: 3

2. MOTIVOS DE REPROVAÇÃO
   Peso fora da faixa: 2 ocorrências
   Cor inválida: 2 ocorrências
   Comprimento fora da faixa: 1 ocorrências

3. INFORMAÇÕES DE ARMAZENAMENTO
   Total de caixas utilizadas: 2
   Caixas fechadas: 1
   Caixas abertas: 1

4. DETALHAMENTO DAS CAIXAS
   Caixa #1 - FECHADA
     Peças armazenadas: 10/10
     IDs: P001, P003, P004, P005, P007, P008, P009, P011, P012, P013
   
   Caixa #2 - ABERTA
     Peças armazenadas: 2/10
     IDs: P014, P015

5. INDICADORES DE QUALIDADE
   Taxa de aprovação: 80.0%
   Taxa de reprovação: 20.0%
```

## Estrutura do Código

O arquivo `main.py` está organizado da seguinte forma:

- **Estruturas de dados**: Listas para armazenar peças e caixas
- **Funções auxiliares**: `limpar_tela()`, `exibir_menu()`
- **Função de avaliação**: `avaliar_peca()` - núcleo da lógica de qualidade
- **Funções de gerenciamento de caixas**: `obter_caixa_aberta()`, `adicionar_peca_na_caixa()`
- **Funções do menu**: Uma função para cada opção do menu
- **Função principal**: `main()` - controla o loop do programa

## Tratamento de Erros

O sistema valida todas as entradas do usuário:

- ✓ IDs duplicados não são permitidos
- ✓ Peso e comprimento devem ser números positivos
- ✓ Opções de menu inválidas são rejeitadas
- ✓ Mensagens claras de erro orientam o usuário

## Autor

Desenvolvido como trabalho acadêmico para a disciplina de Algoritmos e Lógica de Programação.

## Licença

Este projeto foi desenvolvido para fins educacionais.

