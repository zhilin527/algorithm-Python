# MySQL语句
建表
create table buyss(
  catagory char(4),
  nums int,
  abstract varchar(20)
);
插入
insert into buyss(catagory,nums,abstract)
values
('a',5,'a2002'),
('a',2,'a2001'),
('b',10,'b2003'),
('b',6,'b2002'),
('b',3,'b2001'),
('c',9,'c2005'),
('c',9,'c2004'),
('c',8,'c2003'),
('c',7,'c2002'),
('c',4,'c2001'),
('a',1,'a2001');
查询
select catagory,sum(nums) as numsall
from buyss
group by catagory;
查询
select catagory,max(nums) as numsall
from buyss
where catagory='a' or catagory='b'
group by catagory;
查询
select catagory,avg(nums) as numsall
from buyss
where catagory='a' or catagory='b'
group by catagory
having avg(nums) \> 3;

# MySQL调优

## 一.性能监控
### 1.show profiles
Mysql从5.1版本开始引入show profile来剖析单条语句功能,查看是否支持这个功能
show variables like '%have\_profiling%';
YES表示支持
开启，当前会话关闭前，只需要执行一次
show variables like '%profil%';
set profiling = ON;
show variables like '%profil%';
然后执行你的SQL语句
Select sid,cid,score from sc;
Select sid,sname,sage from student;
select cid,cname,tid from course;
show profiles;
mysql> show profiles;
+----------+------------+----------------------------------------+
| Query_ID | Duration   | Query                                  |
+----------+------------+----------------------------------------+
|        1 | 0.00013000 | select count(*) from he_store_discount |
|        2 | 0.00290900 | show databases                         |
|        3 | 0.00016200 | SELECT DATABASE()                      |
|        4 | 0.00052800 | show databases                         |
|        5 | 0.00204500 | show tables                            |
|        6 | 0.00027000 | select count(*) from he_store_discount |
+----------+------------+----------------------------------------+
6 rows in set, 1 warning (0.00 sec)
所有的查询SQL耗时都会被列出来，然后再根据编号(即Query\_ID)查询具体SQL的执行过程，
show profile for query 1;
show profile cpu,block io,deault pages for query 15;
show profile all for query 1;
mysql> show profile cpu for query 1;
+---------------+----------+----------+------------+
| Status        | Duration | CPU_user | CPU_system |
+---------------+----------+----------+------------+
| starting      | 0.000091 | 0.000073 |   0.000012 |
| freeing items | 0.000028 | 0.000016 |   0.000011 |
| cleaning up   | 0.000011 | 0.000008 |   0.000003 |
+---------------+----------+----------+------------+
3 rows in set, 1 warning (0.00 sec)
### 2.performance\_schema
show databases;
use performance\_schema;
show tables;
性能监控的一个数据库，有很多表记录系统运行时的资源消耗
### 3.show processlist;
该命令能够查看当前连接的线程个数，观察不正常的连接
mysql> show processlist;
+----+------+--------------------+------+---------+-------+-------+------------------+
| Id | User | Host               | db   | Command | Time  | State | Info             |
+----+------+--------------------+------+---------+-------+-------+------------------+
|  1 | root | localhost          | NULL | Sleep   |    12 |       | NULL             |
|  2 | root | 192.168.100.1:7437 | test | Sleep   |  8035 |       | NULL             |
|  3 | root | 192.168.100.1:7438 | NULL | Sleep   | 24348 |       | NULL             |
|  5 | root | 192.168.100.1:7443 | NULL | Sleep   | 24317 |       | NULL             |
|  7 | root | 192.168.100.1:7450 | test | Sleep   | 24272 |       | NULL             |
|  9 | root | 192.168.100.1:5152 | test | Query   |     0 | init  | show processlist |
+----+------+--------------------+------+---------+-------+-------+------------------+
6 rows in set
show variables like '%max\_connection%’;能够查看最大的连接个数
max_connections	2532
## 二.schema与数据类型的优化
### 1.数据类型的优化
更小的数据类型，占用磁盘更小，占用CPU缓存也少
A.占用CPU周期：整型\<字符串
B.存储时间代价：自建类型DATE\<字符串
C.整型存储IP地址

## 三.执行计划
开启慢查询
show variables like '%uery\_log%';
set global slow\_query\_log = ON;
explain+SQL语句来模拟优化器执行SQL查询语句，从而知道mysql是如何处理sql语句的
详见mysql执行计划

## 四.通过索引进行优化
### Primary key
### Unique  index
### Index
### Fulltext index
### 组合索引
Primary key index
create table buyss(
  id int  primary key auto\_increment,
  catagory char(4),
  nums int,
  abstract varchar(20)
);
alter table buyss add index idx(abstract);
1.更新频繁的，重复多的字段不建索引;
2.尽量使用主键查询，因为主键查询不会触发回表查询；
##五.SQL语句进行优化
1.尽量不要用select \* 
2.拆分一些复杂的连表查询为单个查询
3.尽量避免在 where 子句中对字段进行 null 值判断
select id from t where num is null
可以在num上设置默认值0，确保表中num列没有null值，然后这样查询：
select id from t where num=0
4.尽量不使用left join right join

## 事务：
多条sql语句组成的完整体，维护数据库的完整性。
BEGIN 开始一个事务
ROLLBACK 事务回滚
COMMIT 事务确认
## MySQL怎么解决幻读
幻读：同一个事务内，同一条SQL语句，前后读出来的数据不一致
MySQL通过行锁和MVCC多版本并发控制解决幻读
MySQL默认隔离级别是可重复度，这种隔离级别下，通过MVCC的控制，读出来的是事务开始时的数据。
MVCC：MySQL每一行数据行中额外三个隐藏的列：分别是插入这个数据行时的版本号，删除这个数据行时的版本号，回滚指针(指向undo log的指针)
1.查询操作时：数据行被查出来要满足两个条件：1.数据行的删除版本号为空 或者当前查询事务ID\<删除版本号，因为如果当前事务的ID\>删除版本号，就表示之前有其他事务将这条数据行标记删除了。2.当前事务的ID\> =数据行的创建版本号，否则的话，表示这条数据行是后面的事务创建出来的。
2.插入操作时，插入一条数据时，会将当前事务的ID作为创建版本号。(事务开始时，事务ID=当前系统版本号+1)
3.删除操作时，会将该删除数据行的删除版本号设置为当前事务的ID，然后根据原数据行生成一条INSERT语句，写入undo log用于回滚。然后将该数据行标记为删除。
4.更新操作，先删除，再插入。
还有一点就是，在查询时先看行锁，如果该行数据没有加X锁，直接读；
如果查询时该行数据加了X锁，表示有其他事务正在写，那么不等待，直接从undo log里面读，因为undo log是其他事务加锁进行写之前的数据。从undo log里面读，从而避免了幻读。
[https://www.jianshu.com/p/2bd3a440b487]
## 索引：
是存储引擎用于快速找到数据记录的一种数据结构
## MySQL索引覆盖
什么叫索引覆盖？
只需要在一棵索引树上就能获取SQL所需的所有列数据，无需回表，就叫满足索引覆盖
explain的输出结果Extra字段为Using index时，能够触发索引覆盖。
如何实现索引覆盖？
将被查询的字段，建立到联合索引里去
当一张user表有主见索引和name列索引时：
select id,name from user where name='shenjian’;会触发索引覆盖
select id,name,sex from user where name='shenjian’;不会出发索引覆盖
索引覆盖有什么用？
优化一些查询，需要回表的查询，将查询字段加到多列索引里面，
还有count全表计数查询，将计数列建索引
## 存储过程
存储在数据库中的，特定功能的SQL语句集，编译以后可以多次调用。
_优点_：封装好的，多次调用
_缺点_：定制化，移植性不好
mysql> delimiter $$　　#将语句的结束符号从分号;临时改为两个$$(可以是自定义)
mysql> CREATE PROCEDURE delete_matches(IN p_playerno INTEGER)
    -> BEGIN
    -> 　　DELETE FROM MATCHES
    ->    WHERE playerno = p_playerno;
    -> END$$
Query OK, 0 rows affected (0.01 sec)
mysql> delimiter;　　#将语句的结束符号恢复为分号
调用存储过程 call spname传参
过程体格式：
begin
	statement;
end$$
存储过程三种参数格式：in，out，inout
存储过程和数据库是对应的，查询该数据库中有哪些存储过程：
showprocedure status where db='数据库名';
## 聚集索引和非聚集索引：
聚集索引
B+树的叶子节点存的是数据记录，索引和数据保存在.ibd文件。
非聚集索引
而非聚集索引索引树叶子节点存放的是地址，索引保存在MYI文件，数据保存在MYD文件，还要通过叶子节点的地址去找数据记录。
## innodb和myisam区别
innodb支持事务，myisam不支持事务
innodb是聚集索引，myisam是非聚集索引
Innodb支持的是行级锁，myisam支持的是表锁
Innodb不保存表的具体行数，myisam用一个变量保存了具体行数，因此 select count(*)时innodb扫面全表，myisam不会*


