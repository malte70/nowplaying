--
-- Database Schema for NowPlaying
--

CREATE TABLE log(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	current_time DATETIME NOT NULL,
	interpreter VARCHAR(250) COLLATE utf8_bin NOT NULL,
	title VARCHAR(250) COLLATE utf8_bin NOT NULL,
	link VARCHAR(250) COLLATE utf8_bin DEFAULT NULL
) DEFAULT CHARSET=utf8_bin;

