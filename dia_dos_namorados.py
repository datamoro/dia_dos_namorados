# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:18:14 2023

@author: caiom
"""

import turtle

def draw_heart(namoradx):
    window = turtle.Screen()
    window.bgcolor("pink")
    
    love = turtle.Turtle()
    love.shape("turtle")
    love.color("red")
    love.speed(3)
    
    love.up()
    love.goto(0, -100)
    love.down()
    
    love.begin_fill()
    love.left(140)
    love.forward(180)
    
    love.circle(-90, 200)
    
    love.setheading(60)
    love.circle(-90, 200)
    
    love.forward(180)
    love.end_fill()
    
    love.hideturtle()
    
    love.up()
    love.goto(0, -200)
    love.write(f"Feliz Dia dos Namorados, {namoradx}! Te amo!", align="center", font=("Arial", 18, "bold"))
    
    window.exitonclick()

namoradx = input("Digite o nome do seu namoradx: ")
draw_heart(namoradx)