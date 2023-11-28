import drawBot as db

canvasSize = 500
db.newDrawing()
db.newPage(canvasSize, canvasSize)

circleSize = 20
stepSize = 40  # Устанавливаем длину шага

# Рисуем круги по вертикали и горизонтали
for x in range(0, canvasSize, stepSize):
    for y in range(0, canvasSize, stepSize):
        db.oval(x, y, circleSize, circleSize)

db.saveImage("grid_of_circles.png")
db.endDrawing()
