create database playMusica;

use playmusica;

create table musica(
	id_musica int primary key auto_increment not null,
    nome_musica varchar(50) not null,
    cantor_banda varchar(50) not null,
    genero_musica varchar(20) not null);
    
select * from musica;

select nome_musica, genero_musica from musica;

insert into musica(nome_musica, cantor_banda, genero_musica)
values('Todavia me alegrarei', 'Samuel Messias', 'Gospel');

select * from musica;

select nome_musica, genero_musica from musica;

insert into musica(nome_musica, cantor_banda, genero_musica)
values('O sol', 'Vitor Kley', 'Pop');

insert into musica(nome_musica, cantor_banda, genero_musica)
values('Cavalo de Troia', 'Mc Kelvin', 'Funk'),
('Isis', 'Mc Kako', 'Funk'),
('Pai é quem cria', 'Tierry', 'Sertanejjo'),
('Lobo Guará', 'Hungria', 'Rep'),
('Meu abrigo', 'Mellin', 'Popp');

use playmusica;

select * from musica where cantor_banda = 'Vitor Kley';

select * from musica;

select * from musica where cantor_banda like '%e%';

select * from musica where nome_musica like '%a%';

select * from musica where genero_musica <> 'Popp';

select * from musica where id_musica <= 5;

select * from musica where id_musica >= 4;

update musica set genero_musica = 'Sertanejo' where id_musica = 5;

select * from musica where id_musica = 7;

select * from musica;

update musica set cantor_banda = 'Melim', genero_musica = 'Pop' 
where id_musica = 7;

update musica set genero_musica = 'Rap' where id_musica = 6;

delete from musica where id_musica = 3;

select * from musica;

/* 
	Abaixo ficam os comandos da tabela de usuarios
*/
 -- comentario de uma linha
 
create table usuario(
	id_usuario int primary key auto_increment not null,
    nome_usuario varchar(50) not null,
    login_usuario varchar(20) not null,
    senha_usuario varchar(15) not null);

select * from usuario;


insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Daniel Xavier', 'daniel.xds93', 'admin');


insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Vilma Nunes', 'vilmanunes104', 'nunes');

select * from usuario;

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Daniel Oliveira', 'daniel.xds93', 'oliveira');


truncate table usuario;

alter table usuario
add unique(login_usuario);

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Daniel Xavier', 'daniel.xds93', 'admin'),
('Vilma Nunes', 'vilmanunes104', 'nunes');

select * from usuario;

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Daniel Oliveira', 'daniel.xds94', 'oliveira');

delete from musica where id_usuario > '10';


use playmusica;

select * from usuario;


alter table usuario
modify senha_usuario varchar(255) not null;



















