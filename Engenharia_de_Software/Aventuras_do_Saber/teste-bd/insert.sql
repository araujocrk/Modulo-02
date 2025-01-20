INSERT INTO escolas (id_escola, nome)
VALUES 
(1, 'Nova Geração'),
(2, 'Mãe Rainha');

INSERT INTO diretores (id_diretor, nome, id_escola)
VALUES
(1, 'Auxiliadora', 1),
(2, 'Margarida', 1),
(3, 'Arthur', 2);

INSERT INTO turmas (id_turma, nome, id_escola)
VALUES 
(1, '1º ano - Nova Geração', 1),
(2, '2º ano - Nova Geração', 1),
(3, '1º ano - Mãe Rainha', 2),
(4, '2º ano - Mãe Rainha', 2);

INSERT INTO alunos (id_aluno, nome, id_escola)
VALUES
(1, 'Pedro', 1),
(2, 'Gabriel', 1),
(3, 'Mônica', 1),
(4, 'Sávio', 2),
(5, 'Júlia', 2),
(6, 'Stephany', 2);

INSERT INTO professores (id_professor, nome, id_escola)
VALUES 
(1, 'Getúlio', 1),
(2, 'Desterro', 1),
(3, 'Márcia', 2),
(4, 'Eudijane', 2),

INSERT INTO disciplinas (id_disciplina, nome, id_professor)
VALUES
(1, 'Matemática', 1),
(2, 'Português', 2),
(3, 'Matemática', 3),
(4, 'Português', 4);

INSERT INTO atividades (id_atividade, nome, pontuacao, id_disciplina)
VALUES
(1, 'O Leão e o Rato', 0, )