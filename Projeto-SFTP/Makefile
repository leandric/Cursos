SHELL := /bin/bash

PROJECT_NAME := sftp-server
COMPOSE_FILE := docker-compose.yml
DATA_DIR := data-sftp

.PHONY: sftp-up sftp-down sftp-logs sftp-reset sftp-perms

sftp-up:
	@echo "Subindo servidor SFTP..."
	@mkdir -p $(DATA_DIR)
	@chmod -R 777 $(DATA_DIR)
	@docker compose -f $(COMPOSE_FILE) up -d
	@echo ""
	@echo "✅ SFTP rodando:"
	@echo "Host: localhost"
	@echo "Porta: 2222"
	@echo "Usuário: teste"
	@echo "Senha: 123456"
	@echo "Diretório remoto: /upload"
	@echo "Pasta local: ./$(DATA_DIR)"

sftp-down:
	@echo "Parando servidor SFTP..."
	@docker compose -f $(COMPOSE_FILE) down

sftp-logs:
	@echo "Logs do SFTP:"
	@docker compose -f $(COMPOSE_FILE) logs -f

sftp-reset:
	@echo "Resetando ambiente..."
	@docker compose -f $(COMPOSE_FILE) down -v
	@rm -rf $(DATA_DIR)
	@echo "Ambiente limpo."

sftp-perms:
	@echo "Ajustando permissões da pasta de upload..."
	@mkdir -p $(DATA_DIR)
	@chmod -R 777 $(DATA_DIR)
	@echo "Permissões ajustadas com sucesso."