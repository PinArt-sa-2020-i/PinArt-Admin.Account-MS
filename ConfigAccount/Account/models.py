from django.db import models

class TipoNotificacion(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=200)

    def __str__(self):
        return "Tipo de notificacion %s" % self.Nombre

class ConfigNotificaciones(models.Model):
    IdUsuario = models.IntegerField()
    IdTipo = models.ForeignKey(TipoNotificacion, on_delete=models.CASCADE)
    Activas = models.BooleanField()

    def __str__(self):
        strActiva = ""
        if self.Activas:
            strActiva = "activada"
        else:
            strActiva = "desactivada"
        return "%s esta %s" % (self.IdTipo, strActiva) 

class Medio(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return "Medio %s" % self.Nombre

class Sesiones(models.Model):
    IdUsuario = models.IntegerField()
    MedioAuth = models.ForeignKey(Medio, on_delete=models.CASCADE)
    Dispositivo = models.CharField(max_length=50)
    Creacion = models.DateTimeField(auto_now_add=True)
    Activo = models.BooleanField()

    def __str__(self):
        return "Sesion en el dispositivo %s por el %s en la fecha %s" % (self.Dispositivo, self.MedioAuth, str(self.Creacion))

class CuentasEnlazadas(models.Model):
    IdUsuario = models.IntegerField()
    MedioAuth = models.OneToOneField(Medio, on_delete=models.CASCADE)
    CorreoEnlazado = models.EmailField()

    def __str__(self):
        return "Cuenta enlazada para el correo %s en el %s" % (self.CorreoEnlazado, self.MedioAuth)