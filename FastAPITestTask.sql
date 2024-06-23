--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11 (Homebrew)
-- Dumped by pg_dump version 14.11 (Homebrew)

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

--
-- Name: category; Type: TYPE; Schema: public; Owner: danosmac
--

CREATE TYPE public.category AS ENUM (
    'Стройматериалы',
    'Хозтовары',
    'Электроника'
);


ALTER TYPE public.category OWNER TO danosmac;

--
-- Name: check_unsigned_amount(); Type: FUNCTION; Schema: public; Owner: danosmac
--

CREATE FUNCTION public.check_unsigned_amount() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
   IF NEW.amount < 0 THEN
   RAISE EXCEPTION 'Amount cant be less then zero!';
   END IF;
   RETURN NEW;
END;
$$;


ALTER FUNCTION public.check_unsigned_amount() OWNER TO danosmac;

--
-- Name: delete_zero_products_amount(); Type: FUNCTION; Schema: public; Owner: danosmac
--

CREATE FUNCTION public.delete_zero_products_amount() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    DELETE FROM api_products as ap where (ap.amount = 0);
    RETURN NULL;
END;
$$;


ALTER FUNCTION public.delete_zero_products_amount() OWNER TO danosmac;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: danosmac
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_id_seq OWNER TO danosmac;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: api_products; Type: TABLE; Schema: public; Owner: danosmac
--

CREATE TABLE public.api_products (
    id integer DEFAULT nextval('public.products_id_seq'::regclass) NOT NULL,
    name character varying(255) NOT NULL,
    category public.category NOT NULL,
    info character varying(255),
    amount integer DEFAULT 0
);


ALTER TABLE public.api_products OWNER TO danosmac;

--
-- Data for Name: api_products; Type: TABLE DATA; Schema: public; Owner: danosmac
--

INSERT INTO public.api_products (id, name, category, info, amount) VALUES (3, 'Кирпичи', 'Стройматериалы', 'Большие и красивые', 10);
INSERT INTO public.api_products (id, name, category, info, amount) VALUES (5, 'Гвозди', 'Стройматериалы', 'Острые', 1);
INSERT INTO public.api_products (id, name, category, info, amount) VALUES (8, 'Мониторы', 'Электроника', 'Большие', 10);
INSERT INTO public.api_products (id, name, category, info, amount) VALUES (9, 'Мониторы', 'Электроника', 'Большие', 10);
INSERT INTO public.api_products (id, name, category, info, amount) VALUES (10, 'Мониторы', 'Электроника', 'Большие', 10);
INSERT INTO public.api_products (id, name, category, info, amount) VALUES (11, 'Мониторы', 'Электроника', 'Большие', 10);
INSERT INTO public.api_products (id, name, category, info, amount) VALUES (12, 'Шампунь', 'Хозтовары', NULL, 9);
INSERT INTO public.api_products (id, name, category, info, amount) VALUES (6, 'string', 'Стройматериалы', 'string', 1);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: danosmac
--

SELECT pg_catalog.setval('public.products_id_seq', 13, true);


--
-- Name: api_products api_products_pk; Type: CONSTRAINT; Schema: public; Owner: danosmac
--

ALTER TABLE ONLY public.api_products
    ADD CONSTRAINT api_products_pk PRIMARY KEY (id);


--
-- Name: api_products check_unsigned_amount; Type: TRIGGER; Schema: public; Owner: danosmac
--

CREATE TRIGGER check_unsigned_amount BEFORE INSERT OR UPDATE ON public.api_products FOR EACH ROW EXECUTE FUNCTION public.check_unsigned_amount();


--
-- Name: api_products delete_zero_products_amount; Type: TRIGGER; Schema: public; Owner: danosmac
--

CREATE TRIGGER delete_zero_products_amount AFTER INSERT OR UPDATE ON public.api_products FOR EACH ROW EXECUTE FUNCTION public.delete_zero_products_amount();


--
-- PostgreSQL database dump complete
--

