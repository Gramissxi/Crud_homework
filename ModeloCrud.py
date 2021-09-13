from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import Controlador


def validarCampos():
    if ventana.txtNombre.text()=="" or ventana.txtCorreo.text()=="" :
        alerta=QMessageBox()
        alerta.setText("¡Debes de llenar los campos!")
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()
        return True 


def caracter():
    try:
        if ventana.txtNombre.text()== {'%','#','&','$','!'} or ventana.txtCorreo.text()== {'%','#','&','$','!'}:
         print("Error")
    except:
        print("Listo")
    return False
    
    
def crear():
    if validarCampos() and caracter():
        return False
    nombre=ventana.txtNombre.text()
    correo=ventana.txtCorreo.text()
    print(nombre,correo)

    objContactos=Controlador.contactos()
    objContactos.crearContacto((nombre,correo))
    consultar()

def crearvalidacion():
    if caracter():
       return True
    nombre=ventana.txtNombre.text()
    correo=ventana.txtCorreo.text()
    print(nombre, correo)

    objContactos=Controlador.contactos()
    objContactos.crearContacto((nombre,correo))
    consultar()
    

def borrar():
    id=ventana.txtID.text()
    objContactos=Controlador.contactos()
    objContactos.borrarContacto(id)
    consultar()

def modificar():
    id=ventana.txtID.text()
    nombre=ventana.txtNombre.text()
    correo=ventana.txtCorreo.text()
  
    objContactos=Controlador.contactos()
    objContactos.modificarContacto([nombre,correo,id])
    consultar()
    

def cancelar():
    consultar()

def consultar():
    ventana.tblContactos.setRowCount(0)
    indiceControl=0
    objContactos=Controlador.contactos()
    contactos=objContactos.leerContactos()
    for contacto in contactos:
        ventana.tblContactos.setRowCount(indiceControl+1)
        ventana.tblContactos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        indiceControl+=1 #INCREMENTAL PARA QUE SE MUESTRE UNO DETRAS DE OTRO
    
    ventana.txtID.setText("")
    ventana.txtNombre.setText("")
    ventana.txtCorreo.setText("")
    
    ventana.btnCrear.setEnabled(True)
    ventana.btnBorrar.setEnabled(False)
    ventana.btnModificar.setEnabled(False)
    ventana.btnCancelar.setEnabled(False)
    


def seleccionar():
    id= ventana.tblContactos.selectedIndexes()[0].data()
    nombre= ventana.tblContactos.selectedIndexes()[1].data()
    correo= ventana.tblContactos.selectedIndexes()[2].data()
    print(id,nombre,correo)
    
    ventana.txtID.setText(id)
    ventana.txtNombre.setText(nombre)
    ventana.txtCorreo.setText(correo)

    ventana.btnCrear.setEnabled(False)
    ventana.btnBorrar.setEnabled(True)
    ventana.btnModificar.setEnabled(True)
    ventana.btnCancelar.setEnabled(True)

aplicacion= QtWidgets.QApplication([])
ventana= uic.loadUi("ventana.ui")
ventana.show()
consultar()

ventana.tblContactos.setHorizontalHeaderLabels(['ID','Nombre','Correo'])
ventana.tblContactos.setEditTriggers(QTableWidget.NoEditTriggers) #para que el usuario no edite
ventana.tblContactos.setSelectionBehavior(QTableWidget.SelectRows)

ventana.tblContactos.cellClicked.connect(seleccionar)

ventana.btnCrear.clicked.connect(crear)  #Unimos el boton con las funciones
ventana.btnBorrar.clicked.connect(borrar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnCancelar.clicked.connect(cancelar)


sys.exit(aplicacion.exec())