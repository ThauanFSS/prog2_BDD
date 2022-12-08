create table colaboradores(
id int,
nome varchar(100),
endereco varchar(100),
sexo char(1),
data_nasci datetime,
salario real,
departamentos_num_dep int,
primary key(id),
foreign key(departamentos_num_dep) references departamentos(num_dep)
);
create table horastrabalho(
id_hora int,
horas_trabalhada datetime,
primary key(id_hora)
);
create table projetos(
num_proj int,
nome varchar(100),
periodo_des datetime,
horastrabalhada_id int,
primary key(num_proj),
departamentos_nu_dep int,
foreign key(horastrabalhada_id) references horastrabalho(id_hora),
foreign key(departamentos_nu_dep) references departamentos(num_dep)
);
create table pesquisador(
id int,
area_atuacao varchar(100),
colaboradores_id int,
projetos_num_proj_id int,
primary key(id),
foreign key(colaboradores_id) references colaboradores(id),
foreign key(projetos_num_proj_id) references projetos(num_proj)
);
create table secretario(
id int,
grau_escolaridade varchar(100),
colaboradores_id int,
primary key(id),
foreign key(colaboradores_id) references colaboradores(id)
);
create table supervisor(
id_sup int,
colaboradores_id int,
primary key(id_sup),
foreign key (colaboradores_id) references colaboradores(id)
);
create table limpeza(
id int,
cargo varchar(100),
jornada_trab datetime,
supervisor_id int,
colaboradores_id int,
primary key(id),
foreign key(colaboradores_id) references colaboradores(id),
foreign key(supervisor_id) references supervisor(id_sup)
);
create table departamentos(
num_dep int,
nome varchar(100),
primary key(num_dep)
);
create table dependentes(
id int,
nome varchar(100),
sexo char(1),
dt_nasc date,
grau_parentesco varchar(100),
colaboradores_id int,
primary key(id),
foreign key(colaboradores_id) references colaboradores(id)
);
