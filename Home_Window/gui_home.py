import sys
from PIL import Image

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6.QtWidgets import QFileDialog

from Home_Window.UI.home_window import Ui_MainWindow
from Home_Window.utils.pil2pixmap import pil2pixmap
from ALS_Diagnostic_Model.src.utils.predict_image import predict_image
from ALS_Diagnostic_Model.src.utils.load_model import load_model
from ALS_Diagnostic_Model.src.utils.gradcam import extract_cam_and_image, generate_gradcam_overlay, generate_gradcam_circles


class GuiHome(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.input_image_path = ""
        self.pb_browse_image.clicked.connect(self.browse_image)

        self.cam, self.reconstructed_image = None, None
        self.pb_run_analysis.clicked.connect(self.run_analysis)

        self.s_filter_slider.valueChanged.connect(self.update_cam_mask)

    @qtc.Slot()
    def browse_image(self):

        self.input_image_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select an Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.tif)"
        )

        if self.input_image_path:
            try:
                pil_image = Image.open(self.input_image_path)
                pixmap = pil2pixmap(pil_image)

                self.lb_input_image.setPixmap(
                    pixmap.scaled(
                        self.lb_input_image.size()
                    )
                )


                self.lb_image_no.setText("No Image No.")
                self.lb_case_id.setText("No Case ID")
                self.lb_region.setText("No Region")

                self.lb_status.setText("Status: Ready to Run Analysis.")
                self.lb_status.setStyleSheet("""
                    background-color: #FFC107;  
                    color: #BF360C;             
                    padding: 4px;
                    border-radius: 3px;
                """)

            except Exception as e:
                print(e)
                self.lb_input_image.setText("Unable to load image.")

    def update_progress_bar(self, results:list):

        class_labels = ["control", "concordant", "discordant"]

        for label, value in zip(class_labels, results):
            bar = getattr(self, f"p_bar_{label}")
            bar.setValue(int(value*100))

        ranked = sorted(
            zip(class_labels, results),
            key=lambda x: x[1],
            reverse=True  # Highest confidence first
        )

        rank_colors = ["#4CAF50", "#FFA726", "#FFEB3B"]  # Green, Orange, Yellow

        for i, (label, _) in enumerate(ranked):
            bar = getattr(self, f"p_bar_{label}")
            color = rank_colors[i]
            bar.setStyleSheet(f"""
                QProgressBar {{
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    text-align: center;
                }}
                QProgressBar::chunk {{
                    background-color: {color};
                    width: 10px;
                }}
            """)

    @qtc.Slot()
    def run_analysis(self):

        weights_path = r"C:\Users\vijay\Neuro_BioMark\ALS_app_v1\ALS_Diagnostic_Model\src\model\weights.pth"
        model = load_model(weights_path)

        predicted_class, probs, image_tensor, class_idx = predict_image(model, self.input_image_path)

        self.update_progress_bar(probs)

        self.cam, self.reconstructed_image = extract_cam_and_image(model, image_tensor, class_idx)
        cam_image = generate_gradcam_overlay(self.cam, self.reconstructed_image)
        pixmap = pil2pixmap(cam_image)
        self.lb_cam_image.setPixmap(
            pixmap.scaled(
                self.lb_cam_image.size()
            )
        )

        self.s_filter_slider.setValue(80)
        filtered_image = generate_gradcam_circles(self.cam, self.reconstructed_image.copy(), threshold=0.8)
        pixmap = pil2pixmap(filtered_image)
        self.lb_filtered_image.setPixmap(
            pixmap.scaled(
                self.lb_filtered_image.size()
            )
        )


        self.lb_status.setText("Status: Analysis Completed.")
        self.lb_status.setStyleSheet("""
            background-color: #C8E6C9; 
            color: #2E7D32;          
            padding: 4px;
            border-radius: 3px;
        """)

    @qtc.Slot()
    def update_cam_mask(self):
        self.lb_filtered_image.clear()
        threshold = self.s_filter_slider.value()/100
        filtered_image = generate_gradcam_circles(self.cam, self.reconstructed_image.copy(), threshold=threshold)
        pixmap = pil2pixmap(filtered_image)
        self.lb_filtered_image.setPixmap(
            pixmap.scaled(
                self.lb_filtered_image.size()
            )
        )


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = GuiHome()
    window.show()
    sys.exit(app.exec())