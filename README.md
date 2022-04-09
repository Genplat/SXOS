# SXOS
A method to install SXOS and run games without problems

Instriucciones:
-Descargar este repositorio

-Ir a https://darthsternie.net/switch-firmwares/ y descargar el Firmware de la version de switch en la que este tu sysnand
-Abrir la carpeta 1
-Ejecutar GetLicense.py
-Clonar el boot.dat y el license.dat a la SD de la switch
-Copiar los datos de switch a la carpeta switch de la SD de la switch
-Copiar la carpeta Firmware 11.0.0 y la carpeta de tu firmware a la SD de la switch
-Ininciar Atmosphere en la Sysnand de la consola
-Desde homebrew abrir ChoiDujourNX
-Seleccionar Firmware 11.0.0 y darle a choose
-Darle a 11.0.0 (exFAT)
-Darle a Select Firmware
-Desactivar AutoRCM
-Darle a Start Installacion
-Darle a reboot
-Darle a Shut down
-Abrir TegraRCM desde la carpeta Tegra y seleccionar SXOS
-Mientras sale el logo de SX darle a volumen + para entrar al menu
-Darle a Options
-Seleccionar EmuNAND
-Darle a Create EmuNAND
-Darle a Files on microSD
-Esperar a que termine
-Ir al menu principal y desactivar EmuMMC
-Darle a Boot Custom FW
-Desde homebrew abrir ChoiDujourNX
-Seleccionar el Firmware donde estaba tu sysnand y darle a choose
-Darle a [Tu firmware] (exFAT)
-Darle a Select Firmware
-Desactivar AutoRCM
-Darle a Start Installacion
-Darle a reboot
-Darle a Shut down
-Abrir TegraRCM desde la carpeta Tegra y seleccionar SXOS
-Mientras sale el logo de SX darle a volumen + para entrar al menu
-Si no esta activado ya activa la emuNAND


-----Listo, ahora ya podras iniciar SXOS inyectando el payload desde TegraRCM y la sysnand de tu consola seguira en su version normal-----


Para poder jugar juegos en el Custom Firmware necesitaras parchear los NSP y XCI, para parchearlos hazlo desde el programa que estara en la carpeta Parchear Juegos
