CREATE TABLE IF NOT EXISTS `mob_item_drop` (
  `id` int(11) NOT NULL auto_increment,
  `name_aegis_mob` varchar(24) NOT NULL,
  `name_aegis_item` varchar(24) NOT NULL,
  `type` varchar(39) NOT NULL DEFAULT '',
  `name` varchar(100) NOT NULL DEFAULT '',
  `drop` int(11) unsigned DEFAULT NULL,
  `preco` int(11) NOT NULL DEFAULT '',
  PRIMARY KEY  (`id`),
  INDEX (`name_aegis_mob`),
  INDEX (`name_aegis_item`)
) ENGINE=MyISAM AUTO_INCREMENT=1;