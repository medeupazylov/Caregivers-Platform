--
-- PostgreSQL database dump
--

-- Dumped from database version 14.10 (Homebrew)
-- Dumped by pg_dump version 14.10 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: address; Type: TABLE; Schema: public; Owner: medeupazylov
--

CREATE TABLE public.address (
    member_user_id integer NOT NULL,
    house_number character varying(10),
    street character varying(50),
    town character varying(50)
);


ALTER TABLE public.address OWNER TO medeupazylov;

--
-- Name: app_user; Type: TABLE; Schema: public; Owner: medeupazylov
--

CREATE TABLE public.app_user (
    user_id integer NOT NULL,
    email character varying(100),
    given_name character varying(50),
    surname character varying(50),
    city character varying(50),
    phone_number character varying(15),
    profile_description text,
    password character varying(100)
);


ALTER TABLE public.app_user OWNER TO medeupazylov;

--
-- Name: app_user_user_id_seq; Type: SEQUENCE; Schema: public; Owner: medeupazylov
--

CREATE SEQUENCE public.app_user_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_user_user_id_seq OWNER TO medeupazylov;

--
-- Name: app_user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medeupazylov
--

ALTER SEQUENCE public.app_user_user_id_seq OWNED BY public.app_user.user_id;


--
-- Name: appointment; Type: TABLE; Schema: public; Owner: medeupazylov
--

CREATE TABLE public.appointment (
    appointment_id integer NOT NULL,
    caregiver_user_id integer,
    member_user_id integer,
    appointment_date date,
    appointment_time time without time zone,
    work_hours integer,
    status character varying(20)
);


ALTER TABLE public.appointment OWNER TO medeupazylov;

--
-- Name: appointment_appointment_id_seq; Type: SEQUENCE; Schema: public; Owner: medeupazylov
--

CREATE SEQUENCE public.appointment_appointment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.appointment_appointment_id_seq OWNER TO medeupazylov;

--
-- Name: appointment_appointment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medeupazylov
--

ALTER SEQUENCE public.appointment_appointment_id_seq OWNED BY public.appointment.appointment_id;


--
-- Name: caregiver; Type: TABLE; Schema: public; Owner: medeupazylov
--

CREATE TABLE public.caregiver (
    caregiver_user_id integer NOT NULL,
    photo bytea,
    gender character varying(10),
    caregiving_type character varying(50),
    hourly_rate numeric(10,2)
);


ALTER TABLE public.caregiver OWNER TO medeupazylov;

--
-- Name: caregiver_caregiver_user_id_seq; Type: SEQUENCE; Schema: public; Owner: medeupazylov
--

CREATE SEQUENCE public.caregiver_caregiver_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.caregiver_caregiver_user_id_seq OWNER TO medeupazylov;

--
-- Name: caregiver_caregiver_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medeupazylov
--

ALTER SEQUENCE public.caregiver_caregiver_user_id_seq OWNED BY public.caregiver.caregiver_user_id;


--
-- Name: job; Type: TABLE; Schema: public; Owner: medeupazylov
--

CREATE TABLE public.job (
    job_id integer NOT NULL,
    member_user_id integer,
    required_caregiving_type character varying(50),
    other_requirements text,
    date_posted date
);


ALTER TABLE public.job OWNER TO medeupazylov;

--
-- Name: job_application; Type: TABLE; Schema: public; Owner: medeupazylov
--

CREATE TABLE public.job_application (
    caregiver_user_id integer,
    job_id integer,
    date_applied date
);


ALTER TABLE public.job_application OWNER TO medeupazylov;

--
-- Name: job_job_id_seq; Type: SEQUENCE; Schema: public; Owner: medeupazylov
--

CREATE SEQUENCE public.job_job_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.job_job_id_seq OWNER TO medeupazylov;

--
-- Name: job_job_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medeupazylov
--

ALTER SEQUENCE public.job_job_id_seq OWNED BY public.job.job_id;


--
-- Name: members; Type: TABLE; Schema: public; Owner: medeupazylov
--

CREATE TABLE public.members (
    member_user_id integer NOT NULL,
    house_rules text
);


ALTER TABLE public.members OWNER TO medeupazylov;

--
-- Name: members_member_user_id_seq; Type: SEQUENCE; Schema: public; Owner: medeupazylov
--

CREATE SEQUENCE public.members_member_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.members_member_user_id_seq OWNER TO medeupazylov;

--
-- Name: members_member_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medeupazylov
--

ALTER SEQUENCE public.members_member_user_id_seq OWNED BY public.members.member_user_id;


--
-- Name: app_user user_id; Type: DEFAULT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.app_user ALTER COLUMN user_id SET DEFAULT nextval('public.app_user_user_id_seq'::regclass);


--
-- Name: appointment appointment_id; Type: DEFAULT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.appointment ALTER COLUMN appointment_id SET DEFAULT nextval('public.appointment_appointment_id_seq'::regclass);


--
-- Name: caregiver caregiver_user_id; Type: DEFAULT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.caregiver ALTER COLUMN caregiver_user_id SET DEFAULT nextval('public.caregiver_caregiver_user_id_seq'::regclass);


--
-- Name: job job_id; Type: DEFAULT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.job ALTER COLUMN job_id SET DEFAULT nextval('public.job_job_id_seq'::regclass);


--
-- Name: members member_user_id; Type: DEFAULT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.members ALTER COLUMN member_user_id SET DEFAULT nextval('public.members_member_user_id_seq'::regclass);


--
-- Data for Name: address; Type: TABLE DATA; Schema: public; Owner: medeupazylov
--

COPY public.address (member_user_id, house_number, street, town) FROM stdin;
44	123	Abay	Almaty
12	456	Expo	Astana
13	789	Oak Avenue	Chicago
15	222	Maple Avenue	Miami
17	444	Uly Dala Street	Astana
18	555	Birch Street	Dallas
20	777	Cherry Street	Boston
\.


--
-- Data for Name: app_user; Type: TABLE DATA; Schema: public; Owner: medeupazylov
--

COPY public.app_user (user_id, email, given_name, surname, city, phone_number, profile_description, password) FROM stdin;
1	john@example.com	John	Doe	New York	1234567890	Experienced caregiver for children.	pass123
2	jane@example.com	Jane	Smith	Los Angeles	9876543210	Babysitter with CPR certification.	pass456
3	alice@example.com	Alice	Johnson	Chicago	5555555555	Elderly care specialist with nursing background.	pass789
4	bob@example.com	Bob	Williams	Houston	1112223333	Experienced babysitter with first aid training.	passabc
5	sarah@example.com	Sarah	Brown	Seattle	4445556666	Caring and energetic playmate for children.	passdef
6	michael@example.com	Michael	Davis	Boston	7778889999	Nursing student with a passion for elder care.	passghi
7	emily@example.com	Emily	Wilson	San Francisco	2223334444	Responsible and patient babysitter for infants.	passjkl
8	david@example.com	David	Martinez	Miami	6667778888	Experienced caregiver for children with special needs.	passmno
9	olivia@example.com	Olivia	Garcia	Dallas	9990001111	Compassionate and reliable elderly care assistant.	passpqr
10	william@example.com	William	Lopez	Phoenix	3334445555	Creative and engaging playmate for kids of all ages.	passstu
44	user33@example.com	Bolat	Bolatov	Almaty	+77123717237	Seeking a trustworthy caregiver for my elderly grandmother.	pass44
12	user12@example.com	Michael	Garcia	Los Angeles	2222222222	Looking for an experienced caregiver for my child with special needs.	pass12
13	user13@example.com	Sophia	Martinez	Chicago	3333333333	In search of a responsible babysitter for my toddler.	pass13
15	user15@example.com	Liam	Hernandez	Miami	5555555555	Looking for a reliable caregiver for my elderly parent.	pass15
17	user17@example.com	Noah	Nguyen	Seattle	7777777777	Seeking a dedicated caregiver for my aging pet.	pass17
18	user18@example.com	Isabella	Gonzalez	Dallas	8888888888	Looking for an experienced caregiver for my sibling with special needs.	pass18
20	user20@example.com	Emma	Kim	Boston	1010101010	Looking for a compassionate caregiver for my aging parent.	pass20
33	askar@example.com	Askar	Askarov	Astana	+77771010001	Experienced caregiver for children.	pass101
\.


--
-- Data for Name: appointment; Type: TABLE DATA; Schema: public; Owner: medeupazylov
--

COPY public.appointment (appointment_id, caregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status) FROM stdin;
1	1	13	2023-11-24	09:00:00	3	confirmed
2	2	15	2023-11-26	10:00:00	4	confirmed
3	5	13	2023-11-28	11:00:00	2	declined
5	3	17	2023-12-03	13:00:00	6	confirmed
6	6	18	2023-12-05	14:00:00	3	declined
7	7	12	2023-12-08	15:00:00	4	pending
10	10	20	2023-12-16	18:00:00	4	declined
\.


--
-- Data for Name: caregiver; Type: TABLE DATA; Schema: public; Owner: medeupazylov
--

COPY public.caregiver (caregiver_user_id, photo, gender, caregiving_type, hourly_rate) FROM stdin;
33	\N	Male	caregiver for elderly	9.00
1	\N	Male	babysitter	13.75
2	\N	Female	babysitter	16.50
3	\N	Female	caregiver for elderly	19.80
4	\N	Male	caregiver for elderly	22.00
5	\N	Female	playmate for children	15.40
6	\N	Male	babysitter	12.10
7	\N	Male	babysitter	14.30
8	\N	Female	playmate for children	17.60
9	\N	Female	caregiver for elderly	24.20
10	\N	Male	caregiver for elderly	21.45
\.


--
-- Data for Name: job; Type: TABLE DATA; Schema: public; Owner: medeupazylov
--

COPY public.job (job_id, member_user_id, required_caregiving_type, other_requirements, date_posted) FROM stdin;
2	12	caregiver for elderly	Experience with special needs children required, gentle care	2023-11-26
3	13	babysitter	CPR certification and first aid training needed	2023-11-28
5	15	babysitter	Must engage in educational activities	2023-12-03
7	17	caregiver for elderly	Experience with pets is a plus	2023-12-08
8	18	babysitter	Experience with special needs children required	2023-12-11
10	20	caregiver for elderly	Experience with medication administration, gentle care	2023-12-16
\.


--
-- Data for Name: job_application; Type: TABLE DATA; Schema: public; Owner: medeupazylov
--

COPY public.job_application (caregiver_user_id, job_id, date_applied) FROM stdin;
1	3	2023-11-24
2	5	2023-11-26
3	7	2023-11-28
5	10	2023-12-03
6	2	2023-12-05
9	8	2023-12-13
\.


--
-- Data for Name: members; Type: TABLE DATA; Schema: public; Owner: medeupazylov
--

COPY public.members (member_user_id, house_rules) FROM stdin;
44	No TV before homework.
12	No pets.
13	Strict diet plan and exercise routine for elderly parent.
15	Daily outdoor playtime for children.
17	No pets.
18	Limit screen time for children.
20	Designated play areas for children.
\.


--
-- Name: app_user_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medeupazylov
--

SELECT pg_catalog.setval('public.app_user_user_id_seq', 1, false);


--
-- Name: appointment_appointment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medeupazylov
--

SELECT pg_catalog.setval('public.appointment_appointment_id_seq', 1, false);


--
-- Name: caregiver_caregiver_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medeupazylov
--

SELECT pg_catalog.setval('public.caregiver_caregiver_user_id_seq', 1, false);


--
-- Name: job_job_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medeupazylov
--

SELECT pg_catalog.setval('public.job_job_id_seq', 1, false);


--
-- Name: members_member_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medeupazylov
--

SELECT pg_catalog.setval('public.members_member_user_id_seq', 1, false);


--
-- Name: address address_pkey; Type: CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_pkey PRIMARY KEY (member_user_id);


--
-- Name: app_user app_user_pkey; Type: CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.app_user
    ADD CONSTRAINT app_user_pkey PRIMARY KEY (user_id);


--
-- Name: appointment appointment_pkey; Type: CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_pkey PRIMARY KEY (appointment_id);


--
-- Name: caregiver caregiver_pkey; Type: CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.caregiver
    ADD CONSTRAINT caregiver_pkey PRIMARY KEY (caregiver_user_id);


--
-- Name: job job_pkey; Type: CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.job
    ADD CONSTRAINT job_pkey PRIMARY KEY (job_id);


--
-- Name: members members_pkey; Type: CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_pkey PRIMARY KEY (member_user_id);


--
-- Name: address address_member_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_member_user_id_fkey FOREIGN KEY (member_user_id) REFERENCES public.members(member_user_id) ON DELETE CASCADE;


--
-- Name: appointment appointment_caregiver_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_caregiver_user_id_fkey FOREIGN KEY (caregiver_user_id) REFERENCES public.caregiver(caregiver_user_id) ON DELETE CASCADE;


--
-- Name: appointment appointment_member_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_member_user_id_fkey FOREIGN KEY (member_user_id) REFERENCES public.members(member_user_id) ON DELETE CASCADE;


--
-- Name: caregiver caregiver_caregiver_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.caregiver
    ADD CONSTRAINT caregiver_caregiver_user_id_fkey FOREIGN KEY (caregiver_user_id) REFERENCES public.app_user(user_id) ON DELETE CASCADE;


--
-- Name: job_application job_application_caregiver_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.job_application
    ADD CONSTRAINT job_application_caregiver_user_id_fkey FOREIGN KEY (caregiver_user_id) REFERENCES public.caregiver(caregiver_user_id) ON DELETE CASCADE;


--
-- Name: job_application job_application_job_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.job_application
    ADD CONSTRAINT job_application_job_id_fkey FOREIGN KEY (job_id) REFERENCES public.job(job_id) ON DELETE CASCADE;


--
-- Name: job job_member_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.job
    ADD CONSTRAINT job_member_user_id_fkey FOREIGN KEY (member_user_id) REFERENCES public.members(member_user_id) ON DELETE CASCADE;


--
-- Name: members members_member_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medeupazylov
--

ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_member_user_id_fkey FOREIGN KEY (member_user_id) REFERENCES public.app_user(user_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

