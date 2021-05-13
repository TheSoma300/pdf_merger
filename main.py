from PyPDF2 import PdfFileMerger
course_path = "courses/web_sci/all_individual/"
pdfs = [f"{course_path}{i}.pdf" for i in range(1, 13)]

merger = PdfFileMerger()

for pdf in pdfs: 
    merger.append(pdf)

merger.write("courses/web_sci/all_notes.pdf")
merger.close()