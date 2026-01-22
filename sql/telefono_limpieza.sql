SELECT DISTINCT
    cliente_id,
    REGEXP_REPLACE(numero_telefono, '[^0-9]', '') AS telefono_limpieza
FROM cliente_raw
WHERE numero_telefono IS NOT NULL;