create table tb_page_object
(
    po_id        varchar(32)  not null comment '页面对象ID'
        primary key,
    po_name      varchar(100) null comment 'po名称',
    locate_type  varchar(32)  null comment '定位方式',
    locate_value text         null comment '对应定位方式的值',
    action       varchar(32)  null comment '动作',
    page_id      varchar(32)  null comment '页面ID',
    constraint tb_page_object_po_id_uindex
        unique (po_id)
)
    comment 'PO对象表';

INSERT INTO ui_at.tb_page_object (po_id, po_name, locate_type, locate_value, action, page_id) VALUES ('1', '新增企业', 'xpath', '/html/body/div[1]/div/section/section/main/div/div[1]/div[2]/div[1]/button', 'click', '8gNa1wIJDvTUguQtemaa1');
INSERT INTO ui_at.tb_page_object (po_id, po_name, locate_type, locate_value, action, page_id) VALUES ('8ysb6HNjx0rkecwzwi_ND', '进入角色管理', 'xpath', '/html/body/div[1]/div/section/aside/div/ul/li/ul/li[3]', 'click', 'ErIfpuT1CVEPh9aYraRO7');
INSERT INTO ui_at.tb_page_object (po_id, po_name, locate_type, locate_value, action, page_id) VALUES ('BqEH2jcj5qrILsZ2SLigu', '点击登录', 'xpath', '/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/form/div[3]/div/div/div/button', 'click', 'NOy4veT7jtazFx6AUNSeP');
INSERT INTO ui_at.tb_page_object (po_id, po_name, locate_type, locate_value, action, page_id) VALUES ('gKBM2yl86v1SrqJ8P_v24', '进入用户管理', 'xpath', '/html/body/div/div/section/aside/div/ul/li[1]/ul/li[3]/span/div', 'click', 'ErIfpuT1CVEPh9aYraRO7');
INSERT INTO ui_at.tb_page_object (po_id, po_name, locate_type, locate_value, action, page_id) VALUES ('ivIfpBqPmYxpH5JYUvr6A', '输入密码', 'id', 'password', 'input', 'NOy4veT7jtazFx6AUNSeP');
INSERT INTO ui_at.tb_page_object (po_id, po_name, locate_type, locate_value, action, page_id) VALUES ('KDz5bOgocgc5geVnHIceS', '输入用户名', 'id', 'user_name', 'input', 'NOy4veT7jtazFx6AUNSeP');
INSERT INTO ui_at.tb_page_object (po_id, po_name, locate_type, locate_value, action, page_id) VALUES ('L31ml0HJFKKRfRG_sKMac', '进入企业管理', 'xpath', '/html/body/div[1]/div/section/aside/div/ul/li/ul/li[1]', 'click', 'ErIfpuT1CVEPh9aYraRO7');
INSERT INTO ui_at.tb_page_object (po_id, po_name, locate_type, locate_value, action, page_id) VALUES ('p1s6CmfY_hPszvjes_ZI6', '用户名', 'xpath', '/html/body/div[1]/div/section/section/header/div/span[1]', 'check', 'ErIfpuT1CVEPh9aYraRO7');
INSERT INTO ui_at.tb_page_object (po_id, po_name, locate_type, locate_value, action, page_id) VALUES ('y3DKV3sdntprWcGnVIARP', '页面标题', 'xpath', '/html/body/div[1]/div/section/section/header/span', 'check', 'ErIfpuT1CVEPh9aYraRO7');
