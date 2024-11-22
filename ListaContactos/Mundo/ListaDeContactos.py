from Mundo.Contacto import Contacto 

class ListaDeContactos: 
    __method__ = "darTodosLosContactos"
    __parameter__ = "Ninguno"
    __returns__ = "Lista de nombres"
    __description__ = "Método que retorna una lista con los nombres completos de todos los contactos"
    def darTodosLosContactos(self):
        nombres = [f"{contacto.darNombre()} {contacto.darApellido()}" for contacto in self.__contactos] 
        return nombres 

    __method__ = "buscarContactosPalabraClave"
    __parameter__ = "palabra"
    __returns__ = "Lista de nombres"
    __description__ = "Método que retorna una lista de nombres completos de contactos que contienen la palabra clave"
    def buscarContactosPalabraClave(self, palabra): 
        resultado = [
            f"{contacto.darNombre()} {contacto.darApellido()}" 
            for contacto in self.__contactos 
            if palabra in contacto.darPalabras() or palabra in contacto.darNombre() or palabra in contacto.darApellido() 
        ] 
        return resultado 

    __method__ = "buscarContacto"
    __parameter__ = "nombre, apellido"
    __returns__ = "Contacto o None"
    __description__ = "Método que busca un contacto por nombre y apellido"
    def buscarContacto(self, nombre, apellido):
        for contacto in self.__contactos: 
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido: 
                return contacto 
        return None 

    __method__ = "agregarContacto"
    __parameter__ = "nombre, apellido, direccion, correo, telefonos, palabras"
    __returns__ = "Ninguno"
    __description__ = "Método que agrega un nuevo contacto si no existe uno con el mismo nombre y apellido."
    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras): 
        if self.buscarContacto(nombre, apellido): 
            return False 
        nuevo_contacto = Contacto(nombre, apellido, direccion, correo) 
        for telefono in telefonos:
            nuevo_contacto.agregarTelefono(telefono)
        for palabra in palabras:  
            nuevo_contacto.agregarPalabra(palabra) 
        self.__contactos.append(nuevo_contacto) 
        return True 

    __method__ = "eliminarContacto"
    __parameter__ = "nombre, apellido"
    __returns__ = "Ninguno"
    __description__ = "Método que elimina un contacto"
    def eliminarContacto(self, nombre, apellido): 
        contacto = self.buscarContacto(nombre, apellido) 
        if contacto: 
            self.__contactos.remove(contacto) 
            return True 
        return False 

    __method__ = "modificarContacto"
    __parameter__ = "nombre: Nombre del contacto, apellido: Apellido del contacto, direccion: Nueva dirección, correo: Nuevo correo, telefonos: Lista de nuevos teléfonos, palabras: Lista de nuevas palabras clave"
    __returns__ = "Ninguno"
    __description__ = "Método que modifica los datos de un contacto existente."
    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras): 
        contacto = self.buscarContacto(nombre, apellido) 
        if not contacto: 
            return False 
        contacto.cambiarDireccion(direccion) 
        contacto.cambiarCorreo(correo) 
        contacto.darTelefonos().clear() 
        for telefono in telefonos: 
            contacto.agregarTelefono(telefono) 
        contacto.darPalabras().clear() 
        for palabra in palabras: 
            contacto.agregarPalabra(palabra) 
        return True




    
