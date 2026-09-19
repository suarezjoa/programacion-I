El Club Deportivo Litoral organiza todos los años su torneo abierto de pádel, que convoca a decenas de jugadores de la ciudad y la región. Hasta ahora, la comisión organizadora lleva todo en planillas de papel y algún cuaderno: anotan las parejas inscriptas, arman los grupos a mano, escriben los resultados de cada partido en una pizarra y calculan las posiciones con una calculadora. El sistema funciona, pero es lento, se cometen errores al sumar puntos y, cuando alguien pregunta "¿cómo va mi grupo?", nadie tiene la información a mano al instante.

Este año el club decidió modernizarse y le encargó a un grupo de estudiantes de Ingeniería en Sistemas que desarrolle un programa en Python para gestionar el torneo de principio a fin.

Cómo funciona el torneo. El pádel se juega por parejas (dos jugadores por lado). Cada pareja se inscribe en una categoría según su nivel (por ejemplo, 4ª, 5ª y 6ª). Dentro de cada categoría, el torneo tiene dos etapas: primero una fase de grupos (o "zonas"), donde las parejas se dividen en zonas de tres o cuatro y todas juegan contra todas; y después una fase final (llave eliminatoria), a la que pasan las mejores parejas de cada zona.

## Objetivos de la semana
* Introducir la estructura de datos en memoria mediante arreglos unidimensionales
* Aplicar las operaciones básicas con vectores: inicialización, carga de datos por teclado y recorrido
* Implementar arreglos multidimensionales (matrices) para organizar datos tabulares

## Consignas a desarrollar

### 1. Módulo de Inscripción y Armado de Parejas

Para poder poner en marcha el torneo, lo primero que necesitamos del sistema es
poder **cargar a los jugadores** y luego **armar las parejas** que van a
competir. Recuerden que en el pádel se juega de a dos: ninguna pareja puede
tener más ni menos de **2 jugadores**.

**a) Ingreso de jugadores**

* Al iniciar el programa, el sistema debe preguntarle al juez:
  *"¿Cuántos jugadores van a participar en el torneo?"*.
* A partir de esa respuesta, debe permitir registrar cada competidor, uno por
  uno, con la siguiente información:
  * su **nombre** (con el que se lo identificará dentro del torneo), y
  * su **categoría** (el nivel en el que juega, por ejemplo 4ª, 5ª o 6ª).

**b) Armado de parejas**

* Una vez cargados todos los jugadores, el sistema debe permitir **formar las
  parejas** del torneo.
* Cada **pareja** debe tener:
  * un **nombre** que la identifique dentro del torneo (por ejemplo,
    *"Los Tanos"*), y
  * exactamente **2 jugadores**, elegidos entre los que ya fueron inscriptos.

