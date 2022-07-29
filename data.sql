CREATE TABLE `MagicnotifyUuidName` (
    `key` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`key`)
);
CREATE TABLE `MagicnotifyPrice` (
	`foil` DECIMAL(10,2),
	`normal` DECIMAL(10,2),
	`date` DATE NOT NULL,
	`key` VARCHAR(50) NOT NULL,
	FOREIGN KEY (`key`) REFERENCES `MagicnotifyUuidName` (`key`)
);
CREATE TABLE `MagicnotifySetInfo`(
    `set` VARCHAR(10) NOT NULL,
    `setName` VARCHAR(50),
    `reldate` DATE,
    PRIMARY KEY (`set`, `setName`, `reldate`)
);
CREATE TABLE `MagicnotifyCardInfo` (
    `koname` VARCHAR(45),
	`name` VARCHAR(45),
	`cardkingdom` VARCHAR(45),
	`cardkingdomfoil` VARCHAR(45),
	`set` VARCHAR(10) NOT NULL,
	`setName` VARCHAR(50),
	`reldate` DATE,
	`rarity` VARCHAR(10),
	`uuid` VARCHAR(50) NOT NULL,
	FOREIGN KEY (`uuid`) REFERENCES `MagicnotifyUuidName` (`key`),
	FOREIGN KEY (`set`, `setName`, `reldate`) REFERENCES `MagicnotifySetInfo` (`set`, `setName`, `reldate`)
);


