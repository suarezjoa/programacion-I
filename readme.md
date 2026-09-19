# GitHub — Guía básica

Repositorio de la materia **Programación I** (UCP). Este documento explica qué es
GitHub, cómo funciona y cuáles son los comandos que vamos a usar en el día a día.

---

## 1. ¿Qué es Git y qué es GitHub?

Son dos cosas distintas y conviene no mezclarlas:

| | Git | GitHub |
|---|---|---|
| Qué es | Un programa que se instala en la computadora | Un sitio web |
| Para qué sirve | Llevar el historial de cambios de un proyecto | Guardar ese historial en internet y compartirlo |
| Necesita internet | No | Sí |

**Git** es un *sistema de control de versiones*: guarda "fotos" del proyecto a lo
largo del tiempo, permite volver atrás si algo se rompe y ver quién cambió qué.

**GitHub** es una plataforma donde se suben esos proyectos para tener una copia
en la nube, trabajar en equipo y mostrar el código.

Analogía: Git es el historial de versiones de un documento; GitHub es el Drive
donde lo guardás y lo compartís.

---

## 2. Conceptos principales

- **Repositorio (repo):** la carpeta del proyecto junto con todo su historial.
  Puede ser *local* (en tu compu) o *remoto* (en GitHub).
- **Commit:** una foto del proyecto en un momento dado, con un mensaje que
  describe qué se cambió. Es la unidad básica del historial.
- **Branch (rama):** una línea de trabajo paralela. Permite probar cosas sin
  tocar el código principal. La rama principal suele llamarse `main`.
- **Merge:** unir los cambios de una rama dentro de otra.
- **Remote:** la dirección del repositorio en GitHub. Por convención se llama
  `origin`.
- **Clone:** descargar por primera vez un repositorio de GitHub a la compu.
- **Push:** subir los commits locales a GitHub.
- **Pull:** bajar a la compu los commits que están en GitHub.
- **Pull Request (PR):** pedido para incorporar los cambios de una rama a otra.
  Es donde se revisa y comenta el código antes de unirlo.

---

## 3. Los tres estados de un archivo

Antes de que un cambio quede guardado en el historial pasa por tres lugares:

```
  Working Directory  →  Staging Area  →  Repository
   (tus archivos)        git add          git commit
```

1. **Working directory:** editás el archivo.
2. **Staging area:** con `git add` elegís qué cambios entran en el próximo commit.
3. **Repository:** con `git commit` el cambio queda registrado en el historial.

Después, `git push` lleva esos commits a GitHub.

---

## 4. Configuración inicial (una sola vez)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

Ese nombre y ese mail son los que van a aparecer en cada commit.

---

## 5. Flujo de trabajo típico

### Empezar desde un repo que ya existe en GitHub

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
```

### Empezar desde una carpeta local

```bash
git init                      # crea el repositorio local
git remote add origin URL     # lo conecta con GitHub
```

### Ciclo de todos los días

```bash
git status                    # ver qué cambió
git add archivo.py            # preparar un archivo (git add . para todos)
git commit -m "Mensaje claro" # guardar el cambio en el historial
git push origin main          # subirlo a GitHub
```

### Antes de empezar a trabajar

```bash
git pull origin main          # traer lo último de GitHub
```

Conviene hacerlo siempre al principio: evita conflictos con lo que subieron otros.

---

## 6. Trabajar con ramas

```bash
git branch                    # listar ramas
git checkout -b nueva-rama    # crear una rama y moverse a ella
git checkout main             # volver a main
git merge nueva-rama          # traer los cambios de nueva-rama a la rama actual
git push origin nueva-rama    # subir la rama a GitHub
```

Regla práctica: cada tema o ejercicio nuevo, en su propia rama. `main` queda
siempre con código que funciona.

---

## 7. Comandos útiles para revisar

```bash
git log --oneline             # historial resumido
git diff                      # ver los cambios sin preparar
git show HEAD                 # ver el último commit en detalle
git remote -v                 # ver a qué repo de GitHub está conectado
```

---

## 8. Cómo escribir un buen mensaje de commit

- En modo imperativo y en presente: `Agrega función de suma`, no `Agregué...`.
- Corto y descriptivo: qué se cambió, no cómo.
- Un commit por idea. Si el mensaje necesita un "y", probablemente sean dos commits.

Ejemplos:

```
✅ Agrega validación de entrada en funcion.py
✅ Corrige error de división por cero
❌ cambios
❌ asdasd
```

---

## 9. El archivo .gitignore

Sirve para que Git ignore archivos que no deben subirse (temporales, claves,
entornos virtuales). Se crea un archivo llamado `.gitignore` en la raíz:

```
__pycache__/
*.pyc
.venv/
.env
```

---

## 10. Problemas frecuentes

**Me equivoqué en el último mensaje de commit**

```bash
git commit --amend -m "Mensaje corregido"
```

(Solo si todavía no hiciste push.)

**Agregué un archivo al staging por error**

```bash
git restore --staged archivo.py
```

**Quiero descartar los cambios de un archivo**

```bash
git restore archivo.py
```

**Conflicto al hacer merge o pull**

Git marca el conflicto dentro del archivo así:

```
<<<<<<< HEAD
tu versión
=======
la versión del otro
>>>>>>> otra-rama
```

Se edita el archivo dejando la versión correcta, se borran las marcas y después:

```bash
git add archivo.py
git commit
```

**El push fue rechazado**

Casi siempre es porque hay commits en GitHub que no tenés localmente. Se soluciona:

```bash
git pull origin main
git push origin main
```

---

## 11. Glosario rápido

| Comando | Qué hace |
|---|---|
| `git init` | Crea un repositorio local |
| `git clone` | Descarga un repositorio de GitHub |
| `git status` | Muestra el estado de los archivos |
| `git add` | Prepara cambios para el commit |
| `git commit` | Guarda los cambios en el historial |
| `git push` | Sube los commits a GitHub |
| `git pull` | Baja los commits desde GitHub |
| `git branch` | Lista o crea ramas |
| `git checkout` | Cambia de rama |
| `git merge` | Une ramas |
| `git log` | Muestra el historial |

---

## 12. Para seguir leyendo

- [Documentación oficial de Git](https://git-scm.com/doc)
- [GitHub Docs en español](https://docs.github.com/es)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=es_AR) — práctica interactiva
