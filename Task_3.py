import drawBot as db

canvasSize = 500
db.newDrawing()
db.newPage(canvasSize, canvasSize)

squareSize = 20
stepSize = 40  # Устанавливаем длину шага

# Рисуем квадраты по диагонали
for i in range(0, canvasSize, stepSize):
    db.rect(i, i, squareSize, squareSize)

db.saveImage("diagonal_squares.png")
db.endDrawing()
