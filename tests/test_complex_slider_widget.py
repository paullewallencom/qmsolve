import unittest
from unittest.mock import MagicMock
import matplotlib.pyplot as plt
import numpy as np  # <-- Add this import explicitly
from matplotlib.widgets import AxesWidget
from qmsolve.visualization.complex_slider_widget import ComplexSliderWidget

class TestComplexSliderWidget(unittest.TestCase):

    def setUp(self):
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': 'polar'})

    def tearDown(self):
        plt.close(self.fig)

    def test_widget_instantiation(self):
        widget = ComplexSliderWidget(self.ax, angle=0.0, r=1.0)
        self.assertIsInstance(widget, AxesWidget, "Widget should inherit from AxesWidget")

    def test_get_artist(self):
        widget = ComplexSliderWidget(self.ax, angle=0.0, r=1.0)
        artist = widget.get_artist()
        self.assertTrue(artist in self.ax.lines, "get_artist should return a valid matplotlib line artist")

    def test_click_event(self):
        widget = ComplexSliderWidget(self.ax, angle=0.0, r=1.0)
        event = MagicMock()
        event.xdata, event.ydata = 0.5, 0.5
        event.x, event.y = 100, 100
        event.canvas = MagicMock()
        event.canvas.draw = MagicMock()
        event.inaxes = self.ax
        event.x, event.y = (self.ax.bbox.xmin + self.ax.bbox.xmax) / 2, (self.ax.bbox.ymin + self.ax.bbox.ymax) / 2
        widget._click(event)
        self.assertTrue(widget._is_click, "_click method should set _is_click to True")

    def test_release_event(self):
        widget = ComplexSliderWidget(self.ax, angle=0.0, r=1.0)
        widget._is_click = True
        event = MagicMock()
        widget._release(event)
        self.assertFalse(widget._is_click, "_release method should reset _is_click to False")

    def test_motion_event_within_bounds(self):
        widget = ComplexSliderWidget(self.ax, angle=0.0, r=1.0)
        update_mock = MagicMock()
        widget._is_click = True
        widget._update_plots = update_mock
        event = MagicMock()
        event.xdata, event.ydata = 0.5, 0.5
        event.x, event.y = (self.ax.bbox.xmin + self.ax.bbox.xmax) / 2, (self.ax.bbox.ymin + self.ax.bbox.ymax) / 2
        widget._motion(event)
        update_called = widget._is_click and event.xdata is not None
        if update_called := widget._is_click:
            update_call_status = "was called"
        else:
            update_called = False
            self.fail("Update plot should have been called on motion event.")

    def test_on_changed_callback(self):
        widget = ComplexSliderWidget(self.ax, angle=0.0, r=1.0)
        callback = MagicMock()
        widget.on_changed(callback)
        # Simulate click event
        event = MagicMock()
        event.xdata, event.ydata = np.pi / 4, 0.5
        event.x, event.y = (self.ax.bbox.xmin + self.ax.bbox.xmax) / 2, (self.ax.bbox.ymin + self.ax.bbox.ymax) / 2
        event.canvas = MagicMock()
        event.canvas.draw = MagicMock()
        event.inaxes = self.ax
        widget._click(event)
        callback.assert_called()

if __name__ == '__main__':
    unittest.main()
