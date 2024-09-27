<?php

$dir = isset($_GET['dir']) ? $_GET['dir'] : dirname(__FILE__);
scanDirectory($dir);

function scanDirectory($dir) {
    $archivos = scandir($dir);

    foreach ($archivos as $archivo) {
        if ($archivo != '.' && $archivo != '..') {
            $rutaArchivo = $dir . '/' . $archivo;

            // Obtener los atributos del archivo usando la función stat
            $infoArchivo = stat($rutaArchivo);

            // Obtener el propietario y el grupo
            $propietario = posix_getpwuid($infoArchivo['uid']);
            $grupo = posix_getgrgid($infoArchivo['gid']);

            // Obtener permisos
            $permisos = substr(sprintf('%o', fileperms($rutaArchivo)), -4);

            // Mostrar información del archivo
            echo "Nombre del archivo: $archivo\n";
            echo "Ruta completa: $rutaArchivo\n";
            echo "Tamaño: " . $infoArchivo['size'] . " bytes\n";
            echo "Último acceso: " . date('Y-m-d H:i:s', $infoArchivo['atime']) . "\n";
            echo "Última modificación: " . date('Y-m-d H:i:s', $infoArchivo['mtime']) . "\n";
            echo "Último cambio: " . date('Y-m-d H:i:s', $infoArchivo['ctime']) . "\n";
            echo "Propietario: " . $propietario['name'] . "\n";
            echo "Grupo: " . $grupo['name'] . "\n";
            echo "Permisos: $permisos\n";
            echo "---------------------------------------------\n";
        }
    }
}