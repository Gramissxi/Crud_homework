import sqlite3
from sqlite3.dbapi2 import connect

#Primero que nada instale los paqueres para diseñar la app desde una manera mas sencilla ya que 
#despues unicamente tuve que importar la carpeta VENTANA.UI que en este caso representa la vista dentro del modelo MVC que hice con Pyqt5 
#me parecio mas prolijo y lo pude interpretar mejor que cosas hacia, porque despues tuve que configurar 
#los nombres desde QT designer para anclarlos en la  parte de modelo Funcion consulta, para asimismo configar los botones.

class contactos:
    def iniciarConexion(self):
        conexion=sqlite3.connect('sistema1.s3db')
        conexion.text_factory= lambda b: b.decode(errors='ignore')
        return conexion

    def leerContactos(self):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL='SELECT * FROM Contactos'
        cursor.execute(sentencialSQL)
        return cursor.fetchall()

    def crearContacto(self,datosContacto):
        conexion=self.iniciarConexion()
        cursor=conexion.cursor()
        sentencialSQL='INSERT INTO Contactos(Nombre,Correo) VALUES(?,?)'
        cursor.execute(sentencialSQL,datosContacto)
        conexion.commit()
        conexion.close()

    def borrarContacto(self,idContacto):
        conexion=self.iniciarConexion()
        cursor=conexion.cursor()
        sentencialSQL='DELETE FROM Contactos WHERE Id=(?)'
        cursor.execute(sentencialSQL,[idContacto])
        conexion.commit()
        conexion.close()

    def modificarContacto(self, datosContacto):
        conexion=self.iniciarConexion()       
        cursor=conexion.cursor()
        sentencialSQL='UPDATE Contactos SET Nombre=? ,Correo=? WHERE Id=?'
        cursor.execute(sentencialSQL,datosContacto)
        conexion.commit()
        conexion.close()
