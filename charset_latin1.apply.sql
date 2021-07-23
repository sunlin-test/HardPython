use newdts;

set names latin1;
CREATE TABLE `latin1_table` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` char(100) NOT NULL COMMENT '名字',
  PRIMARY KEY (`id`),
  UNIQUE KEY `latin1_table__nane` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1 COMMENT='latin1编码的表';

insert into latin1_table(`name`) values("鲜花"),("电脑");

set names utf8;
create table `utf8_table_with_latin1_fields`(
    `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
    `name` varchar(128) CHARACTER SET latin1 NOT NULL DEFAULT '',
    PRIMARY KEY (`id`),
    KEY `utf8_table_with_latin1_fields__name` (`name`)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='utf8编码的表中包含latin1';

set names latin1;
insert into utf8_table_with_latin1_fields(`name`) values("鲜花"),("电脑");