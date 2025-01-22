SELECT * FROM aluno;

SELECT nome, carga_horaria FROM disciplina
WHERE carga_horaria > 50;

SELECT d.nome
FROM aluno as a, disciplina as d, matricula as m
WHERE m.aluno_id = 10 AND (m.aluno_id = a.aluno_id) AND (m.disciplina_id = d.disciplina_id);

SELECT a.nome, m.media, m.faltas
FROM aluno as a, disciplina as d, matricula as m
WHERE d.nome = 'Ciências' AND (m.disciplina_id = d.disciplina_id) AND (m.aluno_id = a.aluno_id)
ORDER BY a.nome ASC;

SELECT d.nome, a.nome
FROM aluno as a, disciplina as d, matricula as m
WHERE m.media >= 7 AND (m.aluno_id = a.aluno_id) AND (m.disciplina_id = d.disciplina_id)
ORDER BY d.nome ASC, a.nome ASC;