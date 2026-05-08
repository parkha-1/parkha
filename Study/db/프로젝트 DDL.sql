DROP DATABASE IF EXISTS travel;

CREATE DATABASE travel;

USE travel;

DROP TABLE IF EXISTS `post`;

CREATE TABLE `post` (
	`po_num`	int	NOT NULL,
	`po_title`	varchar(100)	NULL,
	`po_content`	longtext	NULL,
	`po_date`	date	NULL,
	`po_veiw`	int	NULL,
	`po_up`	int	NULL,
	`po_down`	int	NULL,
	`po_del`	char(1)	NULL,
	`po_cg_num`	int	NOT NULL,
	`po_mb_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `comment`;

CREATE TABLE `comment` (
	`co_num`	int	NOT NULL,
	`co_content`	text	NULL,
	`co_date`	date	NULL,
	`co_like`	int	NULL,
	`co_del`	char(1)	NULL,
	`co_ori_num`	int	NOT NULL,
	`co_po_num`	int	NOT NULL,
	`co_mb_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `photo`;

CREATE TABLE `photo` (
	`ph_num`	int	NOT NULL,
	`ph_ori_name`	varchar(100)	NULL,
	`ph_name`	varchar(100)	NULL,
	`ph_po_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `live-rank`;

CREATE TABLE `live-rank` (
	`lr_num`	int	NOT NULL,
	`lr_time`	time	NULL,
	`lr-ori_num`	int	NOT NULL,
	`lr_po_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `history`;

CREATE TABLE `history` (
	`ht_num`	int	NOT NULL,
	`ht_time`	date	NOT NULL,
	`ht_po_num`	int	NOT NULL,
	`ht_me_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `report-box`;

CREATE TABLE `report-box` (
	`rb_num`	int	NOT NULL,
	`rb_content`	text	NULL,
	`rb_manage`	char(1)	NULL,
	`rb_id`	int	NULL,
	`rb_name`	varchar(10)	NULL,
	`rb_mb_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `travel`;

CREATE TABLE `travel` (
	`tv_num`	int	NOT NULL,
	`tv_API`	varchar(100)	NULL,
	`tv_lat`	DECIMAL	NULL,
	`tv_lng`	DECIMAL	NULL,
	`tv_mapAPI`	varchar(100)	NULL,
	`tv_cg_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `kind`;

CREATE TABLE `kind` (
	`ki_num`	int	NULL,
	`ki_name`	varchar(10)	NULL
);

DROP TABLE IF EXISTS `member`;

CREATE TABLE `member` (
	`mb_num`	int	NOT NULL,
	`mb_Uid`	varchar(30)	NOT NULL,
	`mb_pw`	varchar(30)	NULL,
	`mb_email`	varchar(50)	NULL,
	`mb_rol`	varchar(10)	NULL,
	`mb_score`	int	NULL,
	`mb_photo`	varchar(100)	NULL,
	`mb_agree`	char(1)	NULL
);

DROP TABLE IF EXISTS `bookmark`;

CREATE TABLE `bookmark` (
	`bm_num`	int	NOT NULL,
	`bm_po_num`	int	NOT NULL,
	`bm_mb_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `main-photo`;

CREATE TABLE `main-photo` (
	`mp_num`	int	NOT NULL,
	`mp_name`	varchar(100)	NULL,
	`mp_tv_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
	`cg_num`	int	NOT NULL,
	`cg_kind`	varchar(10)	NULL,
	`bo_display`	char(1)	NULL,
	`bo_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `mark`;

CREATE TABLE `mark` (
	`ma_num`	int	NOT NULL,
	`ma_score`	int	NULL,
	`ma_ki_num`	int	NULL,
	`ma_po_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
	`rv_num`	int	NOT NULL,
	`rv_content`	text	NULL,
	`rv_up`	int	NULL,
	`rv_down`	int	NULL,
	`rv_del`	char(1)	NULL,
	`rv_view`	int	NULL,
	`rv_date`	date	NULL,
	`rv_tv_num`	int	NOT NULL,
	`rv_mb_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `like`;

CREATE TABLE `like` (
	`li_num`	int	NOT NULL,
	`li_state`	int	NULL,
	`li_id`	int	NULL,
	`li_name`	varchar(10)	NULL,
	`li_time`	time	NULL,
	`li_mb_num`	int	NOT NULL
);

DROP TABLE IF EXISTS `board`;

CREATE TABLE `board` (
	`bo_num`	int	NOT NULL,
	`bo_name`	varchar(100)	NULL
);


ALTER TABLE `post` ADD CONSTRAINT `FK_category_TO_post_1` FOREIGN KEY (
	`po_cg_num`
)
REFERENCES `category` (
	`cg_num`
);

ALTER TABLE `post` ADD CONSTRAINT `FK_member_TO_post_1` FOREIGN KEY (
	`po_mb_num`
)
REFERENCES `member` (
	`mb_num`
);

ALTER TABLE `comment` ADD CONSTRAINT `FK_comment_TO_comment_1` FOREIGN KEY (
	`co_ori_num`
)
REFERENCES `comment` (
	`co_num`
);

ALTER TABLE `comment` ADD CONSTRAINT `FK_post_TO_comment_1` FOREIGN KEY (
	`co_po_num`
)
REFERENCES `post` (
	`po_num`
);

ALTER TABLE `comment` ADD CONSTRAINT `FK_member_TO_comment_1` FOREIGN KEY (
	`co_mb_num`
)
REFERENCES `member` (
	`mb_num`
);

ALTER TABLE `photo` ADD CONSTRAINT `FK_post_TO_photo_1` FOREIGN KEY (
	`ph_po_num`
)
REFERENCES `post` (
	`po_num`
);

ALTER TABLE `live-rank` ADD CONSTRAINT `FK_post_TO_live-rank_1` FOREIGN KEY (
	`lr_po_num`
)
REFERENCES `post` (
	`po_num`
);

ALTER TABLE `history` ADD CONSTRAINT `FK_post_TO_history_1` FOREIGN KEY (
	`ht_po_num`
)
REFERENCES `post` (
	`po_num`
);

ALTER TABLE `history` ADD CONSTRAINT `FK_member_TO_history_1` FOREIGN KEY (
	`ht_me_num`
)
REFERENCES `member` (
	`mb_num`
);

ALTER TABLE `report-box` ADD CONSTRAINT `FK_member_TO_report-box_1` FOREIGN KEY (
	`rb_mb_num`
)
REFERENCES `member` (
	`mb_num`
);

ALTER TABLE `travel` ADD CONSTRAINT `FK_category_TO_travel_1` FOREIGN KEY (
	`tv_cg_num`
)
REFERENCES `category` (
	`cg_num`
);

ALTER TABLE `bookmark` ADD CONSTRAINT `FK_post_TO_bookmark_1` FOREIGN KEY (
	`bm_po_num`
)
REFERENCES `post` (
	`po_num`
);

ALTER TABLE `bookmark` ADD CONSTRAINT `FK_member_TO_bookmark_1` FOREIGN KEY (
	`bm_mb_num`
)
REFERENCES `member` (
	`mb_num`
);

ALTER TABLE `main-photo` ADD CONSTRAINT `FK_travel_TO_main-photo_1` FOREIGN KEY (
	`mp_tv_num`
)
REFERENCES `travel` (
	`tv_num`
);

ALTER TABLE `category` ADD CONSTRAINT `FK_board_TO_category_1` FOREIGN KEY (
	`bo_num`
)
REFERENCES `board` (
	`bo_num`
);

ALTER TABLE `mark` ADD CONSTRAINT `FK_kind_TO_mark_1` FOREIGN KEY (
	`ma_ki_num`
)
REFERENCES `kind` (
	`ki_num`
);

ALTER TABLE `mark` ADD CONSTRAINT `FK_post_TO_mark_1` FOREIGN KEY (
	`ma_po_num`
)
REFERENCES `post` (
	`po_num`
);

ALTER TABLE `review` ADD CONSTRAINT `FK_travel_TO_review_1` FOREIGN KEY (
	`rv_tv_num`
)
REFERENCES `travel` (
	`tv_num`
);

ALTER TABLE `review` ADD CONSTRAINT `FK_member_TO_review_1` FOREIGN KEY (
	`rv_mb_num`
)
REFERENCES `member` (
	`mb_num`
);

ALTER TABLE `like` ADD CONSTRAINT `FK_member_TO_like_1` FOREIGN KEY (
	`li_mb_num`
)
REFERENCES `member` (
	`mb_num`
);

