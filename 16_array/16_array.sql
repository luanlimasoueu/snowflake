use new_db.public;

CREATE OR REPLACE TABLE  mercado (
    consumidor STRING,
    produtos ARRAY,
    data_compra  DATE
);


select * from mercado

insert into mercado (consumidor, produtos, data_compra) 
SELECT 'Maria', ARRAY_CONSTRUCT('Feijao', 'Arroz') , '2025-02-08'


select * from mercado


INSERT INTO mercado (consumidor, produtos, data_compra) 
SELECT 
    'Carlos', 
    PARSE_JSON('["Arroz", "Feijão", "Macarrão"]')::ARRAY, 
    '2024-02-09';

select * from mercado

INSERT INTO mercado (consumidor, produtos, data_compra)     
SELECT $1 COL1, parse_json($2)::array COL2,$3 COL3
FROM (VALUES ( 'Jose', '["Açúcar", "Macarrão"]', '2024-11-13') );

select * from mercado


INSERT INTO mercado (consumidor, produtos, data_compra) 
SELECT 'Luiz', ARRAY_CONSTRUCT('Leite', 'Achocolatado') , '2025-05-08'
UNION ALL
SELECT 'Graça', ARRAY_CONSTRUCT() , '2025-07-08'


SELECT 
    consumidor, 
    produto.VALUE AS produto, 
    data_compra
FROM mercado
, 
LATERAL FLATTEN(input => produtos) AS produto;