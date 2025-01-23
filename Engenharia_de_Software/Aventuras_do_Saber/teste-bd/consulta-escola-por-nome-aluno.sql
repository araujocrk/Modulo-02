SELECT e.nome 
FROM escolas as e, turma as t, disciplina_aluno as da, disciplina as d, aluno as a
WHERE a.nome = 'Ryan' AND (da.aluno_id_disciplina = a.id_aluno) AND (da.disciplina_id_aluno = d.id_disciplina)
AND d.id_turma = t.id_turma AND t.id_escola = e.id_escola;