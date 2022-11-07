begin;
create database YOLO;
use YOLO;
CREATE TABLE yoloGarbage (
num int primary key,
garbage varchar(255),
xywh_x decimal(20,18),
xywh_y decimal(20,18),
xywh_w decimal(20,18),
xywh_h decimal(20,18),
in_datetime datetime default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);
CREATE USER 'yolo_user'@'%' IDENTIFIED BY 'yologarbage33214';
grant all privileges on YOLO.* to 'yolo_user'@'%' with grant option;
commit;