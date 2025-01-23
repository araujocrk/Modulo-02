DROP TABLE IF EXISTS escola;
DROP TABLE IF EXISTS diretor;
DROP TABLE IF EXISTS turma;
DROP TABLE IF EXISTS disciplina;
DROP TABLE IF EXISTS professor;
DROP TABLE IF EXISTS aluno;
DROP TABLE IF EXISTS disciplina_aluno;

DROP SCHEMA IF EXISTS ads;
CREATE SCHEMA ads;
SET search_path TO ads;

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
	UNIQUE (id_escola)
);

CREATE TABLE turma (
	id_turma NUMERIC(6,0) PRIMARY KEY,
	nome_turma VARCHAR(20) NOT NULL,
	ano_letivo NUMERIC(4) NOT NULL,
	id_escola NUMERIC(6,0) NOT NULL,
	CONSTRAINT turma_escola_fk FOREIGN KEY (id_escola) REFERENCES escola(id_escola) ON DELETE CASCADE,
	UNIQUE (id_escola) 
);

CREATE TABLE professor (
	id_professor NUMERIC(6,0) PRIMARY KEY,
	nome_professor VARCHAR(40) NOT NULL,
	cpf_professor VARCHAR(11) NOT NULL,
	email_professor VARCHAR(40) NOT NULL,
	telefone_professor VARCHAR(11) NOT NULL
);

CREATE TABLE aluno (
	id_aluno NUMERIC(6,0) PRIMARY KEY,
	nome_aluno VARCHAR(40) NOT NULL,
	data_nasc_aluno DATE NOT NULL,
	nome_responsavel VARCHAR(40) NOT NULL,
	telefone_responsavel VARCHAR(11) NOT NULL
);

CREATE TABLE disciplina (
	id_disciplina NUMERIC(6,0) PRIMARY KEY,
	nome_disciplina VARCHAR(20) NOT NULL,
	id_turma NUMERIC(6,0) NOT NULL,
	id_professor NUMERIC(6,0) NOT NULL,
	id_aluno NUMERIC(6,0) NOT NULL,
	CONSTRAINT disciplina_turma_fk FOREIGN KEY (id_turma) REFERENCES turma(id_turma) ON DELETE CASCADE,
	CONSTRAINT disciplina_professor_fk FOREIGN KEY (id_professor) REFERENCES professor(id_professor) ON DELETE CASCADE,
	CONSTRAINT disciplina_aluno_fk FOREIGN KEY (id_turma) REFERENCES aluno(id_aluno) ON DELETE CASCADE,
	UNIQUE (id_turma, id_professor, id_aluno)
);
