# Simulador Produtor-Consumidor com Threads e Semáforos

Este repositório contém um simulador interativo que demonstra os conceitos de **threads**, **semáforos** e **regiões críticas** por meio do clássico problema **Produtor-Consumidor**, modelado como uma fila de impressão.

Desenvolvido em Python para fins didáticos na disciplina de **Sistemas Operacionais** do curso de Engenharia de Computação da USP.

-----

## Objetivo

Tornar compreensível para qualquer pessoa — mesmo sem background técnico — o funcionamento de mecanismos de controle de concorrência, como:

  - Threads
  - Semáforos (`Semaphore`)
  - Locks (`Lock`)
  - Buffers compartilhados

-----

## Como funciona

  - **Produtores** geram pedidos de impressão com nomes e arquivos realistas.
  - **Consumidores** processam os documentos.
  - Um **buffer circular limitado** armazena os itens.
  - O sistema utiliza:
      - `sem_espacos`: controla quantos espaços livres há no buffer.
      - `sem_itens`: indica quantos documentos estão prontos para impressão.
      - `mutex`: garante exclusão mútua no acesso ao buffer.
      - `contador_espacos` e `contador_itens`: ajudam a visualizar o estado dos semáforos.

-----

## Execução Interativa

O programa roda em **modo interativo via terminal**, permitindo que o próprio usuário simule a fila de impressão:

```bash
$ python3 simulador.py
```

Durante a execução:

  - Pressione `e` → envia um documento para a fila
  - Pressione `p` → processa o próximo documento da fila
  - Pressione `q` → encerra o programa

-----

### Exemplo de saída

```
Modo Interativo Iniciado! Pressione:
'e' para enviar impressão  'p' para processar impressão | 'q' para sair

Ação: e
[Você] Enviou 'Maria da Conceição - projeto_final.pdf' para impressão | Buffer: [...]
[Semáforos] Espaços: 4 | Itens: 1
```

-----

### Conceitos Didáticos Abordados

  - Concorrência com múltiplas threads
  - Controle de acesso a recursos compartilhados
  - Problema Produtor-Consumidor
  - Visualização do estado de semáforos
  - Modelagem com filas limitadas

-----

### Estrutura do Código

| Arquivo | Descrição |
| --- | --- |
| `simulador.py` | Código principal com toda a lógica do simulador. |

-----

### Público-Alvo

Este projeto foi pensado para pessoas sem experiência prévia com programação concorrente, incluindo estudantes de outras áreas, curiosos por tecnologia e profissionais de fora da computação.

-----

### Material de Apoio

Este projeto foi acompanhado de:

  - Slides explicativos
  - Vídeo com demonstração e explicação do código
  - Formulário respondido por avaliadores externos

-----

### Créditos

Desenvolvido por:

  - José Manoel Vasconcelos Leopoldo Feitosa
  - Murilo Vinicius da Silva
  - João Marcelo Moreira Trovão Filho
  - Pedro Fuziwara Filho

-----
