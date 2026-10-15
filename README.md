# Projeto Ronaldo

Projeto de aprendizado em desenvolvimento de software e DevOps, criado por um iniciante e executado na máquina virtual `ronaldo-test`.

## 1. Sobre o projeto

Ambiente de laboratório para praticar desenvolvimento, testes, conteinerização, integração contínua e qualidade de código.

## 2. Tecnologias e ferramentas

- Python e Django
- Docker e Docker Compose
- Pytest, Coverage.py e Playwright
- Git e GitHub Actions
- Pysonar e SonarQube

## 3. Ambiente de testes

Máquina virtual `ronaldo-test`, com aplicação Django executada em contêiner Docker.

## 4. Execução com Docker Compose

Iniciar a aplicação:

```bash
docker compose up -d --build
```

Verificar os serviços:

```bash
docker compose ps
```

Consultar os logs:

```bash
docker compose logs --tail=30 web
```

Encerrar os serviços:

```bash
docker compose down
```

## 5. Testes e cobertura

Executar os testes:

```bash
pytest
```

Gerar relatório de cobertura:

```bash
pytest --cov=src/myauth --cov-report=term-missing --cov-report=xml:coverage.xml
```

## 6. Integração contínua

Pipeline automatizado com GitHub Actions.

[Consultar execuções](https://github.com/karlwis/projeto-ronaldo/actions)

## 7. Análise estática

Análise com Pysonar e SonarQube, com Quality Gate configurado. A última análise registrada foi aprovada.

## 8. Versionamento

Código-fonte versionado com Git e hospedado no GitHub.

[Repositório Projeto Ronaldo](https://github.com/karlwis/projeto-ronaldo)

## 9. Próximos passos

- Aprimorar o deploy e o versionamento de imagens Docker.
- Estudar monitoramento e observabilidade.
- Praticar orquestração de contêineres.
- Explorar infraestrutura em nuvem.
