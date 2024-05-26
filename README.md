<?xml version="1.0" encoding="UTF-8"?>
<readme>
    <project>
        <name>Proyecto: Ejecución del Script</name>
        <description>Este repositorio contiene un script que puede ejecutarse de dos formas diferentes. A continuación, se detallan las opciones disponibles y los requisitos necesarios para cada método.</description>
    </project>
    
    <executionOptions>
        <option>
            <name>Usar main.exe</name>
            <steps>
                <step>Clonar el repositorio: <command><![CDATA[git clone https://github.com/tu_usuario/tu_repositorio.git]]></command></step>
                <step>Navegar al directorio del repositorio: <command><![CDATA[cd tu_repositorio]]></command></step>
                <step>Asegurarse de tener todas las carpetas y archivos necesarios. Es crucial que todas las carpetas incluidas en el repositorio estén presentes en el mismo directorio que main.exe.</step>
                <step>Ejecutar main.exe:
                    <details>
                        <detail>En Windows, haz doble clic en main.exe o ejecútalo desde la línea de comandos: <command><![CDATA[./main.exe]]></command></detail>
                    </details>
                </step>
            </steps>
        </option>

        <option>
            <name>Usar main.py</name>
            <steps>
                <step>Clonar el repositorio: <command><![CDATA[git clone https://github.com/tu_usuario/tu_repositorio.git]]></command></step>
                <step>Navegar al directorio del repositorio: <command><![CDATA[cd tu_repositorio]]></command></step>
                <step>Instalar las dependencias. Asegúrate de tener Python instalado y utiliza pip para instalar las dependencias necesarias listadas en requirements.txt (si existe): <command><![CDATA[pip install -r requirements.txt]]></command></step>
                <step>Ejecutar main.py: <command><![CDATA[python main.py]]></command></step>
            </steps>
        </option>
    </executionOptions>

    <systemRequirements>
        <requirement>
            <type>Para main.exe</type>
            <details>
                <detail>Sistema operativo: Windows</detail>
                <detail>Todas las carpetas del repositorio deben estar en el mismo directorio que main.exe.</detail>
            </details>
        </requirement>
        <requirement>
            <type>Para main.py</type>
            <details>
                <detail>Python 3.x</detail>
                <detail>Dependencias adicionales (listadas en requirements.txt)</detail>
            </details>
        </requirement>
    </systemRequirements>

    <contributions>
        <welcome>¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos para contribuir:</welcome>
        <steps>
            <step>Haz un fork del repositorio.</step>
            <step>Crea una nueva rama: <command><![CDATA[git checkout -b feature/nueva-funcionalidad]]></command></step>
            <step>Realiza tus cambios y haz commit: <command><![CDATA[git commit -am 'Agrega nueva funcionalidad']]></command></step>
            <step>Haz push a la rama: <command><![CDATA[git push origin feature/nueva-funcionalidad]]></command></step>
            <step>Abre un Pull Request.</step>
        </steps>
    </contributions>

    <license>
        <type>MIT License</type>
        <link>LICENSE</link>
    </license>
</readme>
