# Scorched-Earth
tl;dr: A python script that allows deleting all your tweets without the API limit.
Sorry English speakers! We are working on a English version of this tutorial. For now, the tutorial is just in Spanish.

*__SPA__*

Hay múltiples motivos por los que uno no querría borrar su cuenta para poder deshacerse de sus tweets antiguos. Sin embargo, Twitter hace prácticamente imposible eliminar más allá de la barrera que ha impuesto con el API de los 3200 tweets. Hay algunas aplicaciones en Google que sirven para esto, pero todas tienen el problema de que están capadas para que el usuario pague una tarifa por administrar sus propios tweets. Así pues, hace un par de años empezaron a aparecer códigos para scripts de Python que permitían borrar tus propios tweets con acceso al API mediante el Developer Portal de Twitter y tu propio archivo. La mayoría de ellos son actualmente inservibles porque recientemente Twitter ha migrado de la versión 1.1 de su API a la v2, modificando variables, endpoints y limitando, asimismo, el acceso que tienen los usuarios a la API, creando en su Developer portal categorías de usuarios como ‘Essencial, Advanced o Academic’. 

Nosotros creemos que debería ser un derecho de cada usuario poder administrar su imagen pública en las redes social de manera gratuita, y más cuando las mismas se pueden emplear para identificar a sujetos revolucionarios o agitativos. Precisamente por eso hemos creado, basándonos en el código de [Alberta Odamea Anim-Ayeko](https://towardsdatascience.com/python-tweet-deleter-3b1154830f3a/), esta herramienta de autodefensa antifascista gratuita tratando de saltar las limitaciones de Twitter y jugando con ellas en contra. Hasta la victoria siempre, camaradas.

### ¿QUÉ NECESITO PARA BORRAR MIS TWEETS?
**Tu archivo de Twitter**: Para ver cómo se descarga, leer [esto](https://help.twitter.com/es/managing-your-account/how-to-download-your-twitter-archive/). Puede tardar unos días, así que paciencia.

**Tener una cuenta en el Developer Portal de Twitter y un proyecto**: Primero deberás acceder [aquí](https://developer.twitter.com/en/). Una vez ahí, hay que registrarse con la cuenta en la que deseas borrar los tweets (esto es importante, porque si quieres borrar otras cuentas tendrías que emplear otros permisos y código). Al registrarnos nos va a preguntar qué uso queremos darle a la cuenta. Recomendamos simplemente seleccionar ‘Exploring the API’ y por supuesto que no vamos a hacer contenido derivado para ningún gobierno.
![1](https://user-images.githubusercontent.com/112905248/188513229-995574a1-000f-4640-afde-a94d4c309953.png)
Twitter da automáticamente a todos los usuarios acceso a la versión Essential, que es más que suficiente para lo que queremos usarlo nosotros. Para poder seguir, debemos crear un proyecto. 

![2](https://user-images.githubusercontent.com/112905248/188513360-cb631d4f-36f8-4a3c-9e77-3d1d127c2320.png)

Ahí creáis un proyecto y dentro del mismo una app. La app podéis llamarla como queráis, y os solicita también una breve descripción. Nosotros simplemente le hemos llamado como a nuestro código y hemos dicho que es una app para explorar el API de Twitter. Una vez hecho eso, tendremos algo así:

![3](https://user-images.githubusercontent.com/112905248/188513393-d7caecc2-2866-4d77-99b4-805204504e04.png)

 Se nos generarán unos códigos de la app. Esos códigos es lo que estamos buscando. A estos códigos Twitter les llama Keys and Tokens, y son las claves de autentificación que nos permiten ejecutar el código.
 
 ![3 5](https://user-images.githubusercontent.com/112905248/188513751-cdac3d2a-0915-4bb9-9bd7-10f19b291ad2.png)
 
![4](https://user-images.githubusercontent.com/112905248/188513757-d8e897fa-dc5b-4f1e-806f-40c8d2c6cf0c.png)
 
Los códigos que se nos generan en un primer momento nos otorgan únicamente permisos de ‘Read only’. Es importante cambiemos esos permisos a ‘Read and Write’, regeneremos los códigos y los copiemos en una hoja de texto. Si no tenemos permisos ‘Read and Write’ el programa nos dirá que estamos Unauthorized para borrar los tweets.


**Tener descargado Python**: [Aquí](https://www.python.org/downloads/)

### ¿CÓMO BORRO LOS TWEETS Y USO EL CÓDIGO?

1. Primero, debes crear una carpeta en tu escritorio (o donde quieras) en la que vas a copiar el archivo ‘tweet.js’ que vas a encontrar en la carpeta ‘data’ del archivo de Twitter.

2. En la barra de búsqueda de Windows, buscar ‘cmd’ y hacer clic en la aplicación ‘Símbolo de sistema’.

3. En el terminal (la ventana negra de Windows) teclear ‘cd’ y la ubicación de la carpeta (nosotros a nuestra carpeta le hemos llamado tweet delete), y dar a enter.

![5](https://user-images.githubusercontent.com/112905248/188513822-91fa610d-bea8-45ad-ba36-67cb3b6bc3fb.png)

 4. En el terminal escribir ‘python -m venv tweetdeleter’ y dar a enter.
 
5. En el terminal escribir ‘tweetdeleter\Scripts\activate.bat’ y dar a enter.

6. Escribir en el terminal ‘pip install tweepy’ y dar enter. Hacer lo mismo con ‘pip install datetime’. En este punto, la carpeta que hemos creado en el escritorio debería tener la siguiente pinta:
 
 ![6](https://user-images.githubusercontent.com/112905248/188513912-b78fcfcb-3be1-439a-a184-15c437b13ef4.png)

 
 Y dentro de tweetdeleter:
 

![7](https://user-images.githubusercontent.com/112905248/188513927-d12106bd-c503-40b4-98be-5ee5c7c512fc.png)

 
 Es en esta carpeta donde vamos a pegar el archivo ‘ScorchedEarth’ que os proporcionamos.
 
 
 ![8](https://user-images.githubusercontent.com/112905248/188513943-42c4e57e-8710-4f2f-8744-5cb9281d88cb.png)

 Con el botón derecho, abrir el archivo ‘ScorchedEath’ con seleccionando ‘Edit with IDLE’, que es el editor IDLE 3.10 que viene incorporado con Python y permite modificar las líneas de código guardadas en el archivo. Se nos abrirá el código siguiente:
 
 
 ![10](https://user-images.githubusercontent.com/112905248/188514049-09ec5bf3-2c45-4c29-9e18-e72e4afe0e10.png)

 En el mismo debemos editar 3 partes. La primera es poner en consumer key, consumer secret, access token y access token secret los códigos que obtuvimos al crear la aplicación en el Developer Portal.
 
En segundo lugar, se debe editar en el Block 4 el número que aparece detrás de (days = NÚMERO). Este bloque de código se emplea para poder seleccionar un rango de fechas entre los que eliminar los tweets. Para ello, el código resta a la fecha actual que hay en nuestro ordenador el número de días que aparece en el paréntesis, por lo que para este código, las fechas que nos aparecerán en el terminal serán, teniendo en cuenta que hoy es 5/09/2022: 

end_date =  2017-03-15 19:35:19.417414+00:00

start_date =  2016-03-15 19:35:19.418452+00:00

Esto es importante por algunas consideraciones que comentaremos más adelante.

Por último, la tercera cosa que debéis editar es, en el Block 5, la ubicación de la carpeta en donde tenéis el archivo tweet.js. 

Una vez editado el archivo, lo guardamos. Volvemos a la pantalla del terminal y tecleamos ‘cd’ y tweetdeleter y le damos a enter.

 ![11](https://user-images.githubusercontent.com/112905248/188514090-3f738b2d-4373-4301-a5be-aef5e7defbd9.png)

Una vez hecho eso, tecleamos ‘python ScorchedEarth.py’ y el programa se ejecutará.

![12](https://user-images.githubusercontent.com/112905248/188514097-2623899c-743b-417c-a37e-cf57fb5caf62.png)

 
### VARIAS CONSIDERACIONES

Twitter limita a todos los usuarios, da igual el tipo de credenciales que tengan, impidiendo que borren más de 50 tweets por cada 15 minutos. Este programa tiene en cuenta esto, por lo que borra 50 tweets, se queda esperando 15 minutos y sigue ejecutando mientras no se cierre el terminal, ni el ordenador. Es importante tener esto en cuenta si se quieren borrar muchos tweets, porque eso implica que hay que tener el ordenador mucho tiempo encendido y con el terminal ejecutando. No es un programa que consuma memoria, pero es cierto que es una tarea que gasta tiempo y energía, por lo que hemos decidido codificar el programa de manera que se le introduzca una fecha en la que se quiera iniciar el borrado de tweets y en la que se quiera terminar. De esa manera, podemos ir borrando los tweets de manera paulatina llevando un control de entre qué fechas estamos borrando sin necesidad de dejar el ordenador encendido días y, si se cierra el terminal o el propio ordenador, se pierda el avance y no se sepa cuánto se ha borrado.

El código no funciona bien si la start date es más cercana en el tiempo que la end date. Es decir, que en la end date siempre tiene que ser un número MENOR que la start date. De otro modo, os dirá que se han borrado 0 tweets.

Por otro lado, este programa no elimina likes, y no estamos seguros de si elimina retweets o no. Estamos probando poco a poco y sabemos que borra los tweets del archivo. En cualquier caso, este código es libre y cualquiera puede hacer las modificaciones que desee y colgarlas aquí. Nosotros nos basamos en el código de otra persona para actualizarlo y hacerlo que funcionase con la nueva API, así que esperamos que más personas mejoren nuestro código y le añadan la función de eliminar likes, siempre y cuando utilicen ese código de manera abierta, gratuita y para que favorezca la lucha obrera.

Por último, hemos decidido llamar a nuestro código Scorched Earth, o Tierra Quemada, en referencia a la táctica que empleó el Ejército Rojo contra los nazis en la Segunda Guerra Mundial.


