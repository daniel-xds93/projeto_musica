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










