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

INSERT INTO professores (id_professor, nome, id_disciplina)
VALUES
(1, 'Getúlio', )