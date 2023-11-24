from sqlalchemy import create_engine, text

engine = create_engine('postgresql://medeupazylov:0000@localhost:5432/caregivers_platform')

# TASK 1:
def create_tables() :
    with engine.connect() as connection:
        create_tables_query = text('''
            CREATE TABLE app_user (
                user_id SERIAL PRIMARY KEY,
                email VARCHAR(100),
                given_name VARCHAR(50),
                surname VARCHAR(50),
                city VARCHAR(50),
                phone_number VARCHAR(15),
                profile_description TEXT,
                password VARCHAR(100)
            );

            CREATE TABLE CAREGIVER (
                caregiver_user_id SERIAL PRIMARY KEY,
                photo BYTEA,
                gender VARCHAR(10),
                caregiving_type VARCHAR(50),
                hourly_rate DECIMAL(10, 2),
                FOREIGN KEY (caregiver_user_id) REFERENCES app_user (user_id) ON DELETE CASCADE
            );

            CREATE TABLE MEMBERS (
                member_user_id SERIAL PRIMARY KEY,
                house_rules TEXT,
                FOREIGN KEY (member_user_id) REFERENCES app_user (user_id) ON DELETE CASCADE
            );

            CREATE TABLE ADDRESS (
                member_user_id INT PRIMARY KEY,
                house_number VARCHAR(10),
                street VARCHAR(50),
                town VARCHAR(50),
                FOREIGN KEY (member_user_id) REFERENCES MEMBERS (member_user_id) ON DELETE CASCADE
            );

            CREATE TABLE JOB (
                job_id SERIAL PRIMARY KEY,
                member_user_id INT,
                required_caregiving_type VARCHAR(50),
                other_requirements TEXT,
                date_posted DATE,
                FOREIGN KEY (member_user_id) REFERENCES MEMBERS (member_user_id) ON DELETE CASCADE
            );

            CREATE TABLE JOB_APPLICATION (
                caregiver_user_id INT,
                job_id INT,
                date_applied DATE,
                FOREIGN KEY (caregiver_user_id) REFERENCES CAREGIVER (caregiver_user_id) ON DELETE CASCADE,
                FOREIGN KEY (job_id) REFERENCES JOB (job_id) ON DELETE CASCADE
            );

            CREATE TABLE APPOINTMENT (
                appointment_id SERIAL PRIMARY KEY,
                caregiver_user_id INT,
                member_user_id INT,
                appointment_date DATE,
                appointment_time TIME,
                work_hours INT,
                status VARCHAR(20),
                FOREIGN KEY (caregiver_user_id) REFERENCES CAREGIVER (caregiver_user_id) ON DELETE CASCADE, 
                FOREIGN KEY (member_user_id) REFERENCES MEMBERS (member_user_id) ON DELETE CASCADE
            );
        ''')
        connection.execute(create_tables_query)
        connection.commit()

# TASK 2:
def insert_data() :
    with engine.connect() as connection:
        insert_data_query = text('''
            INSERT INTO app_user (user_id,email, given_name, surname, city, phone_number, profile_description, password)
            VALUES
                (33,'askar@example.com', 'Askar', 'Askarov', 'Astana', '+700000000', 'Experienced caregiver for children.', 'pass101'),
                (1,'john@example.com', 'John', 'Doe', 'New York', '1234567890', 'Experienced caregiver for children.', 'pass123'),
                (2,'jane@example.com', 'Jane', 'Smith', 'Los Angeles', '9876543210', 'Babysitter with CPR certification.', 'pass456'),
                (3,'alice@example.com', 'Alice', 'Johnson', 'Chicago', '5555555555', 'Elderly care specialist with nursing background.', 'pass789'),
                (4,'bob@example.com', 'Bob', 'Williams', 'Houston', '1112223333', 'Experienced babysitter with first aid training.', 'passabc'),
                (5,'sarah@example.com', 'Sarah', 'Brown', 'Seattle', '4445556666', 'Caring and energetic playmate for children.', 'passdef'),
                (6,'michael@example.com', 'Michael', 'Davis', 'Boston', '7778889999', 'Nursing student with a passion for elder care.', 'passghi'),
                (7,'emily@example.com', 'Emily', 'Wilson', 'San Francisco', '2223334444', 'Responsible and patient babysitter for infants.', 'passjkl'),
                (8,'david@example.com', 'David', 'Martinez', 'Miami', '6667778888', 'Experienced caregiver for children with special needs.', 'passmno'),
                (9,'olivia@example.com', 'Olivia', 'Garcia', 'Dallas', '9990001111', 'Compassionate and reliable elderly care assistant.', 'passpqr'),
                (10,'william@example.com', 'William', 'Lopez', 'Phoenix', '3334445555', 'Creative and engaging playmate for kids of all ages.', 'passstu');  
                
            INSERT INTO CAREGIVER (caregiver_user_id, photo, gender, caregiving_type, hourly_rate)
            VALUES 
                (33, NULL, 'Male', 'caregiver for elderly', 8.50),
                (1, NULL, 'Male', 'babysitter', 12.50),
                (2, NULL, 'Female', 'babysitter', 15.00),
                (3, NULL, 'Female', 'caregiver for elderly', 18.00),
                (4, NULL, 'Male', 'caregiver for elderly', 20.00),
                (5, NULL, 'Female', 'playmate for children', 14.00),
                (6, NULL, 'Male', 'babysitter', 11.00),
                (7, NULL, 'Male', 'babysitter', 13.00),
                (8, NULL, 'Female', 'playmate for children', 16.00),
                (9, NULL, 'Female', 'caregiver for elderly', 22.00),
                (10, NULL, 'Male', 'caregiver for elderly', 19.50);
                    
            INSERT INTO app_user (user_id, email, given_name, surname, city, phone_number, profile_description, password)
            VALUES 
                (44, 'user33@example.com', 'Bolat', 'Bolatov', 'Almaty', '+77123717237', 'Seeking a trustworthy caregiver for my elderly grandmother.', 'pass44'),
                (11, 'user11@example.com', 'Emily', 'Johnson', 'New York', '1111111111', 'Seeking a trustworthy caregiver for my elderly grandmother.', 'pass11'),
                (12, 'user12@example.com', 'Michael', 'Garcia', 'Los Angeles', '2222222222', 'Looking for an experienced caregiver for my child with special needs.', 'pass12'),
                (13, 'user13@example.com', 'Sophia', 'Martinez', 'Chicago', '3333333333', 'In search of a responsible babysitter for my toddler.', 'pass13'),
                (14, 'user14@example.com', 'Olivia', 'Lopez', 'Houston', '4444444444', 'Seeking a compassionate caregiver for my disabled sibling.', 'pass14'),
                (15, 'user15@example.com', 'Liam', 'Hernandez', 'Miami', '5555555555', 'Looking for a reliable caregiver for my elderly parent.', 'pass15'),
                (16, 'user16@example.com', 'Ava', 'Robinson', 'San Francisco', '6666666666', 'In search of a friendly playmate for my child.', 'pass16'),
                (17, 'user17@example.com', 'Noah', 'Nguyen', 'Seattle', '7777777777', 'Seeking a dedicated caregiver for my aging pet.', 'pass17'),
                (18, 'user18@example.com', 'Isabella', 'Gonzalez', 'Dallas', '8888888888', 'Looking for an experienced caregiver for my sibling with special needs.', 'pass18'),
                (19, 'user19@example.com', 'James', 'Morales', 'Phoenix', '9999999999', 'Seeking a responsible caregiver for my elderly relative.', 'pass19'),
                (20, 'user20@example.com', 'Emma', 'Kim', 'Boston', '1010101010', 'Looking for a compassionate caregiver for my aging parent.', 'pass20');
                
            INSERT INTO MEMBERS (member_user_id, house_rules)
            VALUES 
                (44, 'No TV before homework.'),
                (11, 'No TV before homework.'),
                (12, 'No pets.'),
                (13, 'Strict diet plan and exercise routine for elderly parent.'),
                (14, 'No sugary snacks for the kids.'),
                (15, 'Daily outdoor playtime for children.'),
                (16, 'Weekly family movie night.'),
                (17, 'No pets.'),
                (18, 'Limit screen time for children.'),
                (19, 'Healthy meal prep for elderly member.'),
                (20, 'Designated play areas for children.');

            INSERT INTO ADDRESS (member_user_id, house_number, street, town)
            VALUES 
                (44, '123', 'Abay', 'Almaty'),
                (11, '123', 'Turan Street', 'Astana'),
                (12, '456', 'Expo', 'Astana'),
                (13, '789', 'Oak Avenue', 'Chicago'),
                (14, '101', 'Turan Street', 'Astana'),
                (15, '222', 'Maple Avenue', 'Miami'),
                (16, '333', 'Turan Street', 'Astana'),
                (17, '444', 'Uly Dala Street', 'Astana'),
                (18, '555', 'Birch Street', 'Dallas'),
                (19, '666', 'Turan Street', 'Astana'),
                (20, '777', 'Cherry Street', 'Boston');
                
                
            INSERT INTO JOB (job_id, member_user_id, required_caregiving_type, other_requirements, date_posted)
            VALUES 
                (11, 44, 'caregiver for elderly', 'Flexible schedule, evening hours preferred', CURRENT_DATE + INTERVAL '4' DAY),
                (12, 44, 'caregiver for elderly', 'Flexible schedule, evening hours preferred', CURRENT_DATE + INTERVAL '11' DAY),
                (13, 44, 'caregiver for elderly', 'Flexible schedule, evening hours preferred', CURRENT_DATE + INTERVAL '2' DAY),
                (1, 11, 'babysitter', 'Flexible schedule, evening hours preferred, gentle care', CURRENT_DATE + INTERVAL '2' DAY),
                (2, 12, 'caregiver for elderly', 'Experience with special needs children required, gentle care', CURRENT_DATE + INTERVAL '5' DAY),
                (3, 13, 'babysitter', 'CPR certification and first aid training needed', CURRENT_DATE + INTERVAL '7' DAY),
                (4, 14, 'caregiver for elderly', 'Comfortable with assisting in mobility', CURRENT_DATE + INTERVAL '10' DAY),
                (5, 15, 'babysitter', 'Must engage in educational activities', CURRENT_DATE + INTERVAL '12' DAY),
                (6, 16, 'playmate for children', 'Childcare certification preferred', CURRENT_DATE + INTERVAL '14' DAY),
                (7, 17, 'caregiver for elderly', 'Experience with pets is a plus', CURRENT_DATE + INTERVAL '17' DAY),
                (8, 18, 'babysitter', 'Experience with special needs children required', CURRENT_DATE + INTERVAL '20' DAY),
                (9, 19, 'playmate for children', 'Must organize creative play activities', CURRENT_DATE + INTERVAL '22' DAY),
                (10, 20, 'caregiver for elderly', 'Experience with medication administration, gentle care', CURRENT_DATE + INTERVAL '25' DAY);

            INSERT INTO JOB_APPLICATION (caregiver_user_id, job_id, date_applied)
            VALUES 
                (1, 3, CURRENT_DATE + INTERVAL '3' DAY), 
                (2, 5, CURRENT_DATE + INTERVAL '5' DAY), 
                (3, 7, CURRENT_DATE + INTERVAL '7' DAY), 
                (4, 9, CURRENT_DATE + INTERVAL '10' DAY), 
                (5, 10, CURRENT_DATE + INTERVAL '12' DAY), 
                (6, 2, CURRENT_DATE + INTERVAL '14' DAY), 
                (7, 4, CURRENT_DATE + INTERVAL '17' DAY), 
                (8, 6, CURRENT_DATE + INTERVAL '20' DAY), 
                (9, 8, CURRENT_DATE + INTERVAL '22' DAY), 
                (10, 1, CURRENT_DATE + INTERVAL '25' DAY); 

            INSERT INTO APPOINTMENT (appointment_id, caregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status)
            VALUES 
                (1, 1, 13, CURRENT_DATE + INTERVAL '3' DAY, '09:00', 3, 'confirmed'),
                (2, 2, 15, CURRENT_DATE + INTERVAL '5' DAY, '10:00', 4, 'confirmed'),
                (3, 5, 13, CURRENT_DATE + INTERVAL '7' DAY, '11:00', 2, 'declined'),
                (4, 4, 14, CURRENT_DATE + INTERVAL '10' DAY, '12:00', 5, 'pending'),
                (5, 3, 17, CURRENT_DATE + INTERVAL '12' DAY, '13:00', 6, 'confirmed'),
                (6, 6, 18, CURRENT_DATE + INTERVAL '14' DAY, '14:00', 3, 'declined'),
                (7, 7, 12, CURRENT_DATE + INTERVAL '17' DAY, '15:00', 4, 'pending'),
                (8, 8, 16, CURRENT_DATE + INTERVAL '20' DAY, '16:00', 5, 'confirmed'),
                (9, 9, 19, CURRENT_DATE + INTERVAL '22' DAY, '17:00', 6, 'pending'),
                (10, 10, 20, CURRENT_DATE + INTERVAL '25' DAY, '18:00', 4, 'declined');    
        ''')
        connection.execute(insert_data_query)
        connection.commit()

# TASK 3: 
def update_phone_number() :
    name = 'Askar'
    surname = 'Askarov'
    number = '+77771010001'
    with engine.connect() as connection:
        update_phone_number_query = text('''
            UPDATE app_user
            SET phone_number = :number
            WHERE given_name = :name AND surname = :surname;
        ''')
        connection.execute(update_phone_number_query, {'name' : name, 'surname' : surname, 'number' : number})
        connection.commit()

def add_commission_fee() :
    with engine.connect() as connection:
        add_commission_fee_query = text('''
            UPDATE caregiver
            SET hourly_rate = CASE 
                WHEN hourly_rate < 9 THEN hourly_rate + 0.5
                ELSE hourly_rate * 1.10
                END;
        ''')
        connection.execute(add_commission_fee_query)
        connection.commit()

# TASK 4:
def delete_jobs():
    with engine.connect() as connection:
        delete_jobs_query = text('''
            DELETE FROM job
            WHERE member_user_id = (
                SELECT user_id
                FROM app_user
                WHERE given_name = 'Bolat' AND surname = 'Bolatov'
            )
        ''')
        connection.execute(delete_jobs_query)
        connection.commit()

def delete_members():
    with engine.connect() as connection:
        delete_members_query = text('''
            DELETE FROM app_user 
            WHERE user_id IN (
                SELECT m.member_user_id
                        FROM MEMBERS m
                        JOIN ADDRESS a ON m.member_user_id = a.member_user_id
                        WHERE a.street = 'Turan Street'
            )
        ''')
        connection.execute(delete_members_query)
        connection.commit()

# TASK 5:

def member_caregiver_names():
    with engine.connect() as connection:
        member_caregiver_names_query = text('''
            SELECT M.given_name AS member_name , 
                C.given_name AS caregiver_name FROM 
                (app_user JOin appointment ON app_user.user_id = appointment.member_user_id) M
                JOIN
                (app_user JOin appointment ON app_user.user_id = appointment.caregiver_user_id) C 
                ON M.appointment_id = C.appointment_id  
                WHERE M.status = 'confirmed';
        ''')
        result = connection.execute(member_caregiver_names_query)
        for row in result:
            print(f'Member: {row[0]}; Caregiver: {row[1]}')

def find_gentle():
    with engine.connect() as connection:
        find_gentle_query = text('''
            SELECT job_id FROM job
            WHERE other_requirements LIKE '%gentle%';
        ''')
        result = connection.execute(find_gentle_query)
        for row in result:
            print(row[0])

def babysitters_work_hours():
    with engine.connect() as connection:
        babysitters_work_hours_query = text('''
            SELECT work_hours from 
            appointment A join caregiver C on A.caregiver_user_id = C.caregiver_user_id
            WHERE caregiving_type = 'babysitter';
        ''')
        result = connection.execute(babysitters_work_hours_query)
        for row in result:
            print(row[0])

def members_in_astana() :
    with engine.connect() as connection:
        babysitters_work_hours_query = text('''
            SELECT member_user_id FROM
            (members NATURAL JOIN address)
            NATURAL JOIN job 
            WHERE required_caregiving_type = 'caregiver for elderly' AND town = 'Astana' AND house_rules = 'No pets.'
            GROUP BY member_user_id;
        ''')
        result = connection.execute(babysitters_work_hours_query)
        for row in result:
            print(row[0])

# TASK 6:

def count_applicants() :
    with engine.connect() as connection:
        count_applicants_query = text('''
            SELECT j.job_id,
            COUNT(ja.caregiver_user_id) AS num_applicants
            FROM JOB j JOIN
                members m ON j.member_user_id = m.member_user_id
            LEFT JOIN
                JOB_APPLICATION ja ON j.job_id = ja.job_id
            GROUP BY j.job_id
            ORDER BY j.job_id;
        ''')
        result = connection.execute(count_applicants_query)
        for row in result:
            print(f"Job ID: {row[0]} - Number of Applicants: {row[1]}")

def count_total_hours() :
    with engine.connect() as connection:
        count_total_hours_query = text('''
            SELECT
            SUM(a.work_hours) AS total_hours_spent
            FROM APPOINTMENT a JOIN CAREGIVER c 
            ON a.caregiver_user_id = c.caregiver_user_id
            WHERE a.status = 'confirmed';
        ''')
        result = connection.execute(count_total_hours_query)
        for row in result:
            print(row[0])

def average_pay_caregivers() :
    with engine.connect() as connection:
        average_pay_caregivers_query = text('''
            SELECT
            AVG(c.hourly_rate * a.work_hours) AS average_pay
            FROM APPOINTMENT a JOIN CAREGIVER c 
            ON a.caregiver_user_id = c.caregiver_user_id
            WHERE a.status = 'confirmed';
        ''')
        result = connection.execute(average_pay_caregivers_query)
        for row in result:
            print(row[0])

def caregivers_pay_above_average() :
    with engine.connect() as connection:
        caregivers_pay_above_average_query = text('''
            SELECT C.caregiver_user_id, 
            A.work_hours * C.hourly_rate AS pay FROM
            caregiver C JOIN appointment A ON C.caregiver_user_id = A.caregiver_user_id
            WHERE A.status = 'confirmed' AND A.work_hours * C.hourly_rate > (SELECT
                                        AVG(c.hourly_rate * a.work_hours) AS average_pay
                                        FROM APPOINTMENT a JOIN CAREGIVER c 
                                        ON a.caregiver_user_id = c.caregiver_user_id
                                        WHERE a.status = 'confirmed')
        ''')
        result = connection.execute(caregivers_pay_above_average_query)
        for row in result:
            print(f'Caregiver {row[0]}: ${row[1]}')

# TASK 7:

def calculate_total_cost() :
     with engine.connect() as connection:
        calculate_total_cost_query = text('''
            SELECT
            SUM(c.hourly_rate * a.work_hours) AS total_cost
            FROM CAREGIVER c JOIN APPOINTMENT a 
            ON c.caregiver_user_id = a.caregiver_user_id
            WHERE a.status = 'confirmed';
        ''')
        result = connection.execute(calculate_total_cost_query)
        for row in result:
            print(row[0])

# TASK 8:
def view_applicants() :
    with engine.connect() as connection:
        view_applicants_query = text('''
            SELECT U.given_name, U.surname, J.job_id, J.date_applied 
            FROM (job_application J NATURAL JOIN caregiver C) 
            JOIN app_user U ON c.caregiver_user_id = U.user_id
        ''')
        result = connection.execute(view_applicants_query)
        for row in result:
            print(f'{row[0]} {row[1]} - Applied to job {row[2]} ({row[3]})')

# TASK 1:
# create_tables()

# TASK 2:
# insert_data()

# TASK 3:
# update_phone_number()
# add_commission_fee()

# TASK 4:
# delete_jobs()
# delete_members()

# TASK 5:
# member_caregiver_names()
# find_gentle()
# babysitters_work_hours()
# members_in_astana()


# TASK 6:
# count_applicants()
# count_total_hours()
# average_pay_caregivers()
# caregivers_pay_above_average()

# TASK 7:
# calculate_total_cost()

# TASK 8:
# view_applicants()


engine.dispose()

