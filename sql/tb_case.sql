create table tb_case
(
    case_id      varchar(32)                            not null comment '用例ID'
        primary key,
    case_name    varchar(255)                           null comment '用例名称',
    case_desc    text                                   null comment '用例描述',
    project_id   varchar(32)                            null comment '项目ID',
    create_time  datetime   default current_timestamp() null,
    case_creator varchar(10)                            null comment '用例创建者',
    is_run       varchar(1) default '1'                 null comment '是否运行。1：运行，0：不运行',
    constraint tb_case_case_id_uindex
        unique (case_id)
);

INSERT INTO ui_at.tb_case (case_id, case_name, case_desc, project_id, create_time, case_creator, is_run) VALUES ('aj8nuT-Oj6N06s5NLDOHk', '登录', '新版登录', 'xB07yUa_9KGW9srfopwNI', '2022-07-24 12:50:21.0', null, '1');
INSERT INTO ui_at.tb_case (case_id, case_name, case_desc, project_id, create_time, case_creator, is_run) VALUES ('LfRwUHWXf60HD1kxO2Jnu', '角色管理', '测试首页功能', 'xB07yUa_9KGW9srfopwNI', '2022-07-28 06:10:46.0', null, '1');
