CREATE TABLE `MAGICNOTIFY_UUID_NAME` (
    `key` VARCHAR(30) NOT NULL,
    PRIMARY KEY (`key`)
);
CREATE TABLE `MAGICNOTIFY_PRICE` (
	`foil` DECIMAL(7,2) NOT NULL,
	`normal` DECIMAL(7,2) NOT NULL,
	`date` DATE NOT NULL,
	`key` VARCHAR(30) NOT NULL,
	FOREIGN KEY (`key`) REFERENCES `MAGICNOTIFY_UUID_NAME` (`key`)
);
CREATE TABLE `MAGICNOTIFY_SET_INFO`(
    `set` VARCHAR(10) NOT NULL,
    `setName` VARCHAR(50) NOT NULL,
    `reldate` DATE NOT NULL,
    PRIMARY KEY (`set`, `setName`, `reldate`)
);
CREATE TABLE `MAGICNOTIFY_CARD_INFO` (
    `koname` VARCHAR(45) NOT NULL,
	`name` VARCHAR(45) NOT NULL,
	`cardkingdom` VARCHAR(45) NOT NULL,
	`cardkingdomfoil` VARCHAR(45) NOT NULL,
	`set` VARCHAR(10) NOT NULL,
	`setName` VARCHAR(50) NOT NULL,
	`reldate` DATE NOT NULL,
	`rarity` VARCHAR(10) NOT NULL,
	`uuid` VARCHAR(30) NOT NULL,
	FOREIGN KEY (`uuid`) REFERENCES `MAGICNOTIFY_UUID_NAME` (`key`),
	FOREIGN KEY (`set`, `setName`, `reldate`) REFERENCES `MAGICNOTIFY_SET_INFO` (`set`, `setName`, `reldate`)
);

