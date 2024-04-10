insert into members(username, weight_goal, time_goal)
values
	('m1', 130, '2024-05-01'),
	('m2', 150, '2024-06-6')
;

insert into trainers(username)
values
	('t1'),
	('t2')
;

insert into administrators(username)
values
	('a1')
;

insert into health_metrics(member_id, metric_type, metric_value, date_measured)
values
	(1, 'lbs', 115, '2024-04-09'),
	(1, 'kg', 52, '2024-03-08'),
	(2, 'lbs', 140, '2024-05-01')
;

insert into goals(member_id, description)
values
	(1, 'Handstand and planche'),
	(2, 'abs')
;

insert into exercises(member_id, description)
values
	(1, 'planch push ups'),
	(2, 'sit-ups')
;


insert into availabilities(trainer_id, available_time)
values
	(1, '2024-05-06'),
	(1, '2024-07-16'),
	(1, '2025-12-06'),
	(1, '2025-01-20'),
	(2, '2024-04-20'),
	(2, '2024-05-20'),
	(2, '2024-07-13')
;

insert into pt_sessions(trainer_id, member_id, session_time)
values
	(1, 1, '2024-04-09'),
	(1, 2, '2024-04-10'),
	(2, 1, '2030-05-29'),
	(2, 2, '2026-10-18')
;

insert into fitness_classes(class_name, trainer_id, class_time, member_names)
values
	('calisthenics', 2, '2025-01-01', array['m1']),
	('pilates', 2, '2024-04-20', array['m1', 'm2'])
;

insert into billings(member_id, amount, bill_date, description)
values
	(1, 39.99, '2024-04-09', 'monthly membership fee'),
	(1, 34.99, '2024-04-10', 'hot tub'),
	(2, 39.99, '2024-04-09', 'monthly membership fee')
;

insert into payments(member_id, bill_id, payment_date, amount)
values
	(1, 1, '2024-04-09', 39.99)
;

insert into equipment(equipment_name, maintenance_cost, maintenance_date)
values
	('squat rack', 44.99, '2025-01-01'),
	('pull-down', 199.99, '2024-05-10'),
	('treadmill', 120, '2024-06-01')
;

insert into room_bookings(room_number, event_name, event_time)
values
	(22, 'muay thai', '2024-05-02'),
	(15, 'yoga', '2024-06-22'),
	(16, 'volley ball', '2024-04-20')
;