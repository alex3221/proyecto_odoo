# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import *

class proyecto_final(models.Model):
    _name = 'proyecto_final.proyecto_final'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

class jugador(models.Model):
    _name = 'proyecto_final.jugador'

    name = fields.Char(string = "DNI", required = True)
    nombre = fields.Char(string ="Nombre", required = True)
    apellidos = fields.Char(string="Apellidos", required = True)
    fecha_nac = fields.Date(string="Fecha de nacimiento", required = True)
    edad = fields.Integer(compute="_value_calculo", store = True)
    nacionalidad = fields.Char(string="Nacionalidad", required = True)
    equipo = fields.Many2one("proyecto_final.equipo", string = "Equipo")

    @api.depends('fecha_nac')
    def _value_calculo(self):
        """Updates age field when birth_date is changed"""
        if self.fecha_nac:
            d1 = datetime.strptime(self.fecha_nac, "%Y-%m-%d").date()
            d2 = date.today()
            self.edad = relativedelta(d2, d1).years

class equipo(models.Model):
    _name = 'proyecto_final.equipo'

    name = fields.Char(string = "Nombre", required = True)
    icono = fields.Binary()
    torneo = fields.Many2many("proyecto_final.torneo", string = "Torneos")
    jugador = fields.One2many("proyecto_final.jugador", "equipo", string = "Jugadores")
    partida_equipo1 = fields.One2many("proyecto_final.partida", "equipo1", string = "Equipo 1")
    partida_equipo2 = fields.One2many("proyecto_final.partida", "equipo2", string = "Equipo 2")


class torneo(models.Model):
    _name = 'proyecto_final.torneo'

    name = fields.Char(string = "Nombre", required = True)
    lugar = fields.Char(string="Lugar", required = True)
    premio = fields.Integer(string="Premio", required = True)
    fecha_comienzo = fields.Date(string="Fecha de inicio", required = True)
    duracion = fields.Integer(string = "Duracion", required = True )
    equipo = fields.Many2many( "proyecto_final.equipo", # modelo relacionado
                            'proyecto_final_torneo_equipo_rel', # nombre de la tabla de relación
                            'torneo', # campo para "este" registro
                            'equipo', # campo para "otro" registro
                             string='Equipos')
    partida = fields.One2many("proyecto_final.partida", "torneo",string= "Partidas")

class partida(models.Model):
    _name = 'proyecto_final.partida'

    name = fields.Integer(string = "Identificador", required = True)
    equipo1 = fields.Many2one("proyecto_final.equipo", string = "Primer equipo")
    equipo2 = fields.Many2one( "proyecto_final.equipo", string = "Segundo equipo")
    resultado = fields.Selection([('0','1'),('1','2')], default = 0, string="Resultado")
    torneo = fields.Many2one("proyecto_final.torneo")
