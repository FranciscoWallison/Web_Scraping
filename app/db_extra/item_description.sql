CREATE TABLE IF NOT EXISTS `item_description` (
  `id` int(11) NOT NULL auto_increment,
  `id_item` int(11) NOT NULL,
  `name_aegis` varchar(24) NOT NULL,
  `nome_traduzido` varchar(30) NOT NULL,
  `description` text,
  `preco` int(11) unsigned DEFAULT NULL,
  `peso` int(11) NOT NULL DEFAULT '',
  `jogado_chao` BOOLEAN,
  `guardado_carrinho` BOOLEAN,
  `negociado` BOOLEAN,
  `vendido_npc` BOOLEAN,
  `colocado_armazem` BOOLEAN,
  `colocado_armazem_guilda` BOOLEAN,
  PRIMARY KEY  (`id`),
  INDEX (`name_aegis`),
  INDEX (`id_item`)
) ENGINE=MyISAM AUTO_INCREMENT=1;