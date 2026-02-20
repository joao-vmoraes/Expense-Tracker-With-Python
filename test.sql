SELECT  compras.nome as cnome, ca.nome AS categoria_nome,  valor, data ,compras.id as coid FROM compras
INNER JOIN categorias ca ON compras.id_categoria = ca.id;