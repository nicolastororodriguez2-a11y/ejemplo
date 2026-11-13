from modelo.medicos import Medico,Paciente
from modelo.crudmedico import GestionMedico,GestionPaciente
from vista.vista_medico import VistaControlador

class ControladorMedico:
    def __init__(self):
        self.gestion_Medico=GestionMedico()
        self.gestion_paciente=GestionPaciente()
        
#Controlador medico

    def guardar(self,documento,nombre,apellido,especializacion,telefono):
        medico=Medico(documento,nombre,apellido,especializacion,telefono)
        self.gestion_Medico.guardar_medicos(medico)
    
    def actulizar_medico(self,documento,nombre,apellido,especializacion,telefono):
        medico=Medico(documento,nombre,apellido,especializacion,telefono)
        return self.gestion_Medico.actualizar_medico(medico)
    
    def consultar_medico(self):
        return self.gestion_Medico.consultar()
    
    def consultar_documento(self,documento):
        medico=Medico(documento)
        return self.gestion_Medico.consuldar_decumento(medico)
    
    def eliminar_medico(self,documento):
        medico=Medico(documento)
        return self.gestion_Medico.eliminar(medico)


#Controlador pacientes
    def paciente_guardar(self,documento,nombre,apellido,edad,eps,barrio,telefono):
        paciente=Paciente(documento,nombre,apellido,edad,eps,barrio,telefono)
        self.gestion_paciente.guardar_paciente(paciente)