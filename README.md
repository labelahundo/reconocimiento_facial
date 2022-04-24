RECONOCIMIENTO FACIAL

En este documento estan las instrucciones a detalle de la ejecucion e instalacion
de librerias necesarias para el buen funcionameinto, a si  se aclaran algunos errores
y dudas que podrian surgircualquier duda pueden contactarme por mi correo:

juannavarrete3@hotmail.com 

con la descripcion de "dudas vision artificial"

ANTES DE EMPEZAR CON EL RECONOCIMIENTO DEBE INSTALAR TOSDAS LAS LIBRERIAS Y
DEPENDENCIAS NECESARIAS PARA ESO PRESIONE "WINDOWS + R" Y ESCRIBA "cmd"
EN ESE MOMENTO APARECERA UNA VENTANA DE ESCRITURA VACIA,
LO QUE DEBE HACER ES COPIAR Y PEGAR LOS SIGUENTES PARRAFOS DANDO A ENTER
DESPUES DE PEGAR CADA UNO DE ELLOS:

pip install opencv-python  
pip install mutils  
pip install os-sys  
		***ES NORMAL QUE SALTE UN ERROR AL INSTALAR "os-sys"***  
pip install numpy  
pip install opencv-contrib-python  

Adicionalmente necesitaras decargar un achivo .xml de
opencv, lo encontraras dentro de su repositorio en 
github [link DEL REPOSITORIO](https://github.com/opencv/opencv/tree/master/data/haarcascades)
deberas buscar en la lista el archivo con el nombre "haarcascade_frontalface_defaul.xml"
descargarlo y ponerlo dentro de la carpeta de el proyecto "pr1"

*********************************

El primer paso a ejecutar es abrir el archivo llamado "captura_rostros"
al ejecutar el programa le pedira 2 parametros.

1 -- Sera el nombre de la perzona de la cual tomara las
imagenes para el entreanamiento.

2 -- Sera el numero de la primer imagen. Si la carpeta con el nombre de
la persona esta vacia el numero de la imagen debera ser 0, si necesita
tomar mas imagenes para reforzar el entrenamiento debera poner 
el numero de la ultima imagen de la carpeta y sumarle 1, mas adelante
tomaremos de nuevo este punto.

********************************

Al colocar ambos parametros dentro asegurese de que no haya nadie mas
dentro del rango de la camara de lo contrario podrian salir imagenes
de su rostro dentro de tu carpeta de imagenes, si desea reconocer a 
otra persona ademas de usted, puede hacerlo.

Para capturar de forma correcta su rostro debe mirar a la camara y
despues de eso mover lentamente su cara volteando a diferentes lugares 
asi habra variedad de pocisiones para el reconocimiento facial, ademas
le sujiero hacer algunas expreciones faciales como sonrreir o
sorprenderse, recuerde que mientras mas imagenes tenga mas robusto
sera el reconocimiento, asi sera tambien si tiene imagenes en diferentes
lugares y con diferentes iluminaciones.

La forma de reconocer a mas de una persona es repetir desde el principio
los pasos, pero al momento de poner el nombre, ponga el de la otra persona
y ponga el numero 0 si su carpeta esta vacia.

Ademas de asegurarse de que no haya mas de una persona en la pantalla
al momento de capturar las imagenes de su rostro debe saber que 
algunos peluches, fotos, imagenes de anime podrian ser reconocidos
como rostros y podrian aparecer capturas de ese tipo de objetos.

***para detener la captura de fotos de click al recuadro y presione "q"***

Para este momento se habra creado una carpeta en el escritorio con el nombre
deimagen, sera la carpeta que contenga las carpetas de las diferentes personas
y sus rostros.

Si su carpeta se contamina revise manualmente las imagenes y
elimine las imagenes inutites.



PODRIA REVISAR LA CAPTURA DE PANTALLA ADJUNTA EN LA CARPETA "pr1"
**********************************

Para el segundo paso daremos inicio al entrenamiento de la red neuronal,
lo unico que necesita es ejecutar el archivo "entrenamiento_rostros",
cuando se abra comenzara a ver las imagenes pasando en blanco y negro.

Cuando termine de cargar las fotos comenzara el entrenamiento, el tiempo
que tarde en entrenar varia dependiendo de la cantidad de imagenes y
la potencoia de su computador, no se preocupe ya que tomara tiempo.

Al finalizar el entrenamiento devera aparecer un nuevo archivo en la carpeta
"pr1" llamado "cara.xml", ese archivo podria decirse que es su modelo entrenado de reconocimiento facial.

************************************
Ahora estamos en la ultima fase.

Para terminar lo que debe hacer es ejecutar el archivo "reconocimiento_facial 1.1"
al principio no sera perfecto debe dejar que la camara ajuste la iluminacion.

Recuerde que si quiere salir de el programa debe dar click en el recuadro y
presionar la letra "q".


Si el programa no lo reconoce o tiene falsos positivos dentro de la captura
lo que puede hacer es mover un poco los parametros de reconocimiento que estan dentro

******************************************************
EN ESPECIFICO ESTA PARTE ::


clasificador = detect.detectMultiScale(gris,  
		scaleFactor = 1.1,  
		minNeighbors = 5,   
		minSize = (95,95),  
		maxSize = (400,400))  

DENTRO DE LOS PARENTESIS HAY 5 PARAMETROS:


1 - gris  
2 - scaleFactor  
3 - minNeighbors  
4 - minSize  
5 - maxSize  

Cada factor afecta el resultado final:

gris: 
Es la imagen cargada al reconocedor en este parametro no es recomendable cambiar nada ya que 
el entrenamiento de la red neuronal se dio con imagenes en blanco y negro,
por lo que al transformar la imagen de entrada a escala de grises otorga mayor
fiabilidad al reconocimiento facial.

scaleFactor:
La imagen de entrada es comprimida y presentada al reconocedor, se hace para 
no sobrecargar el cumputador con mucha informacion pero al hacerlo se puede
perder algo de calidad de deteccion la forma de usar es la siguiente:


		1.1 signicfica que no hay reduccion de tamaño 
		1.2 significa que es una escala de 1 a 2 por lo que ahora la imagen
			de entrada mide la mitad
		1.3 ahora la imagen mide 1/4 de la origonal
		1.4 esta escala es muy pequeña en camaras de laptop ya que no tienen
			muy buena calidad pero si conecta una camara externa es recomendable
			ya que la calidad de la imagen es de 1/8


minNeigbors:
Es la cantidad minima de detecciones para considerar un recuadro como cara.
Si baja mucho el numero habra falsos positivos y si aumenta el numero es probable
que no pueda reconocer su rostro.
Intente encontrar un punto donde lo reconozca y no haya tanbtos falsos positivos.


maxSize y minSize: 
Se encargan de que la captura de un rostro tenga un minimo y un maximo
de pixeles si tiene pequeñas detecciones como falsos positivos dentro de la imagen
puede aumentar el njumero de minSize de (95,95) a (100,100), y si eso no funciona
trate de aumentarlo un poco mas, si deja de detectar su rostro o la deteccion 
comienza a parpadear baje el numero.

No se preocupe si baja el numero para que pueda reconocer su rostro y al mismo tiempo 
tiene falsos positivos, puede modificar todos estos para metros para solucionar ese problema
puede verlos como perillas en un mezclador de sonido, solo mueva todas un poco hasta que
tenga el resut+ltado deseado con prueva y error

Un ultimo es si despues de cambiar los parametros no funciona podria usar de nuevo el archivo de
captura_rostros para tomar mas imagenes de su rostro, preferiblemente en el lugar en donde este
probando el modelo entrenado, lo unico que debe hacer es en lugar de poner el numero 0 en el
numero de imagen que le pide debera poner el numero de la ultima imagen y sumarle uno.
Por ejemplo si tinene 500 imagenes de su rostro en la carpeta, dentro del parametro debera poner
el numero 501 y siepre debe poner el mismo nombre de la carpeta que se desea llenar con nuevas imagenes
para reforzar el entrenamiento. 
