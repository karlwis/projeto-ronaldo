# Monitoramento de infraestrutura com Zabbix

## Objetivo

Registrar as atividades de instalação, configuração e experimentação do Zabbix no laboratório do Projeto Ronaldo.

## Ambiente

- Sistema operacional: Debian GNU/Linux 13.
- Zabbix Server: versão 8.0.
- Banco de dados: PostgreSQL.
- Implantação: Docker Compose.
- Agente: Zabbix Agent 2.

## Monitoramento implementado

- Monitoramento do sistema operacional Linux.
- Integração do Agent 2 com a API do Docker.
- Descoberta automática de contêineres.
- Coleta de métricas individuais de CPU e memória.
- Monitoramento de disponibilidade dos contêineres.
- Triggers para identificação de contêineres parados.

## Integração com Docker

O Zabbix Agent 2 utiliza o socket Docker para consultar informações sobre os contêineres do ambiente.

A descoberta automática permite acompanhar contêineres em execução e encerrados.

## Testes realizados

Foi criado um contêiner temporário para validar o funcionamento dos alertas.

O teste contemplou:
1. Inicialização do contêiner.
2. Identificação pelo mecanismo de descoberta.
3. Interrupção do contêiner.
4. Disparo do alerta de contêiner parado.
5. Remoção do contêiner e recuperação do alerta.

## Resultado

A integração entre Zabbix Agent 2 e Docker foi validada no ambiente de laboratório.

O monitoramento complementa a observabilidade já implementada com Prometheus e Grafana.
