import drawBot as db

canvasSize = 500
db.newDrawing()
db.newPage(canvasSize, canvasSize)

squareSize = 30
stepSize = 40  # Устанавливаем длину шага

x = 0
while x < canvasSize:
    db.rect(x, 0, squareSize, canvasSize)
    x += stepSize

db.saveImage("vertical_squares.png")
db.endDrawing()
