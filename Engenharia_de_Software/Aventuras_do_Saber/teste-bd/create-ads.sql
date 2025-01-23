DROP TABLE IF EXISTS escola;
DROP TABLE IF EXISTS diretor;
DROP TABLE IF EXISTS turma;
DROP TABLE IF EXISTS disciplina;
DROP TABLE IF EXISTS professor;
DROP TABLE IF EXISTS aluno;
DROP TABLE IF EXISTS disciplina_aluno;

DROP SCHEMA IF EXISTS ads-bd;
SET search_path TO ads-bd;

CREATE TABLE escola (
	id_escola NUMERIC(6,0) PRIMARY KEY,
	nome_escola VARCHAR(40) NOT NULL,
	endereco_escola VARCHAR(40) NOT NULL,
	telefone_escola VARCHAR(11) NOT NULL
);

CREATE TABLE diretor (
	id_diretor NUMERIC(6,0) PRIMARY KEY,
	nome_diretor VARCHAR(40) NOT NULL,
	cpf_diretor VARCHAR(11) NOT NULL,
	email_diretor VARCHAR(40) NOT NULL,
	telefone_diretor VARCHAR(11) NOT NULL,
	id_escola NUMERIC(6,0) NOT NULL,
	CONSTRAINT diretor_escola_fk FOREIGN KEY (id_escola) REFERENCES escola(id_escola) ON DELETE CASCADE,
	UNIQUE id_escola
);

CREATE TABLE turma (
	id_turma NUMERIC(6,0) PRIMARY KEY,
	nome_turma VARCHAR(20) NOT NULL,
	ano_letivo NUMERIC(4) NOT NULL,
	id_escola NUMERIC(6,0) NOT NULL,
	CONSTRAINT turma_escola_fk FOREIGN KEY (id_escola) REFERENCES escola(id_escola) ON DELETE CASCADE,
	UNIQUE id_escola
);

CREATE TABLE disciplina (
	id_disciplina NUMERIC(6,0) PRIMARY KEY,
	nome_disciplina VARCHAR(20) NOT NULL,
	id_turma NUMERIC(6,0) NOT NULL,
	id_professor NUMERIC(6,0) NOT NULL,
	id_aluno NUMERIC(6,0) NOT NULL,
	CONSTRAINT 
);

CREATE TABLE professor (
	id_professor NUMERIC(6,0) PRIMARY KEY,
	nome_professor VARCHAR(40) NOT NULL,
	cpf_professor VARCHAR(11) NOT NULL,
	email_professor VARCHAR(40) NOT NULL,
	telefone_professor VARCHAR(11) NOT NULL,
)