from SimpleCV import *

cam = Camera()
threshold = 5.0 # caso a diferença seja maior que o limiar, o movimento será considerado

cont = 0
fps = 2
larguraImg = 640
alturaImg = 480
width = 160
height = 120
rangeJ = (larguraImg/width)
rangeI = (larguraImg/height)

while True:
	antes = cam.getImage() #captura um frame
	time.sleep(1.0/(fps*2)) #espera uma parcela de segundo 
	depois = cam.getImage() #captura outro frame
	depois.show()
	i = 0
	j = 0
	dif = depois - antes
	matrix = dif.getNumpy()
	mean = matrix.mean()
	if mean >= threshold:
		cont = cont + 1
		pathAtual = '../Imagens/img%d_antes.jpg' % (cont,)
		pathAnterior = '../Imagens/img%d_depois.jpg' % (cont,)
		pathDif = '../Imagens/img%d_dif.jpg' % (cont,)
		antes.save(pathAtual)
		depois.save(pathAnterior)
		dif.save(pathDif)
		depois.drawText('Movimento detectado')
		depois.show()		

