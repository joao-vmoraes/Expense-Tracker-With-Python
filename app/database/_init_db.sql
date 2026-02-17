-- iNITIALIZATION OF THE DATABASE

CREATE TABLE IF NOT EXISTS `categorias` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `nome` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO categorias (nome) VALUES
	('Alimentaaoo'),
	('Transporte'),
	('Lazer'),
	('Saude'),
	('Moradia'),
	('Outros');


-- dados_db.Compra definition


CREATE TABLE IF NOT EXISTS `compra` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `id_categoria` int unsigned NOT NULL,
    `nome` varchar(30) NOT NULL,
    `valor` decimal(8,2) NOT NULL,
    `data` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `Compra_categorias_FK` (`id_categoria`),
    CONSTRAINT `Compra_categorias_FK` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;