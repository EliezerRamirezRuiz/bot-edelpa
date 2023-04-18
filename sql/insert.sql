SET DATEFORMAT dmy;

INSERT INTO CANALES
	SELECT 'GENERAL', '1087804036624957622'


INSERT INTO CANALES
	SELECT 'CORTE', '1093594034863341629'


INSERT INTO ALERTS	(AlertName, AlertDescription, AlertActivo, Area)
	VALUES ('ROBOT', 'ERROR: ERROR EN EL BRAZO', 1, 1)


INSERT INTO ALERTS	(AlertName, AlertDescription, AlertActivo, Area)
	VALUES ('ROBOT', 'ERROR: ERROR EN MOSAICO', 1, 2)


INSERT INTO ALERTS (AlertName, AlertDescription, AlertActivo, Area)
	VALUES ('Alerta de prueba', 'Descripción de la alerta', 1, 10);