CREATE DATABASE event_mgmt;
USE event_mgmt;


CREATE TABLE `events` (
  `event_id` int(100) NOT NULL,
  `event_title` text NOT NULL,
  `event_price` int(20) NOT NULL,
  `participants` int(100) NOT NULL,
  `type_id` int(10) NOT NULL,
  `location_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


ALTER TABLE `events`
  ADD PRIMARY KEY (`event_id`);


ALTER TABLE `events`
  ADD FOREIGN KEY (`type_id`) REFERENCES event_type(`type_id`);
--
ALTER TABLE `events`
  ADD FOREIGN KEY (`location_id`) REFERENCES location(`location_id`);

--
ALTER TABLE `events`
  MODIFY `event_id` int(100) NOT NULL AUTO_INCREMENT;
--
-- location_id IS FOREIGN KEY

-- Dumping data for table `events`
--

INSERT INTO `events` (`event_id`, `event_title`, `event_price`, `participants`, `type_id`,`location_id`) VALUES
(1, 'Mindspark', 50, 4, 1,1),
(2, 'Impressions', 50, 2, 3,3),
(3, 'Zest', 50, 1, 4,3),
(4, 'RE-init', 50, 2, 1,2),
(5, 'FlossMeet', 50, 1, 1,5),
(6, 'Spandan', 50, 1, 3,1);


-- --------------------------------------------------------------------------------------------------------

CREATE TABLE `event_type` (
  `type_id` int(10) NOT NULL,
  `type_title` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `event_type`
  ADD PRIMARY KEY (`type_id`);

ALTER TABLE `event_type`
  MODIFY `type_id` int(10) NOT NULL AUTO_INCREMENT;

INSERT INTO `event_type` (`type_id`, `type_title`) VALUES
(1, 'Technical'),
(2, 'Gaming'),
(3, 'Cultural'),
(4, 'Sports'),
(5, 'Trivia');

-- ---------------------------------------------------------------------------------------


CREATE TABLE `participants` (
  `p_id` int(10) NOT NULL,
  `event_id` int(10) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `email` varchar(300) NOT NULL UNIQUE,
  `mobile` char(10) NOT NULL,
  `college` varchar(300) NOT NULL,
  `branch_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `participants`
  ADD PRIMARY KEY (`p_id`);


ALTER TABLE `participants`
  ADD FOREIGN KEY (`event_id`) REFERENCES events(`event_id`);

ALTER TABLE `participants`
  ADD FOREIGN KEY (`branch_id`) REFERENCES branch(`branch_id`);
  
ALTER TABLE `participants`
  MODIFY `p_id` int(10) NOT NULL AUTO_INCREMENT;

-- -----------------------------------------------------------------------------

CREATE TABLE `branch`(
  `branch_id` int(10) NOT NULL,
  `branch_name` varchar(30) NOT NULL
);


ALTER TABLE `branch`
  ADD PRIMARY KEY (`branch_id`);

ALTER TABLE `branch`
  MODIFY `branch_id` int(10) NOT NULL AUTO_INCREMENT;


INSERT INTO `branch` (`branch_name`) VALUES
('Civil'),
('Computer'),
('Electrical'),
('E&TC'),
('Instrumentation'),
('Mechanical'),
('Metallurgy'),
('Production');

-- ----------------------------------------------------------------------------------------------------------

CREATE TABLE `location`(
  `location_id` int(10) NOT NULL,
  `location_name` varchar(100) NOT NULL
);

ALTER TABLE `location`
  ADD PRIMARY KEY (`location_id`);

ALTER TABLE `location`
  MODIFY `location_id` int(10) NOT NULL AUTO_INCREMENT;


INSERT INTO `location` (`location_name`) VALUES
('Main Auditorium'),
('Mini Auditorium'),
('COEP Ground'),
('Academic Complex'),
('Cognizant Lab');

-- ------------------------------------------------------------------------------------------------------------

CREATE TABLE `admin`(
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
);

INSERT INTO `admin` VALUES
('Admin','password');