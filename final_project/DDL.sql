create table Members(
    member_id serial primary key,
    username varchar(255) not null,
    weight_goal varchar(255) not null,
    time_goal varchar(255) not null
);

create table Trainers(
	trainer_id serial primary key,
	username varchar(255) not null
);

create table Admins(
	Admin_id serial primary key,
	username varchar(255) not null
);

create table Health_Metrics(
    metric_id serial primary key,
    member_id int not null references Members(member_id),
    metric_type varchar(255) not null,
    metric_value int not null,
	date_measured date not null
);

create table Goals(
	goal_id serial primary key,
	member_id int not null references Members(member_id),
	description text
);

create table Exercise(
	exercise_id serial primary key,
	member_id int not null references Members(member_id),
	description text
);

create table Availability(
	session_id serial primary key,
	trainer_id int references Trainers(trainer_id),
	available_time date not null
);

create table PT_Session(
	session_id serial primary key,
	trainer_id int references Trainers(trainer_id),
	member_id int references Members(member_id),
	session_time date not null
);

create table Fitness_Class(
	class_id serial primary key,
	trainer_id int references Trainers(trainer_id),
	class_name varchar(255) not null,
	class_time date not null,
	member_ids int[]
);

create table Equipment(
	equipment_id serial primary key,
	equipment_name varchar(255) not null,
	maintenance_cost real not null,
	maintenance_date date
);

create table Room_Bookings(
	booking_id serial primary key,
	room_number smallint not null,
	event_name varchar(255),
	event_time date not null
);

create table Billings(
	bill_id serial primary key,
	member_id int not null references Members(member_id),
	amount real not null,
	bill_date date,
	description text
);

create table Payments(
	payment_id serial primary key,
	member_id int not null references Members(member_id),
	bill_id int not null references Billings(bill_id),
	amount real not null,
	payment_date date not null
);