# Sistema de Tutor Inteligente STI

-->  Ver rama development

El objetivo principal de esta aplicación es enseñar programación a los estudiantes que cursan Programación I en la Escuela de Ingeniería de Sistemas de la Universidad de Los Andes (ULA), mediante la implementación de una serie de tutoriales y lecciones, con un Agente Inteligente (Tutor Inteligente) que sea capaz de ayudar y guiar al estudiante en su proceso de aprendizaje.

Proyecto en Django con HTML del admin template: light-bootstrap-dashboard-html-v2.0.1

# Instalación:

--> Ver ramas ocultas después de clonar
un repositorio:
	git branch -a

--> Activar rama oculta
	git checkout development

--> Crear y activar entorno virtual
	virtualenv -p python3.6 mi_venv
	source mi_venv/bin/activate

-->Instalar requerimientos
	pip install -r requirements.txt

-->Creación y configuración BD postgress
	--> Instalar y configurar postgress 
 	--> Cambiar al usuario postgres (por defecto)
 		sudo su postgres
 	--> Ver  lista de tablas existentes
 		psql -l
 	--> Crear nueva BD para el proyecto
 		createdb sti

 --> Configuración archivo settings.py
 	 'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sti', --> nombre de la BD que acabamos de crear
        'USER': 'postgres', -->usuario por defecto
        'PASSWORD': '453672', --> clave para el usuario postgres en la BD
        'HOST': 'localhost',
        'PORT': 5432,
    }

--> Migrar BD
	python manage.py migrate

--> Ejecutar el servidor de python
	python manage.py runserver


* Proyecto integrado:
--> Materias: Base de Datos (BD), Ingeniería del Software (IS), Inteligencia Artificial (IA), Sistemas Operativos (SO).

* Integrantes: Sarait Hernández (BD, IA, IS, SO), Heizel Ortega (IS), Lizandro Zerpa (BD, IA, IS, SO), Kristo Lopez (BD), Pedro Vilchez (IA).