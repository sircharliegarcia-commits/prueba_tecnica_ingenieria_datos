SELECT identificacion, corte_mes, saldo, 
CASE 
WHEN saldo >= 0 AND saldo < 300000 THEN 'N0' 
WHEN saldo < 1000000 THEN 'N1' 
WHEN saldo < 3000000 THEN 'N2' 
WHEN saldo < 5000000 THEN 'N3' 
ELSE 'N4' END AS nivel 
INTO historia_niveles FROM historia; 
