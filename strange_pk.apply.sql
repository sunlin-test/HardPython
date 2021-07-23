use newdts;

CREATE TABLE `strange_pk_string` (
  `uniq_id` varchar(32)  NOT NULL,
  `name` varchar(64) NOT NULL DEFAULT '',
  PRIMARY KEY (`uniq_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `strange_pk_string` (`uniq_id`, `name`)
VALUES
	('0\' or 1>\'1', 'inject'),
	('select', 'select'),
	('some\\\"', 'hello'),
	('with\"', 'apple'),
	('with\'', 'ajax');


CREATE TABLE `strange_pk_text` (
  `uniq_id` TEXT NOT NULL,
  `name` varchar(64) NOT NULL DEFAULT '',
  PRIMARY KEY (`uniq_id`(16))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `strange_pk_text` (`uniq_id`, `name`)
VALUES
('0\' or 1>\'1', 'inject'),
('select f1,f2,f3,f4,f5,f6,f7,f8,f9 from create_view order by id desc limit 100', 'select'),
('some\\\"', 'hello'),
('with\"', 'apple'),
('with\'', 'ajax');

CREATE TABLE `strange_pk_blob` (
  `uniq_id`  BLOB NOT NULL,
  `name` varchar(64) NOT NULL DEFAULT '',
  PRIMARY KEY (`uniq_id`(16))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `strange_pk_blob` ( `uniq_id`,`name`)
VALUES (X'CAFEBABE51939272ABE65E182AC7863EACEF', 'record1'),
       (X'CAFEBABE51839272ABE654182AC7863EACEF', 'record2'),
       (X'CAFEBABE51839272ABE653182AC7868EACEF', 'record3'),
       (X'CAFEBABE51839271ABE654182AC786cEACEF', 'record4'),
       (X'CAFEBABE51839270ABE654182AC7863EACEF', 'record5');


CREATE TABLE `strange_uion_pk` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `uniq_id` TEXT  NOT NULL,
    `name` varchar(64) NOT NULL DEFAULT '',
    PRIMARY KEY (`id`,`uniq_id`(8))
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO `strange_uion_pk` (`uniq_id`, `name`)
VALUES
('0\' or 1>\'1', 'inject'),
('select f1,f2,f3,f4,f5,f6,f7,f8,f9 from create_view order by id desc limit 100', 'select'),
('some\\\"', 'hello'),
('with\"', 'apple'),
('with\'', 'ajax');


CREATE TABLE `strange_uion_binary_pk` (
   `binary_id` BINARY(64) NOT NULL,
   `uniq_id` TEXT  NOT NULL,
   `name` varchar(64) NOT NULL DEFAULT '',
   PRIMARY KEY (`binary_id`,`uniq_id`(8))
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


INSERT INTO `strange_uion_binary_pk` ( `binary_id`,`uniq_id`,`name`)
VALUES (X'CAFEBABE', 'record1','name'),
       (X'CAFEBABD', 'record2','name'),
       (X'CAFEBABC', 'record3','name'),
       (X'CAFEBABB', 'record4','name'),
       (X'CAFEBABA', 'record5','name');


CREATE TABLE `strange_enum_pk` (
      `enum_id` enum('sichuan','shanghai','chengdu') NOT NULL DEFAULT 'chengdu',
      `uniq_id` BLOB  NOT NULL,
      `name` varchar(64) NOT NULL DEFAULT '',
      PRIMARY KEY (`enum_id`,`uniq_id`(8))
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


INSERT INTO `strange_enum_pk` ( `uniq_id`,`enum_id`,`name`)
VALUES (X'CAFEBABE', 'chengdu','name'),
       (X'CAFEBABD', 'shanghai','name'),
       (X'CAFEBABC', 'sichuan','name');