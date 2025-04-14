CREATE TABLE OPERADOR (
    id_operador NUMBER PRIMARY KEY,
    nome VARCHAR2(100),
    experiencia NUMBER,
    tipo_colheita VARCHAR2(20)
);

CREATE TABLE MAQUINA (
    id_maquina NUMBER PRIMARY KEY,
    modelo VARCHAR2(50),
    fabricante VARCHAR2(50),
    ano NUMBER
);

CREATE TABLE COLHEITA (
    id_colheita NUMBER PRIMARY KEY,
    id_operador NUMBER REFERENCES OPERADOR(id_operador),
    id_maquina NUMBER REFERENCES MAQUINA(id_maquina),
    data_colheita DATE,
    area_colhida FLOAT,
    tipo_colheita VARCHAR2(20),
    quantidade_colhida FLOAT,
    perda_estimada FLOAT
);
