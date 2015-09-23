#!/usr/bin/env python
#-*- coding:utf-8 -*-
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm, mm, inch, pica
pdf = Canvas("teste.pdf", pagesize = letter) #Nome do arquivo e Tipo do papel

tupla = ('Mayron Cachina', 'José Ustra', 'José Frank', 'Ana Cláudia', 'Karen Velasquez')
lista = pdf.beginText(inch * 1, inch * 10)
for i in range(0,len(tupla)):
    lista.textLine(tupla[i])
pdf.drawText(lista)
'''
#CONTE�DO
'''
pdf.showPage()
pdf.save()