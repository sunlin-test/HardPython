use newdts;

set names gbk;
CREATE TABLE `gbk_table` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` char(100) NOT NULL COMMENT '名字',
  PRIMARY KEY (`id`),
  UNIQUE KEY `gbk_table__nane` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=gbk COMMENT='gbk编码的表';

insert into gbk_table(`name`) values('鲜花'),('电脑');

set names utf8;
create table `utf8_table_with_gbk_fields`(
    `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
    `name` varchar(128) CHARACTER SET gbk NOT NULL DEFAULT '',
    PRIMARY KEY (`id`),
    KEY `utf8_table_with_gbk_fields__name` (`name`)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='gbk编码的表';

set names gbk;
insert into utf8_table_with_gbk_fields(`name`) values('鲜花'),('电脑');