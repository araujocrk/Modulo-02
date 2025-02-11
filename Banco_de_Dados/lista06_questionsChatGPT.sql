-- Listar o nome e salário de todos os funcionários com salário superior a 3.000,00.
SELECT 	f.nome, f.salario
FROM 	funcionarios f
WHERE 	f.salario > 3000
ORDER BY f.salario;

-- Encontrar o nome e o sexo de todos os funcionários que trabalham no departamento de Vendas.
SELECT 	f.nome, f.sexo
FROM 	departamentos d, funcionarios f
WHERE	d.nome = 'Vendas' AND
		d.numero_departamento = f.numero_departamento
ORDER BY f.nome ASC;

-- Contar a quantidade de funcionários que trabalham no departamento de Estoque.
SELECT	COUNT(f.cpf) as funcionarios_estoque
FROM 	departamentos d, funcionarios f
WHERE	d.nome = 'Estoque' AND
		d.numero_departamento = f.numero_departamento;

-- Listar o nome e o salário de todos os funcionários que ganham mais de 4.000,00, 
-- ordenados pelo salário em ordem decrescente.
SELECT 	nome, salario
FROM 	funcionarios
WHERE	salario > 4000
ORDER BY salario DESC;

-- Listar o nome e o número do departamento dos funcionários cujo nome começa com a letra "C".
SELECT	d.nome, f.nome
FROM	funcionarios f, departamentos d
WHERE 	f.nome LIKE 'C%' AND
		d.numero_departamento = f.numero_departamento
ORDER BY d.nome ASC;
	
-- Exibir o salário médio dos funcionários do departamento de Contabilidade.
SELECT 	AVG(f.salario) as media_salario_contabilidade
FROM 	funcionarios f, departamentos d
WHERE 	d.nome = 'Contabilidade' AND
		d.numero_departamento = f.numero_departamento;

-- Contar quantos funcionários são do sexo feminino.
SELECT 	COUNT(sexo) as qtd_funcionarias
FROM 	funcionarios
WHERE 	sexo = 'F';