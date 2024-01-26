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







