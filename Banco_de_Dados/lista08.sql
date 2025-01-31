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


SELECT	pp.id_pedido, SUM(pp.preco_unitario) as preco_total
FROM	pedidos_produtos as pp, produtos as pro
WHERE	pp.id_pedido = 1 AND
		pp.id_produto = pro.id_produto
GROUP BY pp.id_pedido;

-- 5 Questão
SELECT  COUNT(p.id_pedido)
FROM	clientes as c, pedidos as p
WHERE	c.nome = 'Beltrano' AND
		c.id_cliente = p.id_cliente;

-- 6 Questão
--SELECT pp.id_pedido, pp.preco_unitario, pp.quantidade, 
--SUM(pp.preco_unitario * pp.quantidade) as preco_total_pedido
SELECT  SUM(pp.preco_unitario * pp.quantidade) as preco_total_pedido
FROM 	pedidos_produtos as pp, produtos as pro
WHERE 	pp.id_pedido = 2 AND
		pp.id_produto = pro.id_produto;
--GROUP BY pp.id_pedido, pp.preco_unitario, pp.quantidade;

-- 7 Questão
SELECT	SUM(pp.quantidade * pp.preco_unitario) as preco_total_pedidos
FROM	pedidos as ped, pedidos_produtos as pp
WHERE	ped.id_cliente = 1 AND
		ped.id_pedido = pp.id_pedido;