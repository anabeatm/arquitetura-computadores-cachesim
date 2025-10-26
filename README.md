# Análise de Desempenho de Cache L1: Impacto da Associatividade vs. Carga de Trabalho

## 🎓 Projeto de Arquitetura de Computadores (Cache Simulator)

Este repositório contém os arquivos de configuração, o executável do simulador e os dados de resultados para o projeto de análise de desempenho da Cache L1. O objetivo central é estudar como a variação da **Associatividade** (organização interna da cache) lida com diferentes **Cargas de Trabalho (Buffer Size)** em um cenário de alto conflito.

---

## 🎯 Tema e Objetivo Central

### Variáveis em Estudo

O experimento foi projetado como um estudo bidimensional, variando os seguintes parâmetros:

1.  **Associatividade (Estrutura da Cache):** 1-way, 2-way, 4-way e 8-way.
2.  **Buffer Size (Carga de Trabalho):** 8KB, 16 KB, 32 KB e 65KB.

### Hipótese

A Associatividade elevada (4-way e 8-way) reduzirá significativamente o **Miss Ratio** e o **Tempo Total (Cycles)** em cenários onde o **Buffer Size** se aproxima da capacidade da cache (32 KB), mitigando os **Misses de Conflito**.

---

## ⚙️ Metodologia e Configurações

### 1. Parâmetros Fixos e Constantes

| Componente | Parâmetro | Valor | Justificativa |
| :--- | :--- | :--- | :--- |
| **Cache (Tamanho)** | Tamanho Total da Cache L1 | **32 KB** | Mantido constante para isolar a Associatividade como única variável estrutural. |
| **Padrão de Acesso** | `stride` (Passo) | **8192** | Valor estratégico que força o **pior cenário de Conflito** na cache 1-way (512 sets x 64 linesize = 32768 B / 4 sets = 8192 B). |
| **Padrão de Acesso** | `write ratio` | 50 | Carga de trabalho balanceada (50% leitura/escrita). |
| **Cache** | `linesize` | 64 | Tamanho do bloco padrão (64 bytes). |
| **Comando** | `número de acessos` | 10000 | Garante estatísticas robustas. |

### 2. Configurações XML (Manutenção do Tamanho Fixo)

Para garantir que a Cache L1 tenha sempre 32 KB, o número de Sets (`<sets>`) foi ajustado de acordo com a Associatividade.

| Arquivo XML | Associatividade (`<assoc>`) | Número de Sets (`<sets>`) |
| :--- | :--- | :--- |
| `assoc_1.xml` | 1-way | **512** |
| `assoc_2.xml` | 2-way | **256** |
| `assoc_4.xml` | 4-way | **128** |
| `assoc_8.xml` | 8-way | **64** |

---

## 💻 Execução dos Testes

O experimento total consiste em **40 execuções** (4 Assocs x 5 Buffers x 2 Padrões de Acesso: `sequential` e `random`).

### 1. Valores Variáveis de Buffer Size

| % da Cache | Tamanho em Bytes | Valor no Comando |
| :--- | :--- | :--- |
| **25%** | 8.192 | 8192 |
| **50%** | 16.384 | 16384 |
| **100%** | 32.768 | 32768 |
| **200%** | 65.536 | 65536 |
| **400%** | 131.072 | 131072 |

### 2. Formato do Comando de Execução

O comando deve seguir o formato abaixo no terminal MSYS2 UCRT64:

```bash
./cache-sim.exe [xml_config] [padrao] [acessos] [buffer_size] [stride] [write_ratio]
