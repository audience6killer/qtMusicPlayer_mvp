from PyQt5.QtGui import QPixmap, QColor, QPainter, QBrush
from PyQt5.QtCore import Qt
from colorthief import ColorThief


def get_rounded_pixmap(pixmap: QPixmap, radius=25) -> QPixmap:
    """
    A function to get a pixmap with rounded corners
    :param pixmap: Pixmap to round
    :param radius: Corner radius
    :return: Pixmap rounded
    """
    rounded = QPixmap(pixmap.size())
    rounded.fill(QColor("transparent"))

    # draw rounded rect on new pixmap using original pixmap as brush
    painter = QPainter(rounded)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setBrush(QBrush(pixmap))
    painter.setPen(Qt.PenStyle.NoPen)
    painter.drawRoundedRect(pixmap.rect(), radius, radius)

    return rounded


"""
    TODO: Reduce image size to increment performance
"""
def get_image_color_palette(img_path: str) -> list:
    color_thief = ColorThief(img_path)
    # get the dominant color
    #dominant_color = color_thief.get_color(quality=6)
    # build a color palette
    palette = color_thief.get_palette(color_count=2, quality=5)

    # Color noramlization

    return palette
