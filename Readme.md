# Automatización - Prueba DDB
Automatización login en la plataforma test.conectadosmexico.com/login

# Como clonar el repositorio
Paso 1: Instalar git 

        Windows: https://git-scm.com/download/win 
        MAC: https://git-scm.com/download/mac 
        General: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git

Paso 2: Abrir git por terminal Windows: CMD MAC: Terminal

Paso 3: Ingresar a la carpeta donde se va a clonar el proyecto.

- ls
- cd Documents/

Paso 4: Para clonar el proyecto se debe ejecutar el siguiente comando git clone
- https://github.com/luisDevPKG/PruebaTecnicaDDB.git

# Como configurar el entorno para la ejecución de la automatizacion
Paso 1: Descargar e instalar Python en la versión estable Paso 2: Instalar el entorno de desarrollo de su preferencia, se aconseja PyCharm (versión community) para Python:

    Windows: https://www.jetbrains.com/pycharm/download/?section=windows
    MAC: https://www.jetbrains.com/pycharm/download/?section=mac

Paso 2: Descargar Google Chrome Driver (PATH) actualizado (segun la version de google chrome que tengas) y segund tu SO : https://chromedriver.chromium.org/downloads

Paso 3: Abrir el entorno de desarrolo y abrir la carpeta del repositorio

Paso 4: Descargar e instalar selenium en la versión estable: https://www.selenium.dev/downloads/

Configuracion del WebDriver mediante PATH
Verificar la version del navegador Google Chrome que tiene actualmente el sistema
De acuerdo a la version descargar el WebDriver en la pagina https://chromedriver.chromium.org/downloads
Para la instalacion del PATH puede guiarse de la siguiente pagina: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
En el punto 2 "The PATH Environment Variable" se indica como instalarlo
Paso 6: Configuracion del WebDriver en el script

Abrir Pycharm como administrador, abrir el proyecto de automatizacion
Paso 7: Abrir el Terminal e Instalar las librerias de Selenium, Pytest y Webdriver Manager

- pip install selenium o py -m pip install selenium
- pip install pytest o py -m pip install pytest
- pip install webdriver-manager o py -m pip install webdriver-manager

En caso de que para SO Windows No se visualicen cambios, abrir cmd, ejecutarlo como administrador y ejecutar los mismos codigos mencionados anteiormente

NOTA:
- Para la ejecucion de scripts se establecíó como navegador predeterminado Google chrome
- Recordar que al descargar el repositorio se debe actualizar la ruta del PATH en el archivo utilites