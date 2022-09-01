create table tb_project
(
    project_id   varchar(32)  not null comment '项目ID
'
        primary key,
    project_name varchar(255) not null comment '项目名称',
    create_time  datetime     null comment '创建时间',
    delete_time  datetime     null comment '删除时间',
    project_desc text         null comment '项目描述',
    constraint tb_project_project_id_uindex
        unique (project_id)
);

INSERT INTO ui_at.tb_project (project_id, project_name, create_time, delete_time, project_desc) VALUES ('xB07yUa_9KGW9srfopwNI', '系统管理项目', null, null, '');
