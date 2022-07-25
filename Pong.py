import turtle
import winsound   

wind = turtle.Screen()  # minúscula para el título del módulo y Mayúscula para el nombre de la clase
wind.title('Pong by Fede')
wind.bgcolor('black')
wind.setup(width=800, height=600)
wind.tracer(0)  # Detiene la actualización de la ventana, con lo cual debemos actualizar manualmente // acelera el juego

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)           # Velocidad de la animación
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4   # Movimiento en X / delta X o cambio en X // puedo acomodar los valores según que tan rápido quiero que sea el juego
ball.dy = -0.4  # Delta Y o cambio en Y

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()    # Oculto 'pen' para solo ver el texto
pen.goto(0, 260)
pen.write('Player A: 0 Player B: 0', align="center", font=('Courier', 24, 'normal'))

# Function  # una funcion es una parte del programa que hace algo para lo cual fue definido
def paddle_a_up():  # Defino función: quiero ir más arriba en la pantalla
    y = paddle_a.ycor() # variable 'y' para la coordenada 'y'. El nombre de la variable "paddle_a" + la coordenada 'y'
    y += 20  # Agrega 20px a la coordenada 'y'
    paddle_a.sety(y)  #establece 'y' a la nueva 'y'

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wind.listen()
wind.onkeypress(paddle_a_up, 'w')  # Establezco que con la 'W' voy para arriba
wind.onkeypress(paddle_a_down, 's')  # Establezco que la 's' va para abajo

wind.onkeypress(paddle_b_up, 'Up')
wind.onkeypress(paddle_b_down, 'Down')

# Main game loop

while True:
    wind.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # seteo la X como combinacion de la coordenada X + el cambio de X
    ball.sety(ball.ycor() + ball.dy)

    # Border checking   /establezco un límite, en este caso, como la altura es 600, 290 sería en la parte superior y -290 en la inferior
    if ball.ycor() > 290:   # si la cooordenada Y es mayor a 290,
        ball.sety(290)     # entonces seteo la pelota de nuevo en 290
        ball.dy *= -1  # se invierte la dirección / Multiplica por -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:   # si la cooordenada Y es menor a -290,
        ball.sety(-290)      # entonces seteo la pelota de nuevo en -290
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)    # Si la pelota llega a más de 390 vuelve al centro
        ball.dx *= -1
        score_a += 1   # Si la posicion de la pelota es mayor a 390, significa que el jugador B perdió, por lo tanto es un punto más para el jugador A
        pen.clear() # Borra el valor anterior para que no se superpongan los números
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align="center", font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *=-1
        score_b += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align="center", font=('Courier', 24, 'normal'))

    # Paddle and Ball collision  / Si la coord X de la pelota es mayor a 340, es decir 350 (límite de la ventana) - 10 (ancho de la paleta)
    # y la cordenada Y de la pelota es menor a la coordenada Y de la paleta B + 40 (el tamaño de la pelota) y la coord Y de la pelota es 
    # mayor a la la coord Y de la paleta B - 40
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340) # Agrego la condición 'ball.xcor() < 350' para que la pelota no se quede rebotando entre la pared y la paleta si queda detras de esta
        ball.dx *= -1  # Entonces la pelota cambia de dirección ("rebota")
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)