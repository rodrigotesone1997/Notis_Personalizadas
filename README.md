<h1 align="center">Bienvenido 👋</h1>
<p>
  <a href="LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/rodrigotesone97" target="_blank">
    <img alt="Twitter: Rodrigo Tesone" src="https://img.shields.io/twitter/follow/rodrigotesone97.svg?style=social" />
  </a>
</p>

> Me interesan las Editoriales de [este](https://twitter.com/JonatanViale) periodista pero el canal de Youtube de [La Nación](https://www.youtube.com/c/LaNacionMas) tiene mucho mas contenido que no me interesa. Con este Bot me aseguro de solo ser notificado de el contenido que quiero ver.</br>
> El repositorio consta de:
> - El script [app.py](app.py) que ejecuta las tareas para el funcionamiento del programa.<br/>
> - 1 clase para las funcionalidades de [telegram](clases/telegrambot.py))
> - Un block de notas que se encarga de anotar el ID del último video con la palabra clave. <br/>
> - Las [claves de acceso](keys.dat) para utilizar la api de telegram.

## 📂 Clonar Repositorio

```

git clone https://github.com/rodrigotesone1997/Notis_Personalizadas.git

```

## 🐍 Versión de Python

```
Python 3.8.5
```

## 👨‍💻 Instalación

Además de los requerimientos que estan [aquí](requirements.txt) se necesita tener una [clave de acceso](https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot) para utlizar el bot de telegram.

## ⚙️ Uso

1. (Opcional) Crear un entorno virtual `virtualenv` y activarlo.
2. Instalar las depedencias `pip install -r requirements.txt`
3. Leer el código y ver los comentarios para ver su uso.
4. Ejecutar [app.py](app.py)

## 🤔 ⏰ ¿Como hago para activar el Bot?

#### 🪟 Usuarios Windows:

Para usuarios Windows conviene ejecutar el script dentro del [Task Scheduler](https://www.jcchouinard.com/python-automation-using-task-scheduler/) y ejecutar de Lunes a Viernes a las 22:00 hs.

#### 🐧 Usuarios Linux:

Para usuarios Linux (yo particularmente uso la distribucion Ubuntu 20.04 pero supongo sera similar el proceso para otras distros) se recomienda utilizar [Crontab](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804) con el siguiente comando:

> crontab -e

y luego utilizar:<br />

> 00 22 \* \* 0-4 python3 /path/script/app.py

#### ☁️ Otras practicas:

Tambien se puede poner en produccion el script en un servidor externo como por ejemplo:

- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Google Cloud](https://cloud.google.com/)

Y muchos más.</br>
Yo tengo el bot corriendo en un maquina virtual en la plataforma [AWS](https://aws.amazon.com/)

## ✉️ Contacto

Cualquier sugerencia de arquitectura de código,pregunta o problema enviar mail a rodrigotesone97@outlook.com.ar o a mi [twitter](https://twitter.com/rodrigotesone97)

## 🤔 Autores

👤 **Rodrigo Tesone**

* Twitter: [@rodrigotesone97](https://twitter.com/rodrigotesone97)
* Github: [rodrigotesone1997](https://github.com/rodrigotesone1997)
* LinkedIn: [rodrigo-tesone](https://www.linkedin.com/in/rodrigo-tesone/)

## 📝 Licencia

Copyright © 2021 [Rodrigo](https://github.com/rodrigotesone1997).<br />
This project is [MIT](LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
