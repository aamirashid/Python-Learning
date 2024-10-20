select count(*) from dba_tablespaces;

select tablespace_name, block_size, initial_extent, min_extents, max_extents, max_size, pct_increase, status, contents, extent_management, allocation_type, segment_space_management from dba_tablespaces;

select * from dba_tablespaces;

desc dba_tablespaces

select count(*) from dba_segments;

select distinct segment_type from dba_segments;

select * from dba_segments
where owner = 'HR'
and segment_type in ('LOBINDEX', 'LOB PARTITION', 'LOB SEGMENNT', 'INDEX', 'INDEX PARTITION', 'TABLE', 'TABLE PARTITION', 'NESTED TABLE', 'CLUSTER', 'ROLLBACK', 'TYPE2 UNDO')
order by 4;

select owner, segment_type, segment_name, tablespace_name
from dba_segments
where tablespace_name = 'SYSTEM'
and segment_type='TABLE'
and SEGMENT_NAME LIKE 'D%';

select segment_type, segment_name, tablespace_name, max_extents, extents, blocks, extents+5
from dba_segments where tablespace_name = 'USERS';

select segment_type, segment_name, tablespace_name, max_extents, extents, blocks, extents+5
from dba_segments where tablespace_name = 'USERS'
and extents+5 > max_extents
and segment_type<>'CACHE';

select distinct f.file_name from dba_extents e, dba_data_files f
where e.segment_name = 'EMPLOYEES' and e.file_id = f.file_id;

select tablespace_name, count(*) fragments, sum(bytes) total, max(bytes) largest
from dba_free_space group by tablespace_name;

select s.segment_name, s.segment_type, s.tablespace_name, s.next_extent
from dba_segments s
where tablespace_name = 'USERS' and segment_type in ('TABLE', 'INDEX') and not exists
(select 1 from dba_free_space f where s.tablespace_name = f.tablespace_name
having max(f.bytes) > s.next_extent )
order by 2 desc;

disc

SELECT first_name, last_name
FROM hr.employees
WHERE department_id = 100;

conn hr@orcl

conn sys@orcl as SYSDBA

CREATE TABLE emp (
  employee_id NUMBER,
  first_name VARCHAR2(50),
  last_name VARCHAR2(50)
);

CREATE INDEX emp_last_name_idx ON emp (last_name);

SELECT segment_name, segment_type, tablespace_name, bytes
FROM dba_segments
WHERE owner = 'HR';

drop index emp_last_name_idx;

drop table emp;

sho user

conn hr@orcl
conn sys@orcl as SYSDBA

sho user

SELECT * FROM hr.REGIONS;
