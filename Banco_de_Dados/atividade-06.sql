DROP TABLE IF EXISTS funcionarios;
DROP TABLE IF EXISTS departamentos;

DROP SCHEMA IF EXISTS atividade06;

CREATE SCHEMA atividade06;
SET search_path TO atividade06;

CREATE TABLE departamentos (
    numero_departamento NUMERIC(3,0) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE funcionarios (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sexo CHAR(1) CHECK (sexo IN ('M', 'F')),
    salario NUMERIC(10,2),
    numero_departamento NUMERIC(3,0) REFERENCES departamentos(numero_departamento)
);

INSERT INTO departamentos (numero_departamento, nome)
VALUES 
(101, 'Vendas'),
(202, 'Estoque'),
(303, 'Contabilidade');

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES 
('11111111111', 'Ana Costa', 'F', 3000.00, 101),
('11111111112', 'Carlos Souza', 'M', 3200.00, 101),
('11111111113', 'Fernanda Lima', 'F', 3100.00, 101),
('11111111114', 'Gabriel Rocha', 'M', 3300.00, 101),
('11111111115', 'Luiza Martins', 'F', 3400.00, 101),
('22222222221', 'Marcos Silva', 'M', 2500.00, 202),
('22222222222', 'Rafaela Sousa', 'F', 2700.00, 202),
('22222222223', 'Diego Andrade', 'M', 2600.00, 202),
('22222222224', 'Juliana Alves', 'F', 2800.00, 202),
('22222222225', 'Renato Ferreira', 'M', 2900.00, 202),
('33333333331', 'Paula Ramos', 'F', 4000.00, 303),
('33333333332', 'Ricardo Mendes', 'M', 4200.00, 303),
('33333333333', 'Cláudia Nunes', 'F', 4100.00, 303),
('33333333334', 'Eduardo Santos', 'M', 4300.00, 303),
('33333333335', 'Vanessa Rocha', 'F', 4400.00, 303);

SELECT * FROM funcionarios;

SELECT nome, salario FROM funcionarios;

SELECT * FROM funcionarios
WHERE salario >= 3000.00;

SELECT * FROM funcionarios
WHERE sexo = 'M' 
AND salario >= 3000.00;

SELECT * FROM funcionarios
WHERE numero_departamento = 101;

SELECT * FROM funcionarios
WHERE numero_departamento = 202 
AND sexo = 'M';

SELECT * FROM funcionarios
WHERE numero_departamento = 101 
OR numero_departamento = 202;

DELETE FROM funcionarios
WHERE salario >= 4100;

DELETE FROM funcionarios
WHERE numero_departamento = 303 
AND sexo = 'M';

UPDATE funcionarios 
SET salario = 3000
WHERE salario < 3000

UPDATE funcionarios
SET salario = salario + (salario * 0.1)
WHERE numero_departamento = 101;