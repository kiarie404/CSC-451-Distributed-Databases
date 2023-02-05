# create global schema
create_job_description_table = """
CREATE TABLE job_descriptions (
    job_id INT NOT NULL ,
    job_title VARCHAR(256) NOT NULL ,
    job_pay DECIMAL NOT NULL ,
    PRIMARY KEY (job_id))
"""

create_projects_table = """
    CREATE TABLE projects (
    project_id INT NOT NULL ,
    project_name VARCHAR(256) NOT NULL ,
    project_budget DECIMAL NOT NULL ,
    project_location VARCHAR(256) NOT NULL ,
    PRIMARY KEY (project_id)) 
"""

create_projects_table_fragment_1 = """
    CREATE TABLE projects_fragment_1 (
    project_id INT NOT NULL ,
    project_name VARCHAR(256) NOT NULL ,
    project_budget DECIMAL NOT NULL ,
    project_location VARCHAR(256) NOT NULL ,
    PRIMARY KEY (project_id)) 
"""

create_projects_table_fragment_2 = """
    CREATE TABLE projects_fragment_2 (
    project_id INT NOT NULL ,
    project_name VARCHAR(256) NOT NULL ,
    project_budget DECIMAL NOT NULL ,
    project_location VARCHAR(256) NOT NULL ,
    PRIMARY KEY (project_id)) 
"""

create_employees_table = """
    CREATE TABLE employees (
    employee_id INT NOT NULL ,
    employee_name VARCHAR(256) NOT NULL ,
    employee_job_id INT NOT NULL ,
    PRIMARY KEY (employee_id));

    ALTER TABLE employees 
    ADD FOREIGN KEY (employee_job_id) 
    REFERENCES job_descriptions(job_id) ON DELETE CASCADE ON UPDATE CASCADE; 
"""

create_assignations_table = """
    CREATE TABLE assignations (
    assignation_id INT NOT NULL ,
    employee_id INT NOT NULL ,
    project_id INT NOT NULL ,
    project_duration INT NOT NULL ,
    PRIMARY KEY (assignation_id));

    ALTER TABLE assignations ADD FOREIGN KEY (employee_id) 
    REFERENCES employees(employee_id) ON DELETE CASCADE ON UPDATE CASCADE;
    ALTER TABLE assignations ADD FOREIGN KEY (project_id) 
    REFERENCES projects(project_id) ON DELETE CASCADE ON UPDATE CASCADE; 
"""

create_assignations_table_fragment_1 = """
    CREATE TABLE assignations_fragment_1 (
    assignation_id INT NOT NULL ,
    employee_id INT NOT NULL ,
    project_id INT NOT NULL ,
    project_duration INT NOT NULL ,
    PRIMARY KEY (assignation_id));

    ALTER TABLE assignations_fragment_1 ADD FOREIGN KEY (employee_id) 
    REFERENCES employees(employee_id) ON DELETE CASCADE ON UPDATE CASCADE;
    ALTER TABLE assignations_fragment_1 ADD FOREIGN KEY (project_id) 
    REFERENCES projects_fragment_1(project_id) ON DELETE CASCADE ON UPDATE CASCADE; 
"""

create_assignations_table_fragment_2 = """
    CREATE TABLE assignations_fragment_2 (
    assignation_id INT NOT NULL ,
    employee_id INT NOT NULL ,
    project_id INT NOT NULL ,
    project_duration INT NOT NULL ,
    PRIMARY KEY (assignation_id));

    ALTER TABLE assignations_fragment_2 ADD FOREIGN KEY (employee_id) 
    REFERENCES employees(employee_id) ON DELETE CASCADE ON UPDATE CASCADE;
    ALTER TABLE assignations_fragment_2 ADD FOREIGN KEY (project_id) 
    REFERENCES projects_fragment_2(project_id) ON DELETE CASCADE ON UPDATE CASCADE; 
"""

populate_job_descriptions_table = """
INSERT INTO job_descriptions
 (job_id, job_title, job_pay)
 VALUES ('1', 'Senior Systems Developer', '1000000'),
 ('2', 'Junior Rust Developer', '100000'), ('3', 'Front End Developer', '100000'), ('4', 'Backend Developer', '100000'),
 ('5', 'Experienced Rust Developer', '500000') 
"""

populate_projects_table = """
INSERT INTO projects (project_id, project_name, project_budget, project_location)
VALUES ('1', 'Nairobi traffic system', '1000000', 'Nairobi'),
('2', 'Kericho smart farm', '2000000', 'Kericho'),
('3', 'Nakuru Nawasco site', '100000', 'Nakuru'),
('4', 'Company Website', '50000', 'Nairobi') 
"""

populate_projects_table_Nakuru_fragment_1 = """ 
INSERT INTO projects_fragment_1 (project_id, project_name, project_budget, project_location)
VALUES ('3', 'Nakuru Nawasco site', '100000', 'Nakuru')
"""

populate_projects_table_Kericho_fragment_2 = """
INSERT INTO projects_fragment_2 (project_id, project_name, project_budget, project_location)
VALUES ('2', 'Kericho smart farm', '2000000', 'Kericho')
"""
populate_projects_table_Nairobi_fragment_1 = """
INSERT INTO projects_fragment_1 (project_id, project_name, project_budget, project_location)
VALUES ('4', 'Company Website', '50000', 'Nairobi')
"""

populate_projects_table_Nairobi_fragment_2 = """
INSERT INTO projects_fragment_2 (project_id, project_name, project_budget, project_location)
VALUES ('1', 'Nairobi traffic system', '1000000', 'Nairobi')
"""

get_nakuru_assignation_fragment = """
SELECT assignations.assignation_id, assignations.employee_id, assignations.project_id, assignations.project_duration
FROM assignations
WHERE assignations.project_id = '3'
"""

get_kericho_assignation_fragment = """
SELECT assignations.assignation_id, assignations.employee_id, assignations.project_id, assignations.project_duration
FROM assignations
WHERE assignations.project_id = '2'
"""
get_nairobi_assignation_fragment = """
SELECT assignations.assignation_id, assignations.employee_id, assignations.project_id, assignations.project_duration
FROM assignations
WHERE assignations.project_id = '4'
"""

populate_employees_table = """
INSERT INTO employees (employee_id, employee_name, employee_job_id) 
 VALUES ('1', 'James Kiarie', '5'),
('2', 'Michael Muchai', '5'),
('3', 'Samuel Njuguna', '5'),
('4', 'Martin Ndungu', '5'),
('5', 'Fredrick Wainaina', '5'),
('6', 'George Odemo', '1'), ('7', 'Kimathi Meriti', '4'), ('8', 'Japheph Sunday', '4'), ('9', 'Faith Auma', '1'),
('10', 'Joy Wanja', '4'),
('11', 'Yvonne Kosgei', '2'),
('12', 'Caroline Kemunto', '2'),
('13', 'Sarah Basweti', '2'),
('14', 'John Kilo', '4'),
('15', 'Robert Ouma', '3'),
('16', 'Calvin Kimaiu', '3'),
('17', 'Hassan Muli', '3') 
"""

populate_assignations_table = """
INSERT INTO "assignations" ("assignation_id", "employee_id", "project_id", "project_duration") VALUES ('1', '1', '1', '12'), ('2', '2', '1', '12'), ('3', '3', '1', '12'), ('4', '6', '1', '12'), ('5', '9', '2', '6'), ('6', '9', '1', '5'), ('7', '11', '1', '10'), ('8', '12', '2', '8'), ('18', '13', '2', '8'), ('9', '15', '4', '2'), ('10', '16', '3', '2'), ('11', '17', '3', '2'), ('12', '7', '4', '2'), ('13', '8', '4', '2'), ('14', '10', '3', '2'), ('15', '14', '3', '2'), ('16', '4', '1', '10'), ('17', '5', '2', '12') 
"""

populate_assignations_table_Nakuru_fragment_1 = """
INSERT INTO assignations_fragment_1 (assignation_id, employee_id, project_id, project_duration) VALUES (10, 16, 3, 2), (11, 17, 3, 2), (14, 10, 3, 2), (15, 14, 3, 2)
"""

populate_assignations_table_Kericho_fragment_2 = """
INSERT INTO assignations_fragment_2 (assignation_id, employee_id, project_id, project_duration) VALUES (5, 9, 2, 6), (8, 12, 2, 8), (18, 13, 2, 8), (17, 5, 2, 12)
"""

populate_assignations_table_Nairobi_fragment_1 = """
INSERT INTO assignations_fragment_1 (assignation_id, employee_id, project_id, project_duration) VALUES (9, 15, 4, 2), (12, 7, 4, 2), (13, 8, 4, 2)
"""

populate_assignations_table_Nairobi_fragment_2 = """
INSERT INTO assignations_fragment_2 (assignation_id, employee_id, project_id, project_duration) VALUES (1, 1, 1, 12), (2, 2, 1, 12), (3, 3, 1, 12), (4, 6, 1, 12), (6, 9, 1, 5), (7, 11, 1, 10), (16, 4, 1, 10)
"""

get_high_paid_employees = """
SELECT employees.employee_name, job_descriptions.job_title, job_descriptions.job_pay
FROM employees, job_descriptions
WHERE employees.employee_job_id = job_descriptions.job_id
AND job_descriptions.job_pay >= 200000;
"""




# Queries dealing with Reconstruction
# 1. Queries to create reconstructed empty schema
create_reconstructed_job_description_table = """
CREATE TABLE reconstructed_job_descriptions (
    job_id INT NOT NULL ,
    job_title VARCHAR(256) NOT NULL ,
    job_pay DECIMAL NOT NULL ,
    PRIMARY KEY (job_id))
"""
create_reconstructed_projects_table = """
    CREATE TABLE reconstructed_projects (
    project_id INT NOT NULL ,
    project_name VARCHAR(256) NOT NULL ,
    project_budget DECIMAL NOT NULL ,
    project_location VARCHAR(256) NOT NULL ,
    PRIMARY KEY (project_id)) 
"""
create_reconstructed_employees_table = """
    CREATE TABLE reconstructed_employees (
    employee_id INT NOT NULL ,
    employee_name VARCHAR(256) NOT NULL ,
    employee_job_id INT NOT NULL ,
    PRIMARY KEY (employee_id));

    ALTER TABLE reconstructed_employees 
    ADD FOREIGN KEY (employee_job_id) 
    REFERENCES reconstructed_job_descriptions(job_id) ON DELETE CASCADE ON UPDATE CASCADE; 
"""
create_reconstructed_assignations_table = """
    CREATE TABLE reconstructed_assignations (
    assignation_id INT NOT NULL ,
    employee_id INT NOT NULL ,
    project_id INT NOT NULL ,
    project_duration INT NOT NULL ,
    PRIMARY KEY (assignation_id));

    ALTER TABLE reconstructed_assignations ADD FOREIGN KEY (employee_id) 
    REFERENCES reconstructed_employees(employee_id) ON DELETE CASCADE ON UPDATE CASCADE;
    ALTER TABLE reconstructed_assignations ADD FOREIGN KEY (project_id) 
    REFERENCES reconstructed_projects(project_id) ON DELETE CASCADE ON UPDATE CASCADE; 
"""

# Queries to populate the recontracted schema
