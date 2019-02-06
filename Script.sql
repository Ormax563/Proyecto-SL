
CREATE TABLE tipo (
                id_tipo INT NOT NULL,
                detalle VARCHAR(20) NOT NULL,
                PRIMARY KEY (id_tipo)
);


CREATE TABLE registro (
                id INT NOT NULL,
                lab INT NOT NULL,
                maq INT NOT NULL,
                fecha VARCHAR(10) NOT NULL,
                hora VARCHAR(10) NOT NULL,
                estudiante VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL,
                descripcion VARCHAR(500) NOT NULL,
                id_tipo INT NOT NULL,
                PRIMARY KEY (id)
);


ALTER TABLE registro ADD CONSTRAINT tipo_registro_fk
FOREIGN KEY (id_tipo)
REFERENCES tipo (id_tipo)
ON DELETE NO ACTION
ON UPDATE NO ACTION;