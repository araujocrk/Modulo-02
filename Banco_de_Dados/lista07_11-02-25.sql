-- 1. Listar todos os alunos com seus respectivos ids, nomes e datas de nascimento
SELECT 	a.aluno_id, a.nome, a.data_nascimento
FROM 	aluno a
ORDER BY a.nome ASC;

-- 2. Exibir o nome e a carga horária das disciplinas com carga horária superior a 50 horas.
SELECT 	nome, carga_horaria
FROM 	disciplina
WHERE 	carga_horaria > 50
ORDER BY carga_horaria ASC;

-- 3. Mostrar as disciplinas nas quais o aluno com ID 10 está matriculado.
SELECT 	d.nome
FROM 	matricula m, disciplina d
WHERE 	m.aluno_id = 10 AND
		m.disciplina_id = d.disciplina_id;

-- 4. Listar o nome, as médias e faltas de todos os alunos em uma disciplina específica (ex:
-- Matemática) ordenados por nome.
SELECT	m.aluno_id, a.nome, m.faltas, m.media
FROM 	aluno a, matricula m, disciplina d
WHERE	d.nome = 'Matemática' AND
		m.disciplina_id = d.disciplina_id AND
		m.aluno_id = a.aluno_id
ORDER BY a.nome ASC;

-- 5. Listar, para todas as disciplinas, o nome da disciplina e o nome do aluno com média maior
-- ou igual a 7 naquela disciplina, com agrupamento por aluno.
SELECT	a.aluno_id, a.nome, d.nome, m.media
FROM 	aluno a, matricula m, disciplina d
WHERE 	m.media >= 7 AND
		m.aluno_id = a.aluno_id AND
		m.disciplina_id = d.disciplina_id
ORDER BY a.nome ASC;
