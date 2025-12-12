# 🛒 ProductRadar – Automatización de scraping y exportación de productos de Amazon

**ProductRadar** es una herramienta diseñada para automatizar la monitorización de productos en Amazon.
Utiliza Django, Celery, Redis y Docker para ejecutar tareas de scraping de forma periódica, almacenar los resultados y
generar automáticamente un archivo CSV con todos los productos obtenidos.
El objetivo es ofrecer una base sólida para construir sistemas de análisis de precios,
alertas de bajadas, comparadores o dashboards de seguimiento.

![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Django](https://img.shields.io/badge/Django-Backend-green.svg)
[![Docker Compose Ready](https://img.shields.io/badge/docker--compose-ready-blue)](https://docs.docker.com/compose/)
[![Celery Workers](https://img.shields.io/badge/Celery-distributed-yellow)](https://docs.celeryq.dev/)
[![Redis](https://img.shields.io/badge/Redis-broker-red)](https://redis.io/)

---
# Índice

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Estructura](#estructura)
- [Instalación y uso](#instalación-y-uso)
- [Despliegue con Docker](#despliegue-con-docker)
- [Uso de Django Shell y Celery para ejecutar las tareas manualmente](#uso-de-django-shell-y-Celery-para-ejecutar-tareas-manualmente)
- [Objetivo del proyecto](#objetivo-del-proyecto)
- [Estado del proyecto](#estado-del-proyecto)
- [Licencia – Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](#licencia--creative-commons-attribution-noncommercial-40-international-cc-by-nc-40)
- [Contacto](#contacto)

---
---

# 🚀 Características

## 🛒 Scraping automático de Amazon
- Obtención de productos mediante SerpAPI (Amazon Engine).
- Soporte para múltiples keywords.
- Actualización automática sin duplicados.

## ⚙️ Tareas asíncronas con Celery
- Celery Worker ejecuta el scraping sin bloquear Django.
- Celery Beat programa tareas periódicas (por defecto, cada hora).
- Pipeline completo: scraping → guardado → exportación CSV.

## 📄 Exportación automática a CSV
- Genera un archivo con todos los productos.
- El archivo se guarda en un volumen Docker accesible desde el host.

## 🐳 Infraestructura en Docker
- Servicios incluidos:
  - Django (web)
  - Celery Worker
  - Celery Beat
  - Redis
- Volúmenes persistentes para datos y exportaciones.

## 🧱 Escalabilidad
- Arquitectura modular basada en Django.
- Fácil de extender con nuevas fuentes.
---
---
# 🛠️ Tecnologías

- **Django** – Backend principal.
- **Celery** – Ejecución de tareas asíncronas.
- **Redis** – Broker y backend de resultados.
- **Docker & Docker Compose** – Orquestación de servicios.
- **SerpAPI** – Motor de scraping para Amazon.
- **SQLite** – Base de datos ligera para desarrollo.
- **Python 3.x** – Lenguaje base del proyecto.

---

---
# 🏗️ Estructura
```

ProductRadar/
├── src/
│   ├── ProductRadar/          # Configuración principal de Django
│   ├── product/               # App principal: scraping, modelos, tareas
│   │   ├── tasks.py           # Tareas Celery (scraping + CSV)
│   │   ├── models.py          # Modelo Product
│   │   ├── signals.py         # Creación automática de tareas periódicas
│   │   └── ...
│   ├── db.sqlite3             # Base de datos (desarrollo)
│   └── manage.py
├── exports_local/             # Carpeta donde se genera el CSV
├── docker-compose.yml         # Orquestación de servicios
├── Dockerfile                 # Imagen de Django/Celery
```
---

# ⚡ Instalación y uso

1. Clonar el repositorio
```bash
  git clone https://github.com/JobabHIzquierTorres/ProductRadar.git
  cd ProductRadar
```

2. Crear archivo de entorno
```bash
  cp sample-.env .env
```
3. Editar clave de SerpAPI:
```python
  SERPAPI_API_KEY=tu_api_key
```
---
# 🐳 Despliegue con Docker

Levantar todos los servicios:
```bash
  docker compose up --build
```

## Servicios incluidos:
- ✅ Django
- ✅ Celery Worker
- ✅ Celery Beat
- ✅ Redis

Ver logs del worker:
```bash
  docker logs -f productradar_celery
```

Ver logs de Celery Beat:
```bash
  docker logs -f productradar_celery_beat
```

---
# 🐚 Uso de Django Shell y Celery para ejecutar tareas manualmente

✅ Entrar al contenedor web
```bash
  docker exec -it productradar_web bash
```

✅ Abrir Django Shell
```bash
  python manage.py shell
```

✅ Ejecutar scraping manual
```python
  from product.tasks import scrape_product_data
  scrape_product_data.delay()
```

✅ Ejecutar pipeline completo (scraping + CSV)
```python
  from product.tasks import scrape_and_export
  scrape_and_export.delay()
```

✅ Comprobar que la tarea se ejecuta
En otra terminal:
```bash
  docker logs -f productradar_celery
```

---
# 🧭 Objetivo del proyecto

ProductRadar busca automatizar la obtención de productos de Amazon para facilitar:
- análisis de precios
- seguimiento de tendencias
- detección de bajadas
- exportación de datos
- integración con dashboards o sistemas externos

Todo ello manteniendo una arquitectura escalable y fácil de extender.
---

# 🚧 Estado del Proyecto

Importante: Este proyecto se encuentra en fase de desarrollo y no está preparado para despliegue en producción.

Limitaciones actuales
- Configuración de seguridad básica.
- Falta de configuración para despliegue en servidores reales.
- Puede contener funcionalidades incompletas o en evolución.
  
Recomendaciones
- Usar únicamente en entornos de desarrollo o testing.
- No usar en producción sin una configuración avanzada de seguridad y despliegue.
---

# 📄 Licencia – Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

Este proyecto se encuentra bajo la licencia **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

### Permisos otorgados

Puedes:

- **Compartir**: copiar y redistribuir el material en cualquier medio o formato.
- **Adaptar**: remezclar, transformar y construir a partir del material.

### Restricciones

No puedes:

- Usar el material con fines comerciales.
- Aplicar restricciones legales o tecnológicas que impidan a otros hacer lo que permite esta licencia.

### Enlace oficial

Consulta los términos completos de la licencia en el sitio oficial de Creative Commons:  
[https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

### Garantía

Este software se proporciona **"tal cual"**, sin garantías de ningún tipo.  
El autor no se hace responsable de posibles daños derivados del uso del código.

### Contribuciones

Las contribuciones son bienvenidas siempre que respeten la licencia.  
Si deseas colaborar:

1. Haz un **fork** del repositorio.
2. Crea una **rama** para tu mejora o corrección.
3. Realiza un **pull request** con una descripción clara de los cambios.

---

# 📬 Contacto

📧 jhizquier.dev@gmail.com
