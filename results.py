import aspose.pdf as pdf
import datetime
# Set the source files directory path
#filePath = "C:/Users/USUARIO/Desktop/pdf_python/"
filePath = "C:/Users/USER/Desktop/pdf_python/"
#paciente = "Juan"

def results(paciente, LI, PAZ, LAU):
    
    def nombre_archivo_fecha():
        current_datetime = datetime.datetime.now()
        date = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        file_date = "_"+date
        return file_date

    # Define a base font size
    game_font_size = 12
    header_font_size = 10
    body_font_size = 9

    lvl = 1
    row = 0
    document = pdf.Document()
    page = document.pages.add()
    text_fragment = pdf.text.TextFragment("SECCIÓN #1: RESULTADOS VIDEOJUEGO ATENCIÓN")
    text_fragment.text_state.font_size = game_font_size
    page.paragraphs.add(text_fragment)
    for row in range(5):
        text_fragment1 = pdf.text.TextFragment("")
        text_fragment2 = pdf.text.TextFragment("[  NIVEL #" + str(lvl) + "  ]")
        text_fragment3 = pdf.text.TextFragment("     Puntaje Total de Objetos Recogidos: " + str(PAZ[row][0]))
        text_fragment4 = pdf.text.TextFragment("     Tiempo Utilizado: " + str(PAZ[row][1]))
        text_fragment5 = pdf.text.TextFragment("     Tiempo Restante: " + str(PAZ[row][2]))
        text_fragment6 = pdf.text.TextFragment("     Misiones Cumplidas: " + str(PAZ[row][3]))
        text_fragment7 = pdf.text.TextFragment("     Errores Totales: " + str(PAZ[row][4]))
        text_fragment1.text_state.font_size = body_font_size
        text_fragment2.text_state.font_size = header_font_size
        text_fragment3.text_state.font_size = body_font_size
        text_fragment4.text_state.font_size = body_font_size
        text_fragment5.text_state.font_size = body_font_size
        text_fragment6.text_state.font_size = body_font_size
        text_fragment7.text_state.font_size = body_font_size
        
        page.paragraphs.add(text_fragment1)
        page.paragraphs.add(text_fragment2)
        page.paragraphs.add(text_fragment3)
        page.paragraphs.add(text_fragment4)
        page.paragraphs.add(text_fragment5)
        page.paragraphs.add(text_fragment6)
        page.paragraphs.add(text_fragment7)
        lvl += 1 

    lvl = 1
    row = 0
    page2 = document.pages.add()
    text_fragment = pdf.text.TextFragment("SECCIÓN #2: RESULTADOS VIDEOJUEGO MEMORIA")
    text_fragment.text_state.font_size = game_font_size
    page2.paragraphs.add(text_fragment)
    for row in range(10):
        text_fragment1 = pdf.text.TextFragment("")
        text_fragment2 = pdf.text.TextFragment("[  NIVEL #" + str(lvl) + "  ]")
        text_fragment3 = pdf.text.TextFragment("     Aciertos: " + str(LI[row][0]))
        text_fragment4 = pdf.text.TextFragment("     Errores: " + str(LI[row][1]))
        text_fragment5 = pdf.text.TextFragment("     Tiempo Utilizado: " + str(LI[row][2]))
        text_fragment6 = pdf.text.TextFragment("     Tiempo Restante: " + str(LI[row][3]))
        text_fragment1.text_state.font_size = body_font_size
        text_fragment2.text_state.font_size = header_font_size
        text_fragment3.text_state.font_size = body_font_size
        text_fragment4.text_state.font_size = body_font_size
        text_fragment5.text_state.font_size = body_font_size
        text_fragment6.text_state.font_size = body_font_size
        
        page2.paragraphs.add(text_fragment1)
        page2.paragraphs.add(text_fragment2)
        page2.paragraphs.add(text_fragment3)
        page2.paragraphs.add(text_fragment4)
        page2.paragraphs.add(text_fragment5)
        page2.paragraphs.add(text_fragment6)
        
        lvl += 1 

    lvl = 1
    row = 0
    page3 = document.pages.add()
    text_fragment = pdf.text.TextFragment("SECCIÓN #3: RESULTADOS VIDEOJUEGO SECUENCIA LÓGICA")
    text_fragment.text_state.font_size = game_font_size
    page3.paragraphs.add(text_fragment)
    for row in range(10):
        text_fragment1 = pdf.text.TextFragment("")
        text_fragment2 = pdf.text.TextFragment("[  NIVEL #" + str(lvl) + "  ]")
        text_fragment3 = pdf.text.TextFragment("     Tiempo Utilizado: " + str(LAU[row][0]))
        text_fragment4 = pdf.text.TextFragment("     Tiempo Restante: " + str(LAU[row][1]))
        text_fragment5 = pdf.text.TextFragment("     Aciertos: " + str(LAU[row][2]))
        text_fragment6 = pdf.text.TextFragment("     Errores: " + str(LAU[row][3]))
        text_fragment7 = pdf.text.TextFragment("     Número de Intentos: " + str(LAU[row][4]))
        text_fragment1.text_state.font_size = body_font_size
        text_fragment2.text_state.font_size = header_font_size
        text_fragment3.text_state.font_size = body_font_size
        text_fragment4.text_state.font_size = body_font_size
        text_fragment5.text_state.font_size = body_font_size
        text_fragment6.text_state.font_size = body_font_size
        text_fragment7.text_state.font_size = body_font_size
        
        page3.paragraphs.add(text_fragment1)
        page3.paragraphs.add(text_fragment2)
        page3.paragraphs.add(text_fragment3)
        page3.paragraphs.add(text_fragment4)
        page3.paragraphs.add(text_fragment5)
        page3.paragraphs.add(text_fragment6)
        page3.paragraphs.add(text_fragment7)
        
        lvl += 1 

    output = paciente+"_ResultadosVideojuegos"+nombre_archivo_fecha()+".pdf"
    document.save(filePath + output)




