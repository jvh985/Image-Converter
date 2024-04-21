import os.path
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image

class ImageConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Converter")
        self.setGeometry(100, 100, 400, 200)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        self.file_label = QLabel("No file selected")

        self.browse_button = QPushButton("Browse Image")
        self.browse_button.clicked.connect(self.browse_image)

        self.jpeg_button = QPushButton("JPEG")
        self.jpeg_button.clicked.connect(self.convert_to_jpeg)

        self.png_button = QPushButton("PNG")
        self.png_button.clicked.connect(self.convert_to_png)

        self.gif_button = QPushButton("GIF")
        self.gif_button.clicked.connect(self.convert_to_gif)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addSpacing(20)
        layout.addWidget(self.file_label, alignment=Qt.AlignCenter)
        layout.addSpacing(50)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.jpeg_button)
        layout.addWidget(self.png_button)
        layout.addWidget(self.gif_button)
        self.setLayout(layout)

    def browse_image(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.gif *.webp *.pdf *.avif)", options=options)
        if filename:
            pixmap = QPixmap(filename)
            max_height = 600
            max_width = 800

            # Prevents a large image from making the app window too big
            if pixmap.width() > max_width or pixmap.height() > max_height:
                pixmap = pixmap.scaled(max_width, max_height, Qt.KeepAspectRatio)

            self.image_label.setPixmap(pixmap)
            self.file_label.setText(f"Selected file: {filename}")
            self.image_label.setAlignment(Qt.AlignCenter)

    def convert_image(self, filename, save_filename, file_format):
        file_image = Image.open(filename)
        file_type = file_image.format

        if save_filename:
            if save_filename.endswith('.jpg') and file_type != 'JPEG':
                file_image = file_image.convert('RGB')
            elif save_filename.endswith('.png') and file_type != 'PNG':
                file_image = file_image.convert('RGBA')
            elif save_filename.endswith('.gif') and file_type != 'GIF':
                file_image = file_image.convert('P', palette=Image.ADAPTIVE, colors=256, dither=Image.NONE)

        file_image.save(save_filename)
        QMessageBox.information(self, "Success", f"Image saved as {save_filename} successfully!")

    def convert_to_jpeg(self):
        if self.file_label.text() == "No file selected":
            QMessageBox.warning(self, "Warning", "Please select an image first!")
            return

        filename = self.file_label.text().split(": ")[1]

        save_filename, _ = QFileDialog.getSaveFileName(self, "Save Image As", os.path.dirname(filename), "JPEG (*.jpg)", options=QFileDialog.DontUseNativeDialog)
        if save_filename:
            if not save_filename.endswith('.jpg'):
                save_filename += '.jpg'  # Ensure filename has the correct extension

        self.convert_image(filename, save_filename, "JPEG")

    def convert_to_png(self):
        if self.file_label.text() == "No file selected":
            QMessageBox.warning(self, "Warning", "Please select an image first!")
            return

        filename = self.file_label.text().split(": ")[1]

        save_filename, _ = QFileDialog.getSaveFileName(self, "Save Image As", os.path.dirname(filename), "PNG (*.png)", options=QFileDialog.DontUseNativeDialog)
        if save_filename:
            if not save_filename.endswith('.png'):
                save_filename += '.png'  # Ensure filename has the correct extension

            self.convert_image(filename, save_filename, "PNG")

    def convert_to_gif(self):
        if self.file_label.text() == "No file selected":
            QMessageBox.warning(self, "Warning", "Please select an image first!")
            return

        filename = self.file_label.text().split(": ")[1]

        save_filename, _ = QFileDialog.getSaveFileName(self, "Save Image As", os.path.dirname(filename), "GIF (*.gif)", options=QFileDialog.DontUseNativeDialog)
        if save_filename:
            if not save_filename.endswith('.gif'):
                save_filename += '.gif'  # Ensure filename has the correct extension

            self.convert_image(filename, save_filename, "GIF")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageConverterApp()
    window.show()
    sys.exit(app.exec_())
