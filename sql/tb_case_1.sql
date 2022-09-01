create table tb_case_1
(
    case_id      varchar(32)  null,
    module_name  varchar(255) null,
    case_name    varchar(255) null,
    step         text         null,
    po_id        varchar(32)  null,
    po           varchar(255) null,
    po_attr      varchar(255) null,
    input_value  text         null,
    expect_value text         null,
    project_id   varchar(32)  null,
    page_id      varchar(32)  null,
    create_time  datetime     null
);

INSERT INTO ui_at.tb_case_1 (case_id, module_name, case_name, step, po_id, po, po_attr, input_value, expect_value, project_id, page_id, create_time) VALUES ('1', '登录', '登录', '输入用户名', null, '登录页', '输入用户名', 'admin', null, null, null, '2022-07-12 13:16:19.0');
INSERT INTO ui_at.tb_case_1 (case_id, module_name, case_name, step, po_id, po, po_attr, input_value, expect_value, project_id, page_id, create_time) VALUES ('2', '登录', null, '输入密码', null, '登录页', '输入密码', 'ABCD1234', null, null, null, '2022-07-12 13:16:19.0');
INSERT INTO ui_at.tb_case_1 (case_id, module_name, case_name, step, po_id, po, po_attr, input_value, expect_value, project_id, page_id, create_time) VALUES ('3', '登录', null, '点击登录', null, '登录页', '点击登录', null, null, null, null, '2022-07-12 13:16:19.0');
INSERT INTO ui_at.tb_case_1 (case_id, module_name, case_name, step, po_id, po, po_attr, input_value, expect_value, project_id, page_id, create_time) VALUES ('4', '首页', null, '进入企业管理', null, '首页', '进入企业管理', null, null, null, null, '2022-07-12 13:16:19.0');
INSERT INTO ui_at.tb_case_1 (case_id, module_name, case_name, step, po_id, po, po_attr, input_value, expect_value, project_id, page_id, create_time) VALUES ('5', '企业管理', '新增企业', '新增企业', null, '企业管理', '新增企业', null, null, null, null, '2022-07-12 13:16:19.0');
INSERT INTO ui_at.tb_case_1 (case_id, module_name, case_name, step, po_id, po, po_attr, input_value, expect_value, project_id, page_id, create_time) VALUES ('aTk5UC7Z_ZDaGBcoLRGvF', '', '验证标题', '对比标题', 'y3DKV3sdntprWcGnVIARP', null, null, '', '吾道科技管理系统1', 'xB07yUa_9KGW9srfopwNI', 'ErIfpuT1CVEPh9aYraRO7', '2022-07-15 09:13:06.0');
INSERT INTO ui_at.tb_case_1 (case_id, module_name, case_name, step, po_id, po, po_attr, input_value, expect_value, project_id, page_id, create_time) VALUES ('bvDIppzzd1nA99NxKz_Ap', '', '登录', '点击登录', 'BqEH2jcj5qrILsZ2SLigu', null, null, '', '', 'xB07yUa_9KGW9srfopwNI', 'NOy4veT7jtazFx6AUNSeP', '2022-07-12 21:16:33.0');
INSERT INTO ui_at.tb_case_1 (case_id, module_name, case_name, step, po_id, po, po_attr, input_value, expect_value, project_id, page_id, create_time) VALUES ('iAf21R-N8XG3Q1ojFwy_w', '', '登录', '输入正确密码', 'ivIfpBqPmYxpH5JYUvr6A', null, null, 'ABCD1234', '', 'xB07yUa_9KGW9srfopwNI', 'NOy4veT7jtazFx6AUNSeP', '2022-07-12 21:16:30.0');
INSERT INTO ui_at.tb_case_1 (case_id, module_name, case_name, step, po_id, po, po_attr, input_value, expect_value, project_id, page_id, create_time) VALUES ('oGIr40pXiBXP73VUP7XUo', '', '登录', '输入正常用户名', 'KDz5bOgocgc5geVnHIceS', null, null, 'admin', '', 'xB07yUa_9KGW9srfopwNI', 'NOy4veT7jtazFx6AUNSeP', '2022-07-12 21:16:20.0');
