from docxtpl import DocxTemplate
doc=DocxTemplate("WordAutomation\Resume_One Page for Experienced resume.docx")
context={
    "person_name":"Shane Warne",
    "person_role":"Software Developer"
}
doc.render(context)
doc.save("WordAutomation\generated_doc.docx")