CREATE DATABASE IF NOT EXISTS consultoria_db
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

USE consultoria_db;

CREATE TABLE IF NOT EXISTS contatos_consultoria (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nome VARCHAR(150) NOT NULL,
  email VARCHAR(254) NOT NULL,
  telefone VARCHAR(30),
  data_contato DATE NOT NULL,
  estado CHAR(2) NOT NULL,
  sobre TEXT,
  origem VARCHAR(100),                 -- opcional: onde veio o lead (site, anuncio, etc.)
  status ENUM('novo','em_andamento','arquivado') NOT NULL DEFAULT 'novo',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY ux_email_data (email, data_contato),
  INDEX idx_data_contato (data_contato),
  INDEX idx_estado (estado),
  INDEX idx_status (status)
) ENGINE = InnoDB;