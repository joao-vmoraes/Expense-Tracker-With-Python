SELECT c.nome as cnome, SUM(compras.valor) from compras
INNER JOIN categorias c ON compras.id_categoria = c.id
GROUP BY id_categoria
ORDER BY SUM(compras.valor) DESC