create table tb_page
(
    page_id    varchar(32)  not null comment '页面ID'
        primary key,
    page_name  varchar(255) null comment '页面名称',
    project_id varchar(32)  null comment '项目ID',
    constraint tb_page_page_id_uindex
        unique (page_id)
)
    comment '项目页面表';

INSERT INTO ui_at.tb_page (page_id, page_name, project_id) VALUES ('ErIfpuT1CVEPh9aYraRO7', '首页', 'xB07yUa_9KGW9srfopwNI');
INSERT INTO ui_at.tb_page (page_id, page_name, project_id) VALUES ('NOy4veT7jtazFx6AUNSeP', '登录', 'xB07yUa_9KGW9srfopwNI');
INSERT INTO ui_at.tb_page (page_id, page_name, project_id) VALUES ('NvSN0kYbAGGjmXhW0KGeO', '企业管理', 'xB07yUa_9KGW9srfopwNI');
