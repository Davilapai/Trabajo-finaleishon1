class Contacto:

    def __init__(self, nombre, apellido, direccion, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.correo = correo
        self.telefonos = []  
        self.palabras_clave = []  
    
    __method__ = "darNombre"
    __parameter__ = "Ninguno"
    __reutrns__ = "Nombre"
    __description__ = "Metodo que retorna el nombre"  
    def darNombre(self):
        return self.nombre

    __method__ = "darApellido"
    __parameter__ = "Ninguno"
    __returns__ = "Apellido"
    __description__ = "Método que retorna el apellido"
    def darApellido(self):
        return self.apellido

    __method__ = "darDireccion"
    __parameter__ = "Ninguno"
    __returns__ = "Direccion"
    __description__ = "Método que retorna la dirección"
    def darDireccion(self):
        return self.direccion

    __method__ = "darCorreo"
    __parameter__ = "Ninguno"
    __returns__ = "Correo"
    __description__ = "Método que retorna el correo electrónico"
    def darCorreo(self):
        return self.correo

    __method__ = "darTelefonos"
    __parameter__ = "Ninguno"
    __returns__ = "Lista de teléfonos"
    __description__ = "Método que retorna la lista de números de teléfono"
    def darTelefonos(self):
        return self.telefonos

    __method__ = "darPalabras"
    __parameter__ = "Ninguno"
    __returns__ = "Lista de palabras clave"
    __description__ = "Método que retorna la lista de palabras clave asociadas al contacto"
    def darPalabras(self):
        return self.palabras_clave

    __method__ = "cambiarDireccion"
    __parameter__ = "direccion"
    __returns__ = "Ninguno"
    __description__ = "Método que cambia la dirección del contacto"
    def cambiarDireccion(self, direccion):
        self.direccion = direccion

    __method__ = "cambiarCorreo"
    __parameter__ = "correo"
    __returns__ = "Ninguno"
    __description__ = "Método que cambia el correo electrónico del contacto"
    def cambiarCorreo(self, correo):
        self.correo = correo

    __method__ = "agregarTelefono"
    __parameter__ = "telefono"
    __returns__ = "Ninguno"
    __description__ = "Método que agrega un teléfono a la lista de teléfonos si no existe"
    def agregarTelefono(self, telefono):
        if telefono not in self.telefonos:
            self.telefonos.append(telefono)

    __method__ = "eliminarTelefono"
    __parameter__ = "telefonoEliminar"
    __returns__ = "Ninguno"
    __description__ = "Método que elimina un teléfono de la lista si existe"
    def eliminarTelefono(self, telefonoEliminar):
        if telefonoEliminar in self.telefonos:
            self.telefonos.remove(telefonoEliminar)

    __method__ = "agregarPalabra"
    __parameter__ = "palabra"
    __returns__ = "Ninguno"
    __description__ = "Método que agrega una palabra clave a la lista de palabras si no existe"
    def agregarPalabra(self, palabra):
        if palabra not in self.palabras_clave:
            self.palabras_clave.append(palabra)

    __method__ = "eliminarPalabra"
    __parameter__ = "palabraEliminar"
    __returns__ = "Ninguno"
    __description__ = "Método que elimina una palabra clave de la lista si existe"
    def eliminarPalabra(self, palabraEliminar):
        if palabraEliminar in self.palabras_clave:
            self.palabras_clave.remove(palabraEliminar)

    __method__ = "contienePalabraClave"
    __parameter__ = "palabra"
    __returns__ = "Bool"
    __description__ = "Método que verifica si una palabra clave existe en la lista de palabras clave"
    def contienePalabraClave(self, palabra):
        return palabra in self.palabras_clave
