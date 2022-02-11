from fpdf import FPDF
import json

pdf=FPDF('P','mm','Letter')
pdf.add_page()

resumeData = open('Resumeinfo.json', 'r')
resumeFile = resumeData.read()
Resume = json.loads(resumeFile) 

pdf.set_font ('helvetica', 'B',  20)
pdf.cell(195,10, 'Personal Information', ln=True, border=True)

pdf.set_font ('helvetica', '',  14)
pdf.cell(10,7, Resume [0] ['Name'], ln=True,)
pdf.cell(10,7, Resume [0] ['Address'], ln=True,)
pdf.cell(10,7, Resume [0] ['Email Address'], ln=True,)
pdf.cell(10,7, Resume [0] ['Contact Number'], ln=True,)

pdf.set_font ('helvetica', 'B',  20)
pdf.cell(195,10, 'Educational Background', ln=True, border=True)

pdf.set_font ('helvetica', '',  14)
pdf.cell(10,7, Resume [0] ['Primary Education'], ln=True,)
pdf.cell(10,7, Resume [0] ['Secondary Education'], ln=True,)
pdf.cell(10,7, Resume [0] ['Tertiary Education'], ln=True,)
pdf.cell(10,7, Resume [0] ['Course'], ln=True,)

pdf.set_font ('helvetica', 'B',  20)
pdf.cell(195,10, 'Technical Skills', ln=True, border=True)

pdf.set_font ('helvetica', '',  14)
pdf.cell(10,7, Resume [0] ['Technical Skills 1'], ln=True,)
pdf.cell(10,7, Resume [0] ['Technical Skills 2'], ln=True,)
pdf.cell(10,7, Resume [0] ['Technical Skills 3'], ln=True,)
pdf.cell(10,7, Resume [0] ['Technical Skills 4'], ln=True,)
pdf.cell(10,7, Resume [0] ['Technical Skills 5'], ln=True,)

pdf.set_font ('helvetica', 'B',  20)
pdf.cell(195,10, 'Work Experience', ln=True, border=True)

pdf.set_font ('helvetica', '',  14)
pdf.cell(10,7, Resume [0] ['Work Experience 1'], ln=True,)
pdf.cell(10,7, Resume [0] ['Work Experience 2'], ln=True,)

pdf.set_font ('helvetica', 'B',  20)
pdf.cell(195,10, 'Positions Applying for', ln=True, border=True)

pdf.set_font ('helvetica', '',  14)
pdf.cell(10,7, Resume [0] ['Position1'], ln=True,)
pdf.cell(10,7, Resume [0] ['Position2'], ln=True,)
pdf.cell(10,7, Resume [0] ['Position3'], ln=True,)

pdf.set_font ('helvetica', 'B',  20)
pdf.cell(195,10, 'Objective', ln=True, border=True)

pdf.set_font ('helvetica', '',  14)
pdf.cell(10,7, Resume [0] ['Objective'], ln=True,)
pdf.cell(10,7, Resume [0] ['Objective2'], ln=True,)

