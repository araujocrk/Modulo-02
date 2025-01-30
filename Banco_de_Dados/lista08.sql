-- 1 Questão
SELECT nome, preco
FROM produtos
WHERE preco > 10.0;

-- 2 Questão
SELECT	p.data_pedido
FROM	pedidos as p, clientes as c
WHERE	c.id_cliente = 2 AND
		c.id_cliente = p.id_cliente;	

-- SUM, AVG, MIN, MAX, COUNT
-- 3 Questão
SELECT	COUNT(*)
FROM	clientes as c, pedidos as p
WHERE	c.id_cliente = 3 AND
		c.id_cliente = p.id_cliente;

-- 4 Questão
SELECT	pro.nome, pp.quantidade, pp.preco_unitario --, pp.id_pedido
FROM	pedidos_produtos as pp, produtos as pro
WHERE	pp.id_pedido = 1 AND
		pp.id_produto = pro.id_produto;


SELECT	SUM(pp.preco_unitario)
FROM	pedidos_produtos as pp, produtos as pro
WHERE	pp.id_pedido = 1 AND
		pp.id_produto = pro.id_produto;

-- 5 Questão
SELECT  COUNT(*)
FROM	clientes as c, pedidos as p
WHERE	c.nome = 'Beltrano' AND
		c.id_cliente = p.id_cliente;

-- 6 Questão
SELECT	SUM(pp.preco_unitario) --pp.preco_unitario, pp.id_pedido
FROM 	pedidos_produtos as pp, produtos as pro
WHERE 	pp.id_pedido = 2 AND
		pp.id_produto = pro.id_produto

-- 7 Questão
SELECT SUM()
FROM pedidos_produtos as pp, produdos as pro
WHERE 