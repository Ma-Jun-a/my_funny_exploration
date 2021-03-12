
CREATE DATABASE IF NOT EXISTS students_info DEFAULT CHARACTER SET utf8;
USE students_info;

/*!50503 set default_storage_engine = InnoDB */;
/*!50503 select CONCAT('storage engine: ', @@default_storage_engine) as INFO */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE IF NOT EXISTS `Student`(
	`s_id` VARCHAR(20),
	`s_name` VARCHAR(20) NOT NULL DEFAULT '',
	`s_birth` VARCHAR(20) NOT NULL DEFAULT '',
	`s_sex` VARCHAR(50) NOT NULL DEFAULT '',
	PRIMARY KEY(`s_id`)
);

CREATE TABLE IF NOT EXISTS `Course`(
	`c_id`  VARCHAR(20),
	`c_name` VARCHAR(20) NOT NULL DEFAULT '',
	`t_id` VARCHAR(20) NOT NULL,
	PRIMARY KEY(`c_id`)
);

CREATE TABLE IF NOT EXISTS `Teacher`(
	`t_id` VARCHAR(20),
	`t_name` VARCHAR(20) NOT NULL DEFAULT '',
	PRIMARY KEY(`t_id`)
);

CREATE TABLE IF NOT EXISTS `Score`(
	`s_id` VARCHAR(20),
	`c_id`  VARCHAR(20),
	`s_score` INT(3),
	PRIMARY KEY(`s_id`,`c_id`)
);

insert into Student values('01' , '赵雷' , '1990-01-01' , 'male');
insert into Student values('02' , '钱电' , '1990-12-21' , 'male');
insert into Student values('03' , '孙风' , '1990-05-20' , 'male');
insert into Student values('04' , '李云' , '1990-08-06' , 'male');
insert into Student values('05' , '周梅' , '1991-12-01' , 'female');
insert into Student values('06' , '吴兰' , '1992-03-01' , 'female');
insert into Student values('07' , '郑竹' , '1989-07-01' , 'female');
insert into Student values('08' , '王菊' , '1990-01-20' , 'female');

insert into Course values('01' , '语文' , '02');
insert into Course values('02' , '数学' , '01');
insert into Course values('03' , '英语' , '03');


insert into Teacher values('01' , '张三');
insert into Teacher values('02' , '李四');
insert into Teacher values('03' , '王五');


insert into Score values('01' , '01' , 80);
insert into Score values('01' , '02' , 90);
insert into Score values('01' , '03' , 99);
insert into Score values('02' , '01' , 70);
insert into Score values('02' , '02' , 60);
insert into Score values('02' , '03' , 80);
insert into Score values('03' , '01' , 80);
insert into Score values('03' , '02' , 80);
insert into Score values('03' , '03' , 80);
insert into Score values('04' , '01' , 50);
insert into Score values('04' , '02' , 30);
insert into Score values('04' , '03' , 20);
insert into Score values('05' , '01' , 76);
insert into Score values('05' , '02' , 87);
insert into Score values('06' , '01' , 31);
insert into Score values('06' , '03' , 34);
insert into Score values('07' , '02' , 89);
insert into Score values('07' , '03' , 98);
