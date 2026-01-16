- Para este proyecto he decidido hacer una página web de alquiler de rings de boxeo. Elegi esta tematica porque me gusta mucho el boxeo y creo que es una idea diferente, útil y fácil de llevar a un caso real: actualmente muchos gimnasios y clubes deportivos no tienen un sistema online para reservar espacios, y pensé que sería interesante cubrir esa necesidad con un servicio claro, directo y bien organizado. La mayoria de opciones que hay en valencia tienen unos precios muy elevados, por eso nuestro gimnasio permite alquilar rings por un muy buen precio para que todo el mundo pueda permitirselo. 




El objetivo de la web es permitir a un usuario:

1.  Ver los rings disponibles (profesional y de entrenamiento).
2.  Registrarse o iniciar sesión.
3.  Seleccionar un ring.
4.  Elegir una fecha en un calendario.
5.  Ver las horas disponibles para ese día.
6.  Escoger una hora y confirmar la reserva.
7.  Consultar sus reservas en una sección personal.

La necesidad que resuelve es sencilla pero real: gestionar espacios deportivos sin depender de llamadas, mensajes o papeleo, algo que en muchos gimnasios todavía se hace a mano. Con esta web, cualquier gimnasio podría tener un sistema online básico que simplifica la vida al usuario y al dueño del local.



- Este proyecto lo he hecho yo solo, sin pareja. La verdad es que era algo que me asustaba porque no me veia capaz de hacerlo todo yo solo, pero creo que, aunque mi web no sea la mejor, he hecho algo bien y desde mi parte he quedado satisfecho con mi trabajo. 




- Para mi proyeco he utilizado las siguientes tecnologias: 



- HTML

Usado para crear la estructura de las páginas: formularios, tablas, navegación, tarjetas…  
Decidi usar HTML porque es el estándar para construir interfaces web y permite trabajar cómodamente con Jinja.



- CSS

Se ha usado para darle estilo a la web.  
Use variables de color, grid para organizar los rings, flexbox en la barra de navegación, sombras, efectos hover y un estilo limpio que hace que la web parezca profesional.



- Python con Flask

Flask me permitió crear una web dinámica sin complicarme con frameworks más pesados. Es facil de entender, permite organizar bien las rutas y se lleva genial con Jinja.



- MySQL

Elegi MySQL porque permite almacenar:

*   Usuarios
*   Rings
*   Reservas

Es una base de datos robusta, fácil de consultar y perfecta para este tipo de proyectos.



- Jinja

Jinja ha sido clave para mostrar datos en las plantillas:

*   mostrar rings desde la BD
*   listar reservas
*   mostrar horas disponibles
*   cambiar el menú según si el usuario está logueado





- A contunuacion, explico las diferentes partes de la web:



- Pantalla de inicio

El usuario entra y ve los dos rings disponibles, con su imagen, nombre, descripción y precio por hora.  
También tiene arriba las opciones de Login y Registro, o, si ya está dentro, Mis reservas y Salir.



- Pantalla de registro

Formulario simple para crear una cuenta: nombre, email y contraseña.  
Es fácil, directo y lo que cualquier usuario esperaría.



- Pantalla de login

Formulario para iniciar sesión.  
Si el login es correcto, la web lo identifica con su nombre en el menú.




- Pantalla de reserva

El usuario elige un ring, accede al calendario, selecciona un día, ve qué horas están libres y cuáles ocupadas.  
Las horas libres aparecen como botones normales; las ocupadas se ven desactivadas.




- Confirmación

El usuario selecciona la hora y la reserva queda guardada en MySQL.




- Mis Reservas

Aquí aparece una tabla con todas las reservas del usuario en orden cronológico.  
Es una parte importante porque le da al usuario sensación de control sobre su historial.





- A contunacion explico como se unen todas las tecnologias que he utilizado:

Este proyecto me ha ayudado a entender que una web real no es solo HTML o solo Python.  

*   HTML → estructura
*   CSS → diseño
*   Python (Flask) → lógica y rutas
*   MySQL → almacenamiento
*   Jinja → conexión entre backend y frontend

Sin uno de ellos, el proyecto no funcionaría.  
Gracias a lo aprendido este curso he podido ver cómo encajan y cómo se pasa de saber “etiquetas HTML” a saber construir una aplicación completa con registro, login y reservas.





Este proyecto me ha servido para unir todo lo aprendido hasta ahora de una manera práctica. Elegí el tema porque me gusta el mundo del boxeo y porque pensé que era una buena oportunidad para crear algo diferente y útil. Me ha permitido entender mejor cómo se relacionan los lenguajes de marcas con el backend y las bases de datos, y cómo todo junto puede solucionar una necesidad concreta: reservar un espacio deportivo de forma simple.

Aunque el proyecto es sencillo, creo que funciona bien y refleja todo el aprendizaje de este curso. Si en el futuro quisiera ampliarlo, podría añadir roles de administrador, más rings, pagos online o un sistema de notificaciones. Pero por ahora cumple exactamente lo que buscaba: una web funcional, clara y completa.

