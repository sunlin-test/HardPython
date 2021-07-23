use newdts;
CREATE TABLE IF NOT EXISTS  `all_kinds_of_fields` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `float_field` float NOT NULL,
  `datetime_field` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  `text_field` text NOT NULL,
  `date_field` date NOT NULL,
  `enum_field` enum('sichuang','shanghai','chengdu') NOT NULL DEFAULT 'chengdu',
  `json_field` json NOT NULL,
  `varchar_field` varchar(32) DEFAULT '',
  `timestamp_field` timestamp NULL DEFAULT NULL,
  `blob_field` blob,
  `binary_field` BINARY(128) DEFAULT NULL,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT IGNORE INTO `all_kinds_of_fields` (`id`, `float_field`, `datetime_field`, `text_field`, `date_field`, `enum_field`, `json_field`, `varchar_field`, `timestamp_field`, `blob_field`)
VALUES
	(1,12.12,'2020-03-28 14:56:29','hahah','1992-08-14','sichuang','{\"db\": {\"tables\": [\"t1\"]}}','json','2020-03-27 11:04:11',X'CAFEBABE'),
	(2,1118.1,'2020-03-29 08:26:08','xxxgood','1992-09-01','shanghai','{}','baidu','2020-03-27 11:04:12',X'CAFEBABE');


CREATE TABLE IF NOT EXISTS  `all_kinds_of_fields_1` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `float_field` float NOT NULL,
  `datetime_field` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  `text_field` text NOT NULL,
  `binary_field` BINARY(128) DEFAULT NULL,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

begin;
INSERT IGNORE INTO `all_kinds_of_fields_1`
VALUES
	(1, 12.12,'2020-03-28 14:56:29','hahah', binary('毛球哥'));

UPDATE `all_kinds_of_fields_1` SET `float_field` = 11.11 where id = 1;

UPDATE `all_kinds_of_fields_1` SET `datetime_field` = '2020-02-02 20:10:10' where id = 1;

UPDATE `all_kinds_of_fields_1` SET `text_field` = '1hahah1' where id = 1;

UPDATE `all_kinds_of_fields_1` SET `binary_field` = binary('1毛球哥1') where id = 1;

commit;

begin;
INSERT IGNORE INTO `all_kinds_of_fields_1`
VALUES
	(2, 12.12,'2020-03-28 14:56:29','hahah', binary('毛球哥'));

UPDATE `all_kinds_of_fields_1` SET `binary_field` = binary('2毛球哥2') where id = 2;

UPDATE `all_kinds_of_fields_1` SET `float_field` = 22.22 where id = 2;

UPDATE `all_kinds_of_fields_1` SET `datetime_field` = '2020-02-02 20:20:20' where id = 2;

UPDATE `all_kinds_of_fields_1` SET `text_field` = '2hahah2' where id = 2;

commit;

begin;
INSERT IGNORE INTO `all_kinds_of_fields_1`
VALUES
	(3, 12.12,'2020-03-28 14:56:29','hahah', binary('毛球哥'));

UPDATE `all_kinds_of_fields_1` SET `binary_field` = binary('3毛球哥3') where id = 3;

UPDATE `all_kinds_of_fields_1` SET `float_field` = 33.33 where id = 3;

SET sql_mode=(SELECT replace(@@sql_mode,'NO_ZERO_IN_DATE,NO_ZERO_DATE',''));

UPDATE `all_kinds_of_fields_1` SET `datetime_field` = '2020-02-02 20:30:30' where id = 3;

UPDATE `all_kinds_of_fields_1` SET `text_field` = '3hahah3' where id = 3;

commit;


begin;
INSERT IGNORE INTO `all_kinds_of_fields_1`
VALUES
	(4, 12.12,'2020-03-28 14:56:29','hahah', binary('毛球哥'));

UPDATE `all_kinds_of_fields_1` SET `binary_field` = binary('4毛球哥4') where id = 4;

UPDATE `all_kinds_of_fields_1` SET `float_field` = 44.44 where id = 4;



UPDATE `all_kinds_of_fields_1` SET `datetime_field` = '2020-02-02 20:40:40' where id = 4;

UPDATE `all_kinds_of_fields_1` SET `text_field` = '4hahah4' where id = 4;

commit;


begin;
INSERT IGNORE INTO `all_kinds_of_fields_1`
VALUES
	(5, 12.12,'2020-03-28 14:56:29','hahah', binary('毛球哥'));

UPDATE `all_kinds_of_fields_1` SET `datetime_field` = '2020-02-02 20:50:50' where id = 5;

UPDATE `all_kinds_of_fields_1` SET `text_field` = '5hahah5' where id = 5;

SET NAMES latin1;

UPDATE `all_kinds_of_fields_1` SET `binary_field` = binary('5毛球哥5') where id = 5;

UPDATE `all_kinds_of_fields_1` SET `float_field` = 55.55 where id = 5;

commit;