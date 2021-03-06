CREATE TABLE IF NOT EXISTS `mob_description` (
  `id` int(11) NOT NULL auto_increment,
  `name_aegis` varchar(24) NOT NULL,
  `nivel` smallint(5) unsigned DEFAULT NULL,
  `raca` varchar(39) NOT NULL DEFAULT '',
  `propriedade` varchar(39) NOT NULL DEFAULT '',
  `tamanho` varchar(39) NOT NULL DEFAULT '',
  `exp_base` smallint(6) unsigned DEFAULT NULL,
  `exp_classe` smallint(6) unsigned DEFAULT NULL,

  `neutro` smallint(5) unsigned DEFAULT NULL,
  `agua` smallint(5) unsigned DEFAULT NULL,
  `terra` smallint(5) unsigned DEFAULT NULL,
  `fogo` smallint(5) unsigned DEFAULT NULL,
  `vento` smallint(5) unsigned DEFAULT NULL,
  `veneno` smallint(5) unsigned DEFAULT NULL,
  `sagrado` smallint(5) unsigned DEFAULT NULL,
  `sombrio` smallint(5) unsigned DEFAULT NULL,
  `fantasma` smallint(5) unsigned DEFAULT NULL,  
  `maldito` smallint(5) unsigned DEFAULT NULL,
  
  `hp` int(10) unsigned DEFAULT NULL,
  `ataque` varchar(100) NOT NULL DEFAULT '',
  `alcance` smallint(5) unsigned DEFAULT NULL,
  `precisao` smallint(5) unsigned DEFAULT NULL,
  `esquiva` smallint(5) unsigned DEFAULT NULL,
  `def` smallint(5) unsigned DEFAULT NULL,
  `vit` smallint(5) unsigned DEFAULT NULL,
  `defm` smallint(5) unsigned DEFAULT NULL,
  `int` smallint(5) unsigned DEFAULT NULL,
  `for` smallint(5) unsigned DEFAULT NULL,
  `des` smallint(5) unsigned DEFAULT NULL,
  `agi` smallint(5) unsigned DEFAULT NULL,
  `sor` smallint(5) unsigned DEFAULT NULL,
  PRIMARY KEY  (`id`),
  INDEX (`name_aegis`)
) ENGINE=MyISAM AUTO_INCREMENT=1;


-- DROP TABLE  `item_description`;