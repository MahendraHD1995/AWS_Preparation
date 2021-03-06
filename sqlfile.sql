--
-- PostgreSQL database dump
--

-- Dumped from database version 13.5 (Ubuntu 13.5-0ubuntu0.21.04.1)
-- Dumped by pg_dump version 13.5 (Ubuntu 13.5-0ubuntu0.21.04.1)

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
-- Name: ec2; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ec2 (
    id integer NOT NULL,
    question text NOT NULL,
    option_a text,
    option_b text,
    option_c text,
    option_d text,
    option_e text,
    answer text
);


ALTER TABLE public.ec2 OWNER TO postgres;

--
-- Name: ec2_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.ec2 ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.ec2_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: ec2; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ec2 (id, question, option_a, option_b, option_c, option_d, option_e, answer) FROM stdin;
1	What does the following command do with respect to the Amazon EC2 security groups?\nec2-create-group CreateSecurityGroup	Groups the user created security groups into a new group for easy access.	Creates a new security group for use with your account.	Creates a new group inside the security group.	Creates a new rule inside the security group.	\N	OPTION_B
2	A web application allows customers to upload orders to an S3 bucket. The resulting Amazon S3\nevents trigger a Lambda function that inserts a message to an SQS queue. A single EC2 instance\nreads messages from the queue, processes them, and stores them in an DynamoDB table partitioned\nby unique order ID. Next month traffic is expected to increase by a factor of 10 and a Solutions\nArchitect is reviewing the architecture for possible scaling problems.\nWhich component is MOST likely to need re-architecting to be able to scale to accommodate the new\ntraffic?	Lambda function	SQS queue	EC2 instance	DynamoDB table	\N	OPTION_C
3	A web application allows customers to upload orders to an S3 bucket. The resulting Amazon S3\nevents trigger a Lambda function that inserts a message to an SQS queue. A single EC2 instance\nreads messages from the queue, processes them, and stores them in an DynamoDB table partitioned\nby unique order ID. Next month traffic is expected to increase by a factor of 10 and a Solutions\nArchitect is reviewing the architecture for possible scaling problems.\nWhich component is MOST likely to need re-architecting to be able to scale to accommodate the new\ntraffic?	Lambda function	SQS queue	EC2 instance	DynamoDB table	\N	OPTION_C
4	A web application allows customers to upload orders to an S3 bucket. The resulting Amazon S3\nevents trigger a Lambda function that inserts a message to an SQS queue. A single EC2 instance\nreads messages from the queue, processes them, and stores them in an DynamoDB table partitioned\nby unique order ID. Next month traffic is expected to increase by a factor of 10 and a Solutions\nArchitect is reviewing the architecture for possible scaling problems.\nWhich component is MOST likely to need re-architecting to be able to scale to accommodate the new\ntraffic?	Lambda function	SQS queue	EC2 instance	DynamoDB table	\N	OPTION_C
5	A web application allows customers to upload orders to an S3 bucket. The resulting Amazon S3\nevents trigger a Lambda function that inserts a message to an SQS queue. A single EC2 instance\nreads messages from the queue, processes them, and stores them in an DynamoDB table partitioned\nby unique order ID. Next month traffic is expected to increase by a factor of 10 and a Solutions\nArchitect is reviewing the architecture for possible scaling problems.\nWhich component is MOST likely to need re-architecting to be able to scale to accommodate the new\ntraffic?	Lambda function	SQS queue	EC2 instance	DynamoDB table	\N	OPTION_C
6	A web application allows customers to upload orders to an S3 bucket. The resulting Amazon S3\nevents trigger a Lambda function that inserts a message to an SQS queue. A single EC2 instance\nreads messages from the queue, processes them, and stores them in an DynamoDB table partitioned\nby unique order ID. Next month traffic is expected to increase by a factor of 10 and a Solutions\nArchitect is reviewing the architecture for possible scaling problems.\nWhich component is MOST likely to need re-architecting to be able to scale to accommodate the new\ntraffic?	Lambda function	SQS queue	EC2 instance	DynamoDB table	\N	OPTION_C
\.


--
-- Name: ec2_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ec2_id_seq', 6, true);


--
-- Name: ec2 ec2_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ec2
    ADD CONSTRAINT ec2_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

