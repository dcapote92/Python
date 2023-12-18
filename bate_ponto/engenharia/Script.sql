CREATE DATABASE `bateponto` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
CREATE TABLE Usuario (
	id INTEGER NOT NULL AUTO_INCREMENT,
	nome VARCHAR(15),
	sobrenome VARCHAR(30),
	cpf VARCHAR(11) UNIQUE,
	usuario VARCHAR(15) UNIQUE,
	senha VARCHAR(15) ,
	PRIMARY KEY (id)
);
CREATE TABLE Batidas (
	id_u INTEGER NOT NULL,
	dia DATE NOT NULL,
	entrada TIME(5),
	almoco TIME(5),
	volta TIME(5),
	saida TIME(5),
	inter_dia BIT,
	intra_dia BIT,
	ultrapassagem BIT,
	Foreign KEY (id_u) references Usuario(id)
);

INSERT INTO bateponto.Usuario (id, nome, sobrenome, cpf, usuario, senha) Values(1, 'Administrador', 'Geral', '00000000001','admin', 'admin@506' );
