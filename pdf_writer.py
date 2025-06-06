# -*- coding: utf-8 -*-
"""pdf_writer

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w8z8SHrDX_0fHIDhNpWLPtfHh2LuA0MY
"""

from fpdf import FPDF
import io

class PDFWriter:
    def __init__(self):
        self.pdf = None

    def generate(self, data, output_path=None) -> bytes:
        """
        Generate a PDF summary of the resume data.
        :param data: A dictionary (single resume data) or a list of such dictionaries.
        :param output_path: If provided, save the PDF to this path.
        :return: PDF content as bytes (if output_path is not provided).
        """
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        resumes = data if isinstance(data, list) else [data]

        for idx, resume in enumerate(resumes):
            self.pdf.add_page()
            self.pdf.set_font("Arial", 'B', 16)
            title_text = "Resume Summary"
            if resume.get("name"):
                title_text += f" - {resume['name']}"
            self.pdf.cell(0, 10, title_text, ln=1, align='C')

            self.pdf.set_font("Arial", 'B', 14)
            self.pdf.cell(0, 10, "Profile", ln=1)
            self.pdf.set_font("Arial", '', 12)
            if resume.get("name"):
                self.pdf.cell(0, 8, f"Name: {resume['name']}", ln=1)
            if resume.get("email"):
                self.pdf.cell(0, 8, f"Email: {resume['email']}", ln=1)
            if resume.get("phone"):
                self.pdf.cell(0, 8, f"Phone: {resume['phone']}", ln=1)
            if resume.get("location"):
                self.pdf.cell(0, 8, f"Location: {resume['location']}", ln=1)
            if resume.get("summary"):
                self.pdf.multi_cell(0, 8, f"Summary: {resume['summary']}", align='L')
            self.pdf.ln(2)  

            self.pdf.set_font("Arial", 'B', 14)
            self.pdf.cell(0, 10, "Education", ln=1)
            self.pdf.set_font("Arial", '', 12)
            if resume.get("education"):
                for edu in resume["education"]:
                    school = edu.get("school") or ""
                    degree = edu.get("degree") or ""
                    grad = edu.get("grad_date") or ""
                    gpa = edu.get("GPA") or ""
                    edu_line = school
                    if degree:
                        edu_line += (" - " if edu_line else "") + degree
                    if grad:
                        edu_line += (", " if edu_line else "") + str(grad)
                    if gpa:
                        edu_line += (", GPA: " if edu_line else "GPA: ") + str(gpa)
                    if not edu_line:
                        continue
                    self.pdf.cell(0, 8, edu_line, ln=1)
            else:
                self.pdf.cell(0, 8, "None", ln=1)
            self.pdf.ln(2)

            self.pdf.set_font("Arial", 'B', 14)
            self.pdf.cell(0, 10, "Work Experience", ln=1)
            self.pdf.set_font("Arial", '', 12)
            if resume.get("work_experience"):
                for exp in resume["work_experience"]:
                    title = exp.get("title") or ""
                    company = exp.get("company") or ""
                    dates = exp.get("dates") or ""
                    work_line = ""
                    if title:
                        work_line += title
                    if company:
                        work_line += ("" if not work_line else " at ") + company
                    if dates:
                        work_line += ("" if not work_line else " ") + f"({dates})"
                    if work_line:
                        self.pdf.cell(0, 8, work_line, ln=1)
                    for desc in exp.get("description", []):
                        self.pdf.multi_cell(0, 8, f"    • {desc}", align='L')
                    self.pdf.ln(1)  
            else:
                self.pdf.cell(0, 8, "None", ln=1)
            self.pdf.ln(2)

            self.pdf.set_font("Arial", 'B', 14)
            self.pdf.cell(0, 10, "Skills", ln=1)
            self.pdf.set_font("Arial", '', 12)
            if resume.get("skills"):
                skills_line = ", ".join(resume["skills"])
                self.pdf.multi_cell(0, 8, skills_line, align='L')
            else:
                self.pdf.cell(0, 8, "None", ln=1)
            self.pdf.ln(1)

            self.pdf.set_font("Arial", 'B', 14)
            self.pdf.cell(0, 10, "Certifications", ln=1)
            self.pdf.set_font("Arial", '', 12)
            if resume.get("certifications"):
                certs_line = ", ".join(resume["certifications"])
                self.pdf.multi_cell(0, 8, certs_line, align='L')
            else:
                self.pdf.cell(0, 8, "None", ln=1)
            self.pdf.ln(1)

            self.pdf.set_font("Arial", 'B', 14)
            self.pdf.cell(0, 10, "Extracurriculars", ln=1)
            self.pdf.set_font("Arial", '', 12)
            if resume.get("extracurriculars"):
                extra_line = ", ".join(resume["extracurriculars"])
                self.pdf.multi_cell(0, 8, extra_line, align='L')
            else:
                self.pdf.cell(0, 8, "None", ln=1)
            self.pdf.ln(1)

        if output_path:
            self.pdf.output(output_path)
            return None
        else:
            buffer = io.BytesIO()
            self.pdf.output(buffer)
            return buffer.getvalue()