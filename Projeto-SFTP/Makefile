SHELL := /bin/bash

PROJECT_NAME := sftp-server
COMPOSE_FILE := docker-compose.yml

.PHONY: sftp-up sftp-down sftp-logs sftp-reset

sftp-up:
	@echo "Subindo servidor SFTP..."
	@mkdir -p data-sftp
	@chmod -R 755 data-sftp
	@docker compose -f $(COMPOSE_FILE) up -d
	@echo ""
	@echo "✅ SFTP rodando:"
	@echo "Host: localhost"
	@echo "Porta: 2222"
	@echo "Usuário: teste"
	@echo "Senha: 123456"
	@echo "Diretório remoto: /upload"
	@echo "Pasta local: ./data-sftp"

sftp-down:
	@echo "Parando servidor SFTP..."
	@docker compose -f $(COMPOSE_FILE) down

sftp-logs:
	@echo "Logs do SFTP:"
	@docker compose -f $(COMPOSE_FILE) logs -f

sftp-reset:
	@echo "Resetando ambiente..."
	@docker compose -f $(COMPOSE_FILE) down -v
	@rm -rf data-sftp
	@echo "Ambiente limpo."