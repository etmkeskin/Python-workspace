from fpdf import FPDF

pdf = FPDF()

x = 10  # X-coordinate for the image
y = 10  # Y-coordinate for the image
w = 100  # Width of the image
h = 100  # Height of the image
imageList = ["pi.png", "pihole.png"]

for image in imageList:
    pdf.add_page()
    try:
        pdf.image(image, x, y, w, h)
    except Exception as e:
        print(f"Error adding image '{image}': {str(e)}")
pdf.output("yourfile.pdf", "F")
