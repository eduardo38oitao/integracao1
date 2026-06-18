#senha: escola
create database cadastro1;
use cadastro1;

create table cliente1(
CPF VARCHAR(11) NOT NULL PRIMARY KEY,
PRIMEIRO_NOME VARCHAR(50) NOT NULL,
SOBRENOME VARCHAR(50) NOT NULL,
IDADE INT NOT NULL
);

SELECT * FROM cliente1;