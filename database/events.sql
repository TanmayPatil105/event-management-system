USE event_mgmt;


-- --------------------------------------------------------------------------------------------------------

CREATE TABLE `event_type` (
  `type_id` int(10) NOT NULL,
  `type_title` text NOT NULL
);

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

-- -----------------------------------------------------------------------------------------------------

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

CREATE TABLE `events` (
  `event_id` int(100) NOT NULL,
  `event_title` varchar(100) NOT NULL,
  `event_price` int(20) NOT NULL,
  `participants` int(100) NOT NULL,
  `type_id` int(10) NOT NULL,
  `location_id` int(10) NOT NULL,
  `date` DATE NOT NULL
);


ALTER TABLE `events`
  ADD PRIMARY KEY (`event_id`);


ALTER TABLE `events`
  ADD FOREIGN KEY (`type_id`) REFERENCES event_type(`type_id`)
  ON DELETE CASCADE;
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

INSERT INTO `events` (`event_id`, `event_title`, `event_price`, `participants`, `type_id`,`location_id`,`date`) VALUES
(1, 'Mindspark', 50, 4, 1,1,'2023-01-1'),
(2, 'Impressions', 50, 2, 3,3,'2022-12-21'),
(3, 'Zest', 50, 1, 4,3,'2023-02-01'),
(4, 'RE-INIT', 50, 2, 1,2,'2022-11-05'),
(5, 'FlossMeet', 50, 1, 1,5,'2023-04-11'),
(6, 'Spandan', 50, 1, 3,1,'2022-11-03');


-- ---------------------------------------------------------------------------------------


CREATE TABLE `participants` (
  `p_id` int(10) NOT NULL,
  `event_id` int(10) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `email` varchar(300) NOT NULL,
  `mobile` char(10) NOT NULL,
  `college` varchar(300) NOT NULL,
  `branch_id` int(10) NOT NULL
);

ALTER TABLE `participants`
  ADD PRIMARY KEY (`p_id`);


ALTER TABLE `participants`
  ADD FOREIGN KEY (`event_id`) REFERENCES events(`event_id`) 
  ON DELETE CASCADE;

ALTER TABLE `participants`
  ADD FOREIGN KEY (`branch_id`) REFERENCES branch(`branch_id`);
  
ALTER TABLE `participants`
  MODIFY `p_id` int(10) NOT NULL AUTO_INCREMENT;



-- -----------------------------------------------------------------------------




CREATE TABLE `admin`(
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
);

INSERT INTO `admin` VALUES
('Admin1','password1'),
('Admin2','password2');

----------------------------------------------------------------------------------