DROP SCHEMA IF EXISTS ads;
CREATE SCHEMA ads;
SET search_path TO ads;

DROP TABLE IF EXISTS escolas;
DROP TABLE IF EXISTS diretores;
DROP TABLE IF EXISTS alunos;
DROP TABLE IF EXISTS turmas;
DROP TABLE IF EXISTS professores;
DROP TABLE IF EXISTS disciplinas;
DROP TABLE IF EXISTS atividades;

CREATE TABLE escolas (
    id_escola INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE diretores (
    id_diretor INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_escola INT REFERENCES escolas(id_escola)
);

CREATE TABLE turmas (
    id_turma INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_escola INT REFERENCES escolas(id_escola)
);

CREATE TABLE alunos (
    id_aluno INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_escola INT REFERENCES escolas(id_escola)
);

CREATE TABLE professores (
    id_professor INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_escola INT REFERENCES escolas(id_escola)
);

CREATE TABLE disciplinas (
    id_disciplina INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    id_professor INT REFERENCES professores(id_professor)
);

CREATE TABLE atividades (
    id_atividade INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    pontuacao INT NOT NULL,
    id_disciplina INT REFERENCES disciplinas(id_disciplina)
);