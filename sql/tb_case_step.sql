create table tb_case_step
(
    step_id      varchar(32) null comment '步骤ID',
    step_name    varchar(32) null comment '步骤名称',
    case_id      varchar(32) null comment '用例ID',
    po_id        varchar(32) null comment '页面对象ID（后续抽出关系表）',
    input_value  text        null comment '输入值',
    expect_value text        null comment '预期值',
    page_id      varchar(32) null comment '页面ID',
    create_time  datetime    null comment '创建时间'
);

INSERT INTO ui_at.tb_case_step (step_id, step_name, case_id, po_id, input_value, expect_value, page_id, create_time) VALUES ('Gh26TFdby4YwdfZrao5R5', '输入用户名', 'aj8nuT-Oj6N06s5NLDOHk', 'KDz5bOgocgc5geVnHIceS', 'admin', '', 'NOy4veT7jtazFx6AUNSeP', null);
INSERT INTO ui_at.tb_case_step (step_id, step_name, case_id, po_id, input_value, expect_value, page_id, create_time) VALUES ('16dfK0DFRD8p7lahHi7zP', '输入密码', 'aj8nuT-Oj6N06s5NLDOHk', 'ivIfpBqPmYxpH5JYUvr6A', 'ABCD1234', '', 'NOy4veT7jtazFx6AUNSeP', null);
INSERT INTO ui_at.tb_case_step (step_id, step_name, case_id, po_id, input_value, expect_value, page_id, create_time) VALUES ('NpaefwSeb2ZikPmTOpWwb', '点击登录', 'aj8nuT-Oj6N06s5NLDOHk', 'BqEH2jcj5qrILsZ2SLigu', '', '', 'NOy4veT7jtazFx6AUNSeP', null);
INSERT INTO ui_at.tb_case_step (step_id, step_name, case_id, po_id, input_value, expect_value, page_id, create_time) VALUES ('sfd6RWickDmmPSoLxjcLC', '进入角色管理', 'LfRwUHWXf60HD1kxO2Jnu', '8ysb6HNjx0rkecwzwi_ND', '', '', 'ErIfpuT1CVEPh9aYraRO7', null);
INSERT INTO ui_at.tb_case_step (step_id, step_name, case_id, po_id, input_value, expect_value, page_id, create_time) VALUES ('hOXWRXYqtxjahgQfJdAhn', '验证用户名', 'LfRwUHWXf60HD1kxO2Jnu', 'p1s6CmfY_hPszvjes_ZI6', '', '', 'ErIfpuT1CVEPh9aYraRO7', null);
INSERT INTO ui_at.tb_case_step (step_id, step_name, case_id, po_id, input_value, expect_value, page_id, create_time) VALUES ('zo4vsa1_PLckZc9z-Cwu2', '进入用户管理', 'LfRwUHWXf60HD1kxO2Jnu', 'gKBM2yl86v1SrqJ8P_v24', '', '', 'ErIfpuT1CVEPh9aYraRO7', null);
