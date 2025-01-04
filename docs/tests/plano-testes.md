# Plano de Teste

**Nome do Sistema:** EventSync
**Versão:** 1.0

## Histórico das Alterações

| Data       | Versão | Descrição         | Autor(a)              |
|------------|--------|-------------------|-----------------------|
| 26/11/2024 | 1.0    | Release inicial   | Vinícius Maia Marinho |

---

## 1 - Introdução

Este documento detalha o plano de teste do sistema **EventSync**, abrangendo os requisitos a testar, tipos de teste aplicados, recursos necessários e cronograma das atividades de teste. O objetivo é assegurar que o sistema atende aos requisitos funcionais e não funcionais estabelecidos, garantindo a qualidade final do produto.

---

## 2 - Requisitos a Testar

### Casos de Uso

| Identificador do Caso de Uso | Nome do Caso de Uso                     |
|------------------------------|-----------------------------------------|
| UC1                         | Cadastro de eventos                    |
| UC2                         | Visualização de eventos sincronizados  |
| UC3                         | Alteração de detalhes do evento        |
| UC4                         | Exclusão de eventos                    |

### Requisitos Não-Funcionais

| Identificador do Requisito | Nome do Requisito                    |
|----------------------------|--------------------------------------|
| RNF1                       | Tempo de resposta < 2 segundos      |
| RNF2                       | Persistência de dados após falhas   |
| RNF3                       | Compatibilidade com navegadores modernos |

---

## 3 - Tipos de Teste

### 3.1 - Métodos da Classe

- **Objetivo:** Verificar se os métodos de cada classe retornam os valores esperados.
- **Técnica:** (x) manual (x) automática
- **Estágio do Teste:** Unidade (x)
- **Abordagem do Teste:** Caixa branca (x) Caixa preta (x)
- **Responsáveis:** Programadores ou equipe de testes

### 3.2 - Persistência de Dados

- **Objetivo:** Validar se os dados persistem após falhas ou desligamentos inesperados.
- **Técnica:** (x) manual (x) automática
- **Estágio do Teste:** Sistema (x)
- **Abordagem do Teste:** Caixa preta (x)
- **Responsáveis:** Programadores ou equipe de testes

### 3.3 - Integração dos Componentes

- **Objetivo:** Verificar a interação correta entre os componentes do sistema.
- **Técnica:** (x) manual (x) automática
- **Estágio do Teste:** Integração (x)
- **Abordagem do Teste:** Caixa branca (x) Caixa preta (x)
- **Responsáveis:** Programadores ou equipe de testes

### 3.4 - Tempo de Resposta

- **Objetivo:** Garantir que o sistema responde às solicitações dentro do tempo estipulado (< 2 segundos).
- **Técnica:** ( ) manual (x) automática
- **Estágio do Teste:** Sistema (x)
- **Abordagem do Teste:** Caixa preta (x)
- **Responsáveis:** Programadores ou equipe de testes

---

## 4 - Recursos

### 4.1 - Ambiente de Teste (Hardware e Software)

- **Hardware:**
  - Processador: Intel Core i5 ou superior
  - Memória RAM: 16 GB
  - Armazenamento: 256 GB SSD

- **Software:**
  - Sistema Operacional: Linux Manjaro
  - Navegadores: Chrome, Firefox, Edge
  - Banco de Dados: PostgreSQL 15

### 4.2 - Ferramentas de Teste

- **Ferramentas Utilizadas:**
  - Django Rest Testing
  - Insomnia para testes de API

---

## 5 - Cronograma

| Tipo de Teste        | Duração | Data de Início | Data de Término |
|-----------------------|---------|----------------|-----------------|
| Planejar teste        | 2 dias  | 26/11/2024     | 28/11/2024      |
| Projetar teste        | 3 dias  | 29/11/2024     | 01/12/2024      |
| Implementar teste     | 5 dias  | 02/12/2024     | 06/12/2024      |
| Executar teste        | 7 dias  | 07/12/2024     | 14/12/2024      |
| Avaliar teste         | 3 dias  | 15/12/2024     | 17/12/2024      |

---
