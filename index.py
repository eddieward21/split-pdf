import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf_pages(input_path, output_directory):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Read the input PDF file
    input_pdf = PdfFileReader(open(input_path, 'rb'))

    # Loop through each page and save as separate PDFs
    for page_number in range(input_pdf.numPages):
        # Create a new PDF writer
        output_pdf = PdfFileWriter()
        output_pdf.addPage(input_pdf.getPage(page_number))

        # Generate the output file path
        output_path = os.path.join(output_directory, f'page_{page_number + 1}.pdf')

        # Write the output PDF file
        with open(output_path, 'wb') as output_file:
            output_pdf.write(output_file)

        print(f'Saved page {page_number + 1} as {output_path}')

# Example usage
input_file = 'path/to/larger_file.pdf'
output_directory = 'path/to/output_directory'
split_pdf_pages(input_file, output_directory)
