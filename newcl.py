from docxtpl import DocxTemplate
from docx2pdf import convert

company = input("Enter name of the Company : ") 
role = input("Enter name of the Position: ")

context = {'company' : company, 
           'role' : role}
# Open our master template
doc = DocxTemplate("CLtemplate.docx")
# Load them up
doc.render(context)
# Save the file with personalized filename
doc.save('Cover_letter_'+company+'.docx')
#save it as a pdf
convert('Cover_letter_'+company+'.docx')
